import logging
import re

from dateutil.parser import parse as dateparser
from typing import Dict, Union, Any, Tuple
from msrest.authentication import BasicAuthentication
from azure.devops.connection import Connection
import sys
import logging as log
from utils.config import get_config_by_name
from utils.tafexcept import TafError

this = sys.modules[__name__]

home_ado_project = ''
home_ado_team = ''
home_ado_org = ''
home_ado_host = ''
home_ado_url = ''
home_ado_connection = None
home_ado_wi_tracking_client = None
home_ado_work_client = None
git_client = None
static_values = None
build_client = None


# Set up connections
def init(config_name, home_ado_config_name):
    log.info(f"Initializing global parameters")
    cfg = get_config_by_name(config_name)
    log.info(f"Attempting to connect to the target ADO instance: '{home_ado_config_name}'")
    home_ado_cfg = cfg['tools']['azure'][home_ado_config_name]
    this.home_ado_project = home_ado_cfg['project']
    this.home_ado_team = home_ado_cfg['team']
    this.home_ado_org = home_ado_cfg['organization']
    this.home_ado_host = home_ado_cfg['host']
    log.debug(f"\t- Project name {this.home_ado_project}")
    log.debug(f"\t- Team name {this.home_ado_team}")
    log.debug(f"\t- Organization name {this.home_ado_org}")
    log.debug(f"\t- Host name {this.home_ado_host}")
    this.home_ado_url = f"{this.home_ado_host}/{this.home_ado_org}"
    log.debug(f"\t- Setting up authentication")
    home_ado_credentials = BasicAuthentication('', home_ado_cfg['access_token'])
    log.debug(f"\t- Establishing connection...")
    this.home_ado_connection = Connection(base_url=this.home_ado_url, creds=home_ado_credentials)
    log.debug(f"\t- Creating Work Item Tracking client")
    this.home_ado_wi_tracking_client = this.home_ado_connection.clients_v6_0.get_work_item_tracking_client()
    log.info(f"Connection to target ADO instance established {this.home_ado_url}/{this.home_ado_project}")
    log.debug(f"\t- Creating Work client")
    this.static_values = home_ado_cfg['static_values']
    this.home_ado_work_client = this.home_ado_connection.clients_v6_0.get_work_client()
    if this.home_ado_work_client:
        log.info(f"Connection to target ADO instance established for work client "
                 f"{this.home_ado_url}/{this.home_ado_project}")
    else:
        log.error(f"Connection to target ADO instance failed for work client "
                  f"{this.home_ado_url}/{this.home_ado_project}")
        raise Exception(f"Connection to target ADO instance failed for work client ")
    this.git_client = this.home_ado_connection.clients_v6_0.get_git_client()
    if this.git_client:
        log.info(f"Connection to target ADO instance established for git client "
                 f"{this.home_ado_url}/{this.home_ado_project}")
    else:
        log.error(f"Connection to target ADO instance failed for git client "
                  f"{this.home_ado_url}/{this.home_ado_project}")
        raise Exception(f"Connection to target ADO instance failed for git client "
                        f"{this.home_ado_url}/{this.home_ado_project}")
    this.build_client = this.home_ado_connection.clients_v6_0.get_build_client()
    if this.build_client:
        log.info(f"Connection to target ADO instance established for Build client "
                 f"{this.home_ado_url}/{this.home_ado_project}")
    else:
        log.error(f"Connection to target ADO instance failed for Build client "
                  f"{this.home_ado_url}/{this.home_ado_project}")
        raise Exception(f"Connection to target ADO instance failed for Build client "
                        f"{this.home_ado_url}/{this.home_ado_project}")


def _simplify_pr_details(pr_details: Dict[str, Any]) -> Union[Dict[str, Any], None]:
    """
    This function simplifies the pull request details returned by Azure DevOps.
    :param pr_details:
    :return:
    """
    if pr_details is None:
        return None

    pr_summary = {}

    pr_summary['id'] = pr_details['pull_request_id'] if 'pull_request_id' in pr_details else None
    pr_summary['completed'] = False
    if all(field_name in pr_details for field_name in ['status', 'merge_status', 'target_ref_name']):
        if pr_details['status'] == 'completed' and pr_details['merge_status'] == 'succeeded' and \
                pr_details['target_ref_name'] == 'refs/heads/master':
            pr_summary['completed'] = True

    pr_summary['final'] = False
    if 'completion_options' in pr_details:
        if 'delete_source_branch' in pr_details['completion_options']:
            if pr_details['completion_options']['delete_source_branch']:
                pr_summary['final'] = True
                if 'closed_date' in pr_details:
                    try:
                        pr_summary['closed_date'] = dateparser(pr_details['closed_date']).isoformat()
                    except Exception as e:
                        log.error(f"Error parsing closed date: {e}")
                        pr_summary['closed_date'] = None
    return pr_summary


