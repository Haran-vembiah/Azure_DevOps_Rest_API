
## Get the code - clone the repository
The code - even for the test automation scripts - is under version control. We store the framework and the scripts in two separate Git repos:
- mt-anachem-titrator-systemtests : This is where the test scripts are stored
- mt-anachem-systemtests-framework: The Test Automation Framework code repository

If you're going to work on both of the codebases at some point, you'll just have to repeat this process for the missing one.
For now, just focus on _mt-anachem-titrator-systemtests_.



1. Go to the Orion project's Azure DevOps (a.k.a. TFS) space and choose _Repos from the left sidebar_
![Step_1_Repos.png](/.attachments/Step_1_Repos-bd66a08c-2687-41c5-a244-8895991d57a5.png)
1. On the _Repos_ page, select the _mt-anachem-titrator-systemtests_ repo on the top of the page.
![Step_2_Select_Repo_From_List.png](/.attachments/Step_2_Select_Repo_From_List-9b7c5a0b-ce24-4cab-8eb3-6d4ebfb90c06.png)
1. On the right side of the page, click the ![Clone.png](/.attachments/Step_3.1_Clone_Link-c08d8c27-1ccb-4f9f-b517-d63b67c25e31.png) button to bring up the pop-up menu.
1. Click the ![Copy](/.attachments/Step_3.1_Clone_Link_Copy_Button-720c02dd-fee5-425a-942d-21f41eb302d1.png) button to copy the link to the clipboard
![Step_3_Clone_Link.png](/.attachments/Step_3_Clone_Link-70ccbd20-8f13-41c2-9472-8f634bcce526.png)
1. Open PyCharm and navigate to _VCS > Checkout from Version Control > Git_
![Step_4_PyCharm_VCS_Git_Menu.png](/.attachments/Step_4_PyCharm_VCS_Git_Menu-5f593210-e9d7-455d-9d2e-aacb78dabab8.png)
1. In the _Clone Repository_ dialog, paste the URL in the _URL_ field, select a local folder for your project, then click _Test_ to see if everything is fine.
![Step_4_PyCharm_VCS_Git_Clone_Dialog.png](/.attachments/Step_4_PyCharm_VCS_Git_Clone_Dialog-2c36e8b1-fa22-40f5-b806-4cdd2a32e736.png)
1. Click _Clone_ and the repository will be copied to the directory you chose and you should see it in the _Project_ tool window.
![Step_6_Done.png](/.attachments/Step_6_Done-054f3b82-202b-487d-8538-09e7d0ce8e70.png)


----

## Configure the Python interpreter
Python packages can have several versions with various dependencies which often collide. To avoid these collisions and to maintain a stable Python environment, we are using virtual environments. PyCharm provides full support for Python Virtual Environments, and setting them up is easy.

1. Open PyCharm and select _File > Settings_
![Step_1_Settings_Menu.png](/.attachments/Step_1_Settings_Menu-5f067f09-5025-4b97-b971-5c1e8e3dac07.png)
1. In the _Settings_ dialogue's sidebar, select _Project: project_name_ > _Project interpreter_
![Step_2_Settings_Project_Interpreter.png](/.attachments/Step_2_Settings_Project_Interpreter-18b7d5ce-e887-4d76-9e4b-805c3537a4eb.png)
1. Click on the cogwheel icon next to the _Project interpreter_ dropdown list
(The list might already show an interpreter, but don't worry about it.)
![Step_3_Add_Interpreter_Menu.png](/.attachments/Step_3_Add_Interpreter_Menu-cdb21bf8-96e3-428e-9b63-2b482d4ec10c.png)
1. In the _Add Python Interpreter_ dialogue, click on the folder icon next to the _Location_ dropdown list
![Step_4_Virtual_Environment_Location_Button.png](/.attachments/Step_4_Virtual_Environment_Location_Button-43a6ab3b-9f60-46f3-9ab4-4df901805c03.png)
1. Select a folder to store your new virtual environment. It is better to keep the environments separate from the project hierarchy. Best is to create a new folder to keep all your virtual environments.
![Step_5_Virtual_Environment_Location_New_Folder.png](/.attachments/Step_5_Virtual_Environment_Location_New_Folder-501eca03-ba81-407e-90c5-dbe6ee7da7b5.png)
1. Click OK and your new location should be set.
![Step_6_Virtual_Environment_Location_Done.png](/.attachments/Step_6_Virtual_Environment_Location_Done-7f36158f-ff0e-46c1-b732-9f2e5ad3d56c.png)
1. Now select a Python interpreter. For this project, we use version 3.7.x, 32-bit interpreters.
![Step_7_Select_Python_Interpreter_Browse.png](/.attachments/Step_7_Select_Python_Interpreter_Browse-4a74cfcb-b118-4b14-ba46-bc35a83e443e.png)
1. Make sure that the _Make available to all projects_ checkbox is selected.
![Step_8_Available_For_All_Projects.png](/.attachments/Step_8_Available_For_All_Projects-a8e9edc4-580b-4f28-8fad-509bccd7013d.png)
1. Click OK, and PyCharm will show you a progress bar as the virtual environment is being created.
![Step_9_Creating_Env_Pop_Up.png](/.attachments/Step_9_Creating_Env_Pop_Up-fdbcef71-41b7-4886-b166-701bce1f910f.png)
1. Done. You have your new environment with the minimal packages installed.
![Step_10_Done_Results.png](/.attachments/Step_10_Done_Results-0f067453-2c6d-4102-87e3-a552e75b6ce3.png)


