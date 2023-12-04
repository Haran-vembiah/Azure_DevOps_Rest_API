The input data, reference data and test results are all stored in a single PostgreSQL database. 
To access it, you'll need a client application.

Database clients are a matter of personal preference, so feel free to make your own choice.
If you're undecided, you'll find three guides to three different DB clients on this page.

[[_TOC_]]



# Connecting with DBeaver
## Download and install
1. Download the community version from here: https://dbeaver.io/download/
Note that the download may take a long time. At first it might even report several thousand days. If that happens, just leave it to do its thing, it will download within a reasonable time.
2. Installation is the usual Windows Installer process '_Next > Next > Finish_'

## Configure the JDBC driver
1. Download the proper JDBC driver from the PostgreSQL website https://jdbc.postgresql.org/download.html 
1. Copy the downloaded JAR file to the _C:\...\DBeaver\drivers_ folder
1. Start DBeaver
1. Open the Driver Manager (Database>Driver Manager)
![DriverManagerMenu.png](/.attachments/DriverManagerMenu-ec5558a7-4f56-4225-83b5-fce548bc73c1.png)
1. Click _New_ to create a new driver
![Click_New.png](/.attachments/Click_New-6aef8358-f591-4d06-9fa4-8891a6abb954.png)
1. Fill the driver settings
![Create_New_Driver.png](/.attachments/Create_New_Driver-916797f6-0103-41c4-aeee-d30fcb432e1d.png)


## Create a new connection
1. On the _Database Navigator_ pane, click the _New Database Connection_ button
1. Select the driver you just created
![Add_New_Connection.png](/.attachments/Add_New_Connection-a6e1b6a7-9fdb-4585-bc33-d3bbb65ff0b9.png)
1. Fill the connection settings
![Connection_Settings.png](/.attachments/Connection_Settings-d7bdf823-3b93-47c6-9c0c-6177c2fa7117.png)
1. Test the connection
![Test_Connection.png](/.attachments/Test_Connection-e3ba7029-49f7-4deb-806f-5b34b59468de.png)
1. Click _Finish_

----

# Connecting with SQuirrel
## Download and install
## Configure the JDBC driver
1. Download the proper JDBC driver from the PostgreSQL website https://jdbc.postgresql.org/download.html 
1. Start SQuirrel
1. Select the _Drivers_ side pane
![Drivers_Pane.png](/.attachments/Drivers_Pane-b9ddc5e7-454f-429a-a19c-1d9b12b387f4.png)
1. Select PostgreSQL from the list (double click)
![new_postgre_driver.png](/.attachments/new_postgre_driver-d755168a-2b3c-4cc8-8630-8d36cc69948d.png)
5. In the dialogue window
5.1 Select the _Extra Class Path_ tab
5.2 Click _Add_ 
5.3 Select the JAR file you downloaded from the PostgreSQL website
![Add_JAR.png](/.attachments/Add_JAR-1716e7b0-2675-4a3c-9969-e021d6fda2d9.png)
5.4 Click _List Drivers_
5.5 Select the available driver from the dropdown list
![list_drivers.png](/.attachments/list_drivers-57bf81e5-6a58-4f6c-8092-e3232f8106bf.png)
5.6 Click _OK_


## Create a new connection
1. Select the _Aliases_ side pane
1. Click the _Create New Alias_ button (blue plus sign)
![New_Alias_button.png](/.attachments/New_Alias_button-7d8aae70-d9bc-4868-b7c5-7710e8f0a816.png)
1. In the dialogue window
3.1 Select the PostgreSQL driver
![select_driver.png](/.attachments/select_driver-8858d214-5f88-4534-9ec2-1fa30d8ce7fb.png)
3.2 Enter the URL
For a local DB something like this would work: jdbc:postgresql://localhost:5432/mydatabase
3.3 Enter username and password
![add_alias.png](/.attachments/add_alias-8f623fe4-fac5-4e71-8fc1-23a1a7a87f97.png)
3.4 Test the connection
3.5 Click _OK_



