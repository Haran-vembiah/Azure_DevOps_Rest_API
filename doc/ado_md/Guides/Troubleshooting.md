If something went wrong, it's likely that you're not the first to come across the problem. Here's a collection of some common problems and the steps to solve them.

[[_TOC_]]



### Missing packages - import errors
----
If you open any of the Python source files, you might see that some import statements triggered errors. That is probably because those packages have not been installed in the virtual environment at this point.
![Step_10_Missing_Modules.png](/.attachments/Step_10_Missing_Modules-9bb1648e-ef3e-45ea-8d65-75493ba33c26.png)

#### Solution in PyCharm
1. To get a list of missing packages, you can run pylint. _Tools > External Tools > pylint_
(In case you missed the step where we set up pylint in PyCharm, here's a link: )
![Step_12_Pylint_Menu.png](/.attachments/Step_12_Pylint_Menu-a3ace11c-f62a-4099-8a22-ddc48b78ca43.png)
1. The results will look a bit messy, but what you're looking for are the error codes **E0401** and **C0114**
![Step_13_Pylint_Results.png](/.attachments/Step_13_Pylint_Results-bb149d80-0526-4232-96da-6015987ebcd7.png)
1. Copy this list into a text editor, and for each missing module or failed import, repeat the following steps for each failed import.

##### Install package in PyCharm Virtual Environment

1. _File > Settings_
1. In the _Settings_ dialogue's sidebar, select _Project: project_name > Project interpreter_
![Step_2_Settings_Project_Interpreter.png](/.attachments/Step_2_Settings_Project_Interpreter-998f2dd2-3f0b-4c90-839c-09fbc0724009.png)
1. Click the _Install_ button on the left side of the window
![Step_3_Install_Button.png](/.attachments/Step_3_Install_Button-6fca15bd-ccff-40a7-b302-6ff3822a787a.png)
1. Search for the package name
1. Select the most suitable one from the list
1. Click _Install Package_
![Step_3_Install_Steps.png](/.attachments/Step_3_Install_Steps-75dd4749-6ad9-41db-aa5a-caa74e0a3a79.png)

----