
[[_TOC_]]

---
# ADO Publish code as wiki setup Guide

You can publish content that you already maintain in a Git repo to a wiki.

---
## **Why Publish code as wiki**
- Organize the content into a hierarchical page structure
- Table of contents that readers can browse and filter
- Publish new versions of the content
- Manage content in the same way you manage your code base
- Readers can search the wiki easily using the wiki search feature


---
## Publish code as wiki setup

- When you set up Publish repo to wiki for the first time, refer the Azure documentation [Publish code to wiki](https://learn.microsoft.com/en-us/azure/devops/project/wiki/publish-repo-to-wiki?view=azure-devops&tabs=browser) for Prerequisites and initial setup.
- Publish a Git repository to a wiki(Code-to-a-wiki), when there is no project wiki available and also code wiki available for the project.
  - Sign in to organization e.g. AnaChem (https://dev.azure.com/AnaChem), open project e.g. AnaChemProjects, and then select Overview > Wiki.

    ![Navigate_wiki.png](/.attachments/Navigate_wiki-1d7f33ab-9f65-4aed-98d0-cb102896a3e7.png)

  - Select Publish code as wiki. 

    ![Select_publish_code_as_wiki.png](/.attachments/Select_publish_code_as_wiki-02c35f25-d1c3-4e59-bf75-2cb3809659e9.png)

- If you've already provisioned a team project wiki and now want to setp up code as wiki.
  - Navigate to Wiki and Select the "list of wikis" dropdown.
  - select Publish code as wiki.

    ![Create_code_as_wiki.png](/.attachments/Create_code_as_wiki-295072e1-2073-40ae-a97a-22e26461da8e.png)

- Setup "Publish code as wiki" for the new repo(e.g "mt-anachem-ta") In the configuration page as follows:

  - Select the repository (e.g "mt-anachem-ta") in the Repository field.
  - Select the branch(master by default) from which you you want to publish code as wiki in the Branch field.
  - Select the folder(where MD files are available) to publish code as wiki in the Folder field. Specify the root of the repo when you want to publish all Markdown files in the repo to your wiki.
  - Enter name of the wiki (e.g. "G5 Test Automation Wiki") in the Wiki name field
  - Then Click on button "Publish".

    ![new_repo_setup.png](/.attachments/new_repo_setup-c6296d4e-81a5-486c-b332-1a13f616d16b.png)

- The wiki repo populates with the Markdown files and folders included within the repo you selected. 

---
## File naming conventions:
- If you are using spaces in the page title, use hyphens instead of spaces. So that the wiki page title will appear with spaces when published as wiki.
  
   e.g. If the page title specified as How-to-contribute.md. it will be displayed as "How to contribute"
- For other restrictions refer [File naming conventions](https://learn.microsoft.com/en-us/azure/devops/project/wiki/wiki-file-structure?view=azure-devops#file-naming-conventions) on Azure documentation.

---
## Setup to remap the repository(e.g. from "mt-anachem-systemtests-framework" to "mt-anachem-ta") to Publish code as wiki - code wiki (Example: "G5 Test Automation Wiki")

Follow below steps to remap a different repository for publish code for an existing wiki.

**_Note_**: Below steps are considered with the assumption project wiki is available already.

### Unpublish the old repository
- Navigate to Overview -> Wiki from Project Home screen.
- Select the desired code wiki (Example: "G5 Test Automation Wiki") from the list of wikis available for the project.
 
  ![Select_existing_code_wiki.png](/.attachments/Select_existing_code_wiki-9b8358b7-b5b2-4a42-9292-3963a1c389de.png)

- When no longer want a repository to be published as a wiki, first we should unpublish it from Wiki.
- Click on "More actions" button and then select the option "Unpublish wiki".

  ![Unpublish_existing_wiki.png](/.attachments/Unpublish_existing_wiki-8d6875ae-52bc-4529-aa36-9b927d6b5a7a.png)


- Then confirm the unpublish process by pressing the button "Unpublish" on confirmation screen.
- Check the Repository name once to make sure that is the one from which you want to unpublish the wiki. 

  ![Unpublish_wiki.png](/.attachments/Unpublish_wiki-9c6d264d-92f7-4764-aa00-af1dfafb276f.png)


### Map a new repository to wiki
- To map another repository "mt-anachem-ta" to publish code as wiki on wiki "G5 Test Automation Wiki" .
- Select the "list of wikis" dropdown and the select the option "Publish code as wiki".

  ![Select_publish_code_as_wiki.png](/.attachments/Select_publish_code_as_wiki-b9381f61-0697-4b18-a8e2-1a231207b69e.png)


- Setup "Publish code as wiki" for the new repo(e.g "mt-anachem-ta") In the configuration page as follows:
  - Select the repository (e.g "mt-anachem-ta") in the Repository field.
  - Select the branch(master by default) from which you you want to publish code as wiki in the Branch field.
  - Select the folder(where MD files are available) to publish code as wiki in the Folder field.
  - Enter name of the wiki (e.g. "G5 Test Automation Wiki") in the Wiki name field
  - Then Click on button "Publish". 

    ![new_repo_setup.png](/.attachments/new_repo_setup-c6296d4e-81a5-486c-b332-1a13f616d16b.png)


- Once we publish code as wiki, recently Published code wiki (e.g. "G5 Test Automation Wiki") available in the list of wikis(project-> Overview -> Wiki)
- Then select the wiki (e.g. "G5 Test Automation Wiki") from the list.
- The wiki repo populates with the Markdown files and folders included within the repo you selected.

- To verify that recently published wiki (e.g. "G5 Test Automation Wiki") mapped with the repository (e.g "mt-anachem-ta") by trying to publish new branch.
  - Select the branch dropdown and then select the option "Publish new branch".

   ![Publish_new_branch.png](/.attachments/Publish_new_branch-cb45d262-9f9a-4906-af68-32b12085aad9.png)

- Make sure that repository(e.g "mt-anachem-ta") set in the Repository field.

   ![new_repo_mapped.png](/.attachments/new_repo_mapped-7ea50582-7f5e-4815-9623-a6727eb71b76.png)
---
## .order file
- The default hierarchy is in alphabetical sequence 
- The .order file defines the sequence of pages within the wiki.

## Change the page sequence, add, or update an .order file
- Each .order file defines the sequence of pages contained within a folder.
- The root .order file specifies the sequence of pages defined at the root level.
- For each folder, an .order file defines the sequence of subpages added to a parent page.
  - You can add an .order file in the same way that you add any file from the Code > Files page. Name the file .order.
  - Each entry should mirror the file name but without the .md file type.
  - Titles are case-sensitive, so the entry should match the case used in the file name.
- The below snapshot shows how the pages are sequenced in the .order file and published in the wiki.

  ![order_of_pages.png](/.attachments/order_of_pages-59d2592b-25ce-45b7-9d3f-74c34fce221e.png)

- If you want to display wiki pages in alphabetical sequence, delete the .order file.



## Reorder a wiki page
- You can reorder pages within the wiki tree view to have pages appear in the order and hierarchy you want.
- You can drag-and-drop a page title in the tree view to do the following operations:
  - Change the parent-child relationship of a page.
  - Change the order of the page within the hierarchy.

**_Note_** : Moving a page in the hierarchy may break links to it from other pages. You can always fix the links manually after you move. Reordering a page within a hierarchy has no impact on page links.

---

Now you can publish your desired version of code\MD files to wiki from the repository ("mt-anachem-ta")