----

# Connecting from PyCharm
## Community
### Install the plugin

PyCharm Community edition doesn't include a database connection manager, but there is a plugin similar to the one bundled with the professional version.
1. Open File>Settings (Ctrl+Alt+S)
![File>Settings](/.attachments/File_Settings-e49b68e8-be4c-4489-bdf4-f14b3eea3dec.png)
1. Search for the Database Browser plugin
2.1 Select _Plugins_ from the side panel
2.2 Select _Marketplace_ at the top of the window
2.3 Type 'database' in the search field
1. Click _Install_
![Plugin_Database_Navigator_Install.png](/.attachments/Plugin_Database_Navigator_Install-aa9b07b7-1e64-4088-969a-58794cf51580.png)
1. Restart the IDE before trying to use the DB Browser
![Plugin_Database_Navigator_Restart_IDE.png](/.attachments/Plugin_Database_Navigator_Restart_IDE-1b99e2bc-5a32-4bde-8989-735324035d1f.png)

### Configure the connection
1. Open the _DB Browser_ Tool window (View>Tool Windows>DB Browser)
     ![View>Tool Windows>DB Browser](/.attachments/Plugin_Database_Navigator_Tool_Window_Menu-d7583c14-dfb9-4999-aae5-860450099188.png)
1. In the tool window, click the New Connection (green plus sign) button and select PostgreSQL from the list
![Create New Connection](/.attachments/Create_New_Connection-cdcba487-37f7-47fd-a2ab-8ff9bf103fa1.png)
1. Name the connection and fill the details
Make sure to choose the **Built-in library** as the _Driver source_.
(Please try to avoid connecting to the live database from your IDE.)
![Connection Details Dialogue](/.attachments/Connection_Details_Dialogue_DEV_DB-4d573a13-b9c0-4c68-bfc6-4d0d3cd88480.png)
1. Test the connection with the _Test Connection_ button
![Test Connection Successful PopUp](/.attachments/Test_Connection_Successful_PopUp-3642fd76-74e5-454e-8e4e-a441ed1ef6b5.png)
1. Click _Apply_, then _OK_, and you're done
![New PostgreSQL DB connection](/.attachments/Ready_Connection-5b2f2392-286e-4197-82a7-4bfdef651838.png)


----
## Professional
### Enable the plugin
By default, the Database Tools plugin (based on DataGrip) is enabled, but if it isn't, or you just want to make sure, here's how to do it.
1. Open File>Settings (Ctrl+Alt+S)
1. Search for the Database Browser plugin
2.1 Select _Plugins_ from the side panel
2.2 Select _Installed_ on the top of the window
2.3 Type 'database' in the search field
![Database_Tools_Enabled.png](/.attachments/Database_Tools_Enabled-0d9b05f7-7e31-484a-b5e3-f6f935d7128e.png)

### Configure the connection
1. Open the _Database_ Tool window (View>Tool Windows>Database)
![View>Tool Windows>Database](/.attachments/File_View_Tool_Windows-177fd3b1-c362-4b09-be0f-080e6957ec81.png)
1. In the DB tool window, click the New (blue-ish plus sign) button and select Data Source > PostgreSQL from the list
![Create New Connection](/.attachments/Create_New_Connection-2c8f507d-c86c-402b-ba5f-3e2a2ee1efde.png)
1. Name the connection and fill the details
(Please try to avoid connecting to the live database from your IDE.)
![Connection Details](/.attachments/Connection_Details-c7fbda7e-2c26-4692-aa55-4ac802cb6f4a.png)
1. Test the connection with the _Test Connection_ button
![Test Connection](/.attachments/Test_Connection-0919dc7f-7785-4619-b62e-0e554bde42af.png)
1. Click _Apply_, then _OK_, and you're done
![Ready DB](/.attachments/Ready_DB-448f96f9-05b0-4c53-b8e2-14f091627739.png)

























