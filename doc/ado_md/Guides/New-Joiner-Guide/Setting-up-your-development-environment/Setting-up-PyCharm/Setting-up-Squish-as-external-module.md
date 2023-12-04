To be able to use the squishtest module from PyCharm, all you need to do is set up a couple of environment variables.

1. Open the Windows *Control Panel*
2. In the search field, type *env*
![01_Control_Panel_env.png](/.attachments/01_Control_Panel_env-49cb3e10-6278-4659-bea8-686c87709ca8.png)
3. Click *Edit environment variables for your account* or *Edit the system environment variables*. If you're the only one using this computer, there is basically no difference, you can use either one.
4. Press the *Environment Variables...* button
![02_System_properties_Environment_Variable_Button.png](/.attachments/02_System_properties_Environment_Variable_Button-08d15f83-62f6-4510-917c-af626ee45593.png)
5. Set/create the *SQUISH_DIR* variable.
5.1 In the *Environment Variables* dialog, check if you already have a variable named *SQUISH_DIR* and make sure that it's pointing to the directory where you installed Squish. 
5.2 If there isn't one, create it.
5.2.1 Press *New...*
![03_Environment_Variables_New_Button.png](/.attachments/03_Environment_Variables_New_Button-91433c48-fc9b-456b-be44-ebf426c56a77.png)
5.2.2 In the variable name enter *SQUISH_DIR*, in the variable value enter your Squish installation path.
![04_New_EnvVar_SQUISH_DIR.png](/.attachments/04_New_EnvVar_SQUISH_DIR-760d5e77-091a-4641-982e-69aeddc72710.png)
5.2.3 Press *OK* to close the dialog.
6. Set/create the *PYTHONPATH* variable
6.1 If you already have the variable - either as a system or a user variable - make sure that *%SQUISH_DIR%* and *%SQUISH_DIR%\bin* are added to it, preferably as the first two items.
![05B_Existing_PythonPath_List.png](/.attachments/05B_Existing_PythonPath_List-819a22f0-2137-49cf-a5ce-414340ff595e.png)
6.2 If you don't have *PYTHONPATH* set anywhere, then create a new one.
![05A_New_PythonPath_one_liner.png](/.attachments/05A_New_PythonPath_one_liner-58b52972-f3bd-4c7a-a5f6-2e61c7bcf66a.png)
Variable name: *PYTHONPATH*
Variable value: *%SQUISH_DIR%\bin;%SQUISH_DIR%\lib\python;%PYTHONPATH%*
7. Start/Restart PyCharm
8. Test it.
8.1 Create a new Python file (even a Python Scratch file should do)
8.2 Try to import the *squishtest* module


**Note for the squishtest module**: This module is not implemented in Python and PyCharm is not aware of its members, so code completion will not work.

**Note for environment variables**: You can also set the environment variables by NOT using other variable names at the time of creation, but still separating the items on it with a semicolon. This way you get the type of easy-to-use dialog that you saw in step 5.3.1.


For more (confusing) details: https://kb.froglogic.com/squish/howto/using-squish-module-python-scripts-applications/




