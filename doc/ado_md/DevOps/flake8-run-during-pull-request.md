[[_TOC_]]

---
## Flake8 run during a merge/pull request

To trigger a pipeline when a PR is opened, but before it is merged, would need to add a branch policy on master branch to have a build validation step. This will trigger the pipeline to run whenever a PR is opened to master.

To enable the pipeline trigger during a Pull request. Need to setup the [Build validation](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation).

**_Note_**: Considering the one who configure this has permission to create a build policy.
- Navigate to project settings -> Repositories.
- Select the appropriate repo from all repositories list.
- Then select the tab "Policies".
- In the "Branch Policies" section select the **Master** branch.
- Then follow the steps given in the documentation on [Build validation](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation)

Once we set the Build policy under Build validation on the Master branch. We all set for the pipeline triggers when a Pull Request is opened to the master.