def identify_artifact(artifact_url: str, artifact_relation_attributes: dict = None) -> Union[dict, None]:
    """
    See https://learn.microsoft.com/en-us/azure/devops/boards/queries/link-type-reference for details
    ("External link types" section)

    :param artifact_url:
    :param artifact_relation_attributes:
    :return:
    """
    artifact_key = {}
    if not re.match(r'vstfs:///(Git|Build|ReleaseManagement)/(Commit|Ref|PullRequestId|Build|ReleaseEnvironment)/.*$',
                    artifact_url):
        logging.error(f"The URL is invalid, or the artifact type is not supported {artifact_url}")
        return None
    else:
        low_artifact_url = artifact_url.lower()
        # The first group is always an empty group for various reasons, that's just how Python 're' works,
        # so we drop the first item in the list, and the artifact type is the 3rd (index=2) item
        artifact_type = re.split(
            r'^(?:vstfs:///)(git|build|releasemanagement)/(commit|ref|pullrequestid|build|releaseenvironment)/.*$',
            low_artifact_url)[2]
        if artifact_type in ['commit', 'pullrequestid']:
            artifact_id = re.split(r'%2f|/', low_artifact_url)[-1]
            repository_id = re.split(r'%2f|/', low_artifact_url)[-2]
            artifact_type = artifact_type.replace('id', '')
        elif artifact_type == 'ref':
            artifact_url_parts = re.split(
                r'^(?:vstfs:///)(git)/(ref)/([0-9a-z\-]+)%2f([0-9a-z\-]+)%2f(.*)$',
                low_artifact_url)
            artifact_type = 'branch'
            artifact_id = re.sub(r'^gb', '', artifact_url_parts[5].replace('%2f', '/'))
            repository_id = artifact_url_parts[4]
        elif artifact_type == 'build':
            artifact_id = re.split(r'/', low_artifact_url)[-1]
            repository_id = None
        elif artifact_type == 'releaseenvironment':
            artifact_type = 'release_env'
            artifact_id = re.split(r'/', low_artifact_url)[-1]
            repository_id = None
        else:
            logging.error(f"Unknown artifact type: {artifact_type} in artifact {artifact_url}")
            return None

    artifact_key.update({
        'artifact_type': artifact_type,
        'artifact_id': artifact_id,
        'repository_id': repository_id,
        'artifact_url': artifact_url
    })
    return artifact_key


def get_git_branch_attribs(repo_id: str, branch_path: str, project_name: str = None):
    if not git_client:
        # TODO: Get config and ADO name from context or parameter
        init('DEV', 'AnaChem')
    if not project_name:
        project_name = this.home_ado_project
    try:
        branch_details = git_client.get_branch(repo_id, branch_path, project=project_name)
    except Exception as e:
        branch_details = None
        logging.error(f"Error getting branch details for {branch_path} in repo {repo_id}")
        logging.error(e)
    return branch_details.as_dict() if branch_details else None


def get_pr_details(pr_id: Union[str, int], summarize: bool) -> Union[Dict[str, Any], None]:
    """
    This function gets the pull request details from Azure DevOps, given a pull request ID.,
    or a Pull Request URL.
    :return:
    """
    pr_details = None
    pull_request_id = None
    if isinstance(pr_id, str):
        if re.match(r'^https://.*?/pullrequest/(\d+)$', pr_id):
            pull_request_id = re.match(r'^https://.*?/pullrequest/(\d+)$', pr_id).group(1)
        elif re.match(r'^vstfs.*$', pr_id):
            pull_request_id = re.split(r'%2F|/', pr_id)[-1]
        elif re.match(r'^\d+$', pr_id):
            pull_request_id = pr_id
    elif isinstance(pr_id, int):
        pull_request_id = str(pr_id)
    else:
        raise TypeError(f'pr_id must be a string or an integer, not {type(pr_id)}')
    if pull_request_id:
        if not git_client:
            # TODO: Get config and ADO name from context or parameter
            init('DEV', 'AnaChem')
        try:
            pr_details = git_client.get_pull_request_by_id(pull_request_id)
        except Exception as e:
            pr_details = None
            logging.error(f"Error getting PR details for PR {pull_request_id}")
            logging.exception(e)

        pr_details = pr_details.as_dict() if pr_details else None
        if pr_details:
            if summarize:
                pr_details['summary'] = _simplify_pr_details(pr_details)
    return pr_details


def get_git_commit_details(repo_id: str, commit_id: str, project_name=None):
    if not git_client:
        # TODO: Get config and ADO name from context or parameter
        init('DEV', 'AnaChem')
    if not project_name:
        project_name = this.home_ado_project
    try:
        commit_details = git_client.get_commit(commit_id, repo_id, project=project_name)
    except Exception as e:
        commit_details = None
        logging.error(f"Error getting commit details for {commit_id} in repo {repo_id}")
        logging.exception(e)
    return commit_details.as_dict() if commit_details else None


def get_build_details(build_id: Union[str, int], project_name=None):
    if not build_client:
        # TODO: Get config and ADO name from context or parameter
        init('DEV', 'AnaChem')
    if not project_name:
        project_name = this.home_ado_project
    try:
        build_details = build_client.get_build(build_id=build_id, project=project_name)
    except Exception as e:
        build_details = None
        logging.error(f"Error getting build details for Build {build_id} in project {project_name}")
        logging.exception(e)
    return build_details.as_dict() if build_details else None


def get_artifact_details(relation_url: str) -> Tuple[Union[Dict[str, Any], None], Union[Dict[str, Any], None]]:
    artifact_id = identify_artifact(relation_url)
    artifact_details = None
    if artifact_id:
        if artifact_id['artifact_type'] == 'commit':
            artifact_details = get_git_commit_details(artifact_id['repository_id'],
                                                      artifact_id['artifact_id'])
        elif artifact_id['artifact_type'] == 'branch':
            artifact_details = get_git_branch_attribs(artifact_id['repository_id'],
                                                      artifact_id['artifact_id'])
        elif artifact_id['artifact_type'] == 'pullrequest':
            artifact_details = get_pr_details(artifact_id['artifact_id'], summarize=True)
        elif artifact_id['artifact_type'] == 'build':
            artifact_details = get_build_details(artifact_id['artifact_id'])
        elif artifact_id['artifact_type'] == 'release_env':
            artifact_details = None
        else:
            logging.error(f"Unknown artifact type: {artifact_id['artifact_type']}")
        return artifact_id, artifact_details
    else:
        return None, None
