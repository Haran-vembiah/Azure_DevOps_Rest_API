
[[_TOC_]] 
#Overview
---
The embedded software for the G5 instruments is available as a *simulator*, which is fundamentally the same code as you would find on the actual target hardware, but it is compiled for 64bit Windows, and comes with a few handy features that make the testers' lives easier.

The vast majority of tests is carried out on the simulator, so it's important to get familiar with the basic operations and settings.

---
#Download
---
##Official release (at the end of each iteration)

The official release at the end of each iteration is uploaded to the SharePoint and you will receive an email to notify you. The same email will also warn you that the release files are too large to be downloaded using File Explorer.
1. If you are working from home, connect to your favorite MT VPN
2. Open the link from the email in a browser.)
3. Click the *ellipsis* (...) next to the file name
4. Click the *ellipsis* in the context menu
5. Click Download
6. Repeat steps 3-5 for all 3 files: .7Zip, .exe and the Release Notes

![Download From SharePoint](/.attachments/01_01_Download_Sharepoint-769765af-c78a-4c69-ba3b-238a72cea44c.png)


##CI/CD build (any time during the active iteration)
In the current setup, every time the developers push their changes to a branch in the main G5 instrument Git repository (*mt-anachem-instrument*), a new build is created and the artifacts are made available in Azure DevOps. 

Unlike those of the official iteration releases, these artifacts are not uploaded to the SharePoint. However, they are still accessible to anyone who wants to take a peak at the half-baked features before they are released for testing.

Keep in mind, though, that any bugs or complaints based on such a build will be rejected and half of your reputation points will be deducted ;-).

1. No need for VPN connection, in fact it will just slow you down
2. Navigation panel (left) in Azure DevOps > Pipelines > Pipelines  

   ![Pipelines-Pipelines](/.attachments/01_02_Download_Azure_Artifacts-2addbbe4-e9e3-4953-be40-5ee13a04e66c.png)
3. On the **Recently run pipelines** page, click on the latest run of the *mt-anachem-instrument* pipeline  

   ![Pipelines-mt-anachem-instrument](/.attachments/01_03_Download_Azure_Artifacts_Pipeline-9313b10f-ae82-4883-a046-58162b284d94.png)
4. On the pipeline's page, the **Runs** tab lists all the available run results. Click on a successful one
(green disc with white checkmark icon)  

   ![Pipelines-Latest-Run](/.attachments/01_04_Download_Azure_Artifacts_Pipeline_Run-db237867-1ff5-48b6-8cb3-2c4d931cd0fc.png)
5. Counterintuitively, the artifacts aren't under the *Artifactory* tab. 
Click on the Job at the top of the list in the **Jobs** section 
 
   ![Pipelines-Latest-Run-Job](/.attachments/01_05_Download_Azure_Artifacts_Pipeline_Run_Job-9acd4e34-22af-4670-95f0-b7f1decc7c86.png)
6. The next page lists the tasks executed in the given job. 
The panel on the right shows the logs for the task on a black background. Click the link that reads *<u>1 artifact</u> produced*  

   ![1-artifact-produced](/.attachments/01_06_Download_Azure_Artifacts_Pipeline_Run_Job_Artifact_Link-50e2674b-d99e-4577-8ed1-772e59db7572.png)
7. On the **Artifacts** page, 
   1. expand the list of files
   2. Click the *ellipsis* (the three vertically aligned dots at the end of the row)
   3. Click *Download artifacts*  

      ![1-artifact-Download](/.attachments/01_07_Download_Azure_Artifacts_Pipeline_Run_Job_Artifact_Download-e0a937d5-9274-4415-94fb-ef19c81641eb.png)

---
#Installation
---
The G5 Terminal Simulator can be installed using the official installer or by simply extracting the 7Zip file to a convenient location. 

- The **installer** is more convenient, but it overwrites previous installations of the simulator.
- The **7Zip** file is not much more complicated than using the installer, but it has the added benefit of allowing you to keep multiple versions and even multiple installations of the same version at the same time. (This can be quite useful for comparing the behavior of the application between releases to find exactly when a specific issue occurred, or for *freezing* an installation for further investigation without having to suspend your testing activities.)

##Using the installer
There is really not much to it. 

1. Double-click the .exe file
2. If this is the first time you install the Simulator or you have uninstalled the previous version, the installer will ask you for the location. **Make sure that you select a location where you have write permissions without elevation** (i.e. you don't need Admin access to modify the directory)
If there is an existing version already installed on your computer, the installer will simply overwrite it without asking for the installation location

![02_01_01_Installer_Select_Location.png](/.attachments/02_01_01_Installer_Select_Location-e9d40802-1719-45db-bd6f-d5046ca8f1fb.png =600x)

3. Click *Install*  

![02_01_Installer_Step_1.png](/.attachments/02_01_Installer_Step_1-2d8eb6dc-1d15-43dd-9af5-7a8615a28867.png =600x)

4. Wait for the installer to finish

![02_02_Installer_Step_2.png](/.attachments/02_02_Installer_Step_2-debe6934-1803-4774-b629-8454a77ffbb6.png =600x)

5. Click *Finish*

![02_03_Installer_Step_3.png](/.attachments/02_03_Installer_Step_3-e19beb76-a6f2-4be1-850c-4ab25382a546.png =600x)


NOTE: The G5 Simulator's Start menu icon is not under the same folder as the rest of the Mettler Toledo simulators. It's in a folder named *Titration*

![02_04_Installer_Start_Menu_Entry.png](/.attachments/02_04_Installer_Start_Menu_Entry-3ba37150-a1da-4cdd-aa1d-359dc3e2198e.png)




##Installing from the 7Zip file

This option is even simpler than the installer. Just extract the 7Zip file and you're good to go.

1. Create a directory on your C: drive where you can keep all your simulator releases. I recommend the C: drive because the mapped network drive can cause some issues. (I use *C:\Users\<username>\Programs\Titrator*)
2. Extract the 7Zip file into your new directory
3. Repeat the same for any number of different versions, or instances of the same version.
4. If you're happy with launching the application from a directory, you're done.
5. An easy extra step is to launch the application and pin it to the taskbar.

### Multiple Simulator versions with Start Menu icons 
If you would like to start different version of the Simulator from the Start Menu, follow these steps:  

1. Right click the ti_terminal.exe in the directory where you extracted the 7Zip file and select  *Create shortcut* 

   ![03_02_01_Create_Shortcut.png](/.attachments/03_02_01_Create_Shortcut-d3996f32-9ee2-4faf-b2f1-d7ea4ae146c0.png)

2. Create a new directory in your C:\ProgramData\Microsoft\Windows\Start Menu\Programs\ directory, for example *G5 Titrator*
3. Copy the shortcut into your new Start menu directory
4. Rename the shortcut so that it includes the version

   ![03_02_02_Start_Menu_Shortcut_Directory.png](/.attachments/03_02_02_Start_Menu_Shortcut_Directory-e0f052fe-a447-49fd-8353-91ec0eee279b.png)

5. The shortcut will be in the directory you created under the Start menu:

   ![03_08_Start_Menu_Custom_G5_Titrator.png](/.attachments/03_08_Start_Menu_Custom_G5_Titrator-e7798645-b6de-4911-981e-d7e7146bec7f.png)


---
#Settings
---
##Overview
When you need the Simulator to run with settings other than the default, you have a number of ways to go, depending on what you need to change in the application's behavior. 

1. Use the command line options to set the 
    1. Instrument type
    1. Serial number
    1. LabX connectivity
    1. Technical settings (see the [Command line options](#command-line-options) chapter for details)
1. Use the configuration files to modify
    1. Low-level technical settings (see the [Configuration files](#configuration-files) chapter for details)
    1. Logging
    1. Simulated services/devices
    1. Instrument type-specific settings (e.g. titration-related parameters)
1. Use the '*init_*' files to modify the default data available in the application, such as
    1. Methods and templates loaded/created at startup
    1. Default users and user groups
    1. Automatic setup of devices/accessories
    1. Default system settings loaded at startup
    1. See the [Settings Database](#settings-database) chapter for details and more settings

If you are looking for a particular (often used) setting or constellation (but not a celestial one), then try your luck on the HowTos page. 


##Command line options
###General information
The settings that are considered more likely to change with each run of the simulator can be modified using command line options. 

To use them, you will have to start the application from the command line of course.

1. Open a Command Line terminal
    1. Open the start menu
    1. Search for *cmd*
2. Change directory (cd) to where your *ti_terminal.exe* is 
3. Start the application from the command line with the options you need 

    ```dos
    C:\SIM_INSTALL_PATH>ti_terminal.exe -t UV5Nano
    ```
 
If you find yourself using the same settings with each run, you can simply modify the shortcut (either the one in the Start menu, or the desktop shortcut, if you have one) and add the options to the *Target* property:

![01_CLI_Shortcut_Target.png](/.attachments/01_CLI_Shortcut_Target-d9ec8834-a2c3-4d7e-a3fe-1071337bb10d.png =500x)

If you find that some of the options don’t work the way it's described here, then please update this page. If you have access to the G5 Instrument Git repository, look for this file: *mt-anachem-instrument/source/tfw-app/src/startup/appparameters.cpp* to figure out how the command line options work.

###List of options

The below list of options is basically a formatted version of what you may find in *appparameters.cpp*, with some explanations, where it was warranted.

> **NOTE: The options [-n, -s, -t, -FR, -l, -u, -dbCreate] are only available in the Simulator**


| Switch | Argument| Description |
|--|--|--|
| -n | <serial_number> | eg. "-n S123456" : Set the serial number for this run (NOT saved to the database). "B123123123" is the default. |
| -s | <serial_number> |  eg. "-s S123456" : Identical to -n plus the characters must be valid and printable ascii characters. |
| -t | <type> | eg. "-t UV5Nano" : Set instrument type. Note that the database is re-created if the instrument type has changed! Also, if you pass an invalid value, nothing will happen, you don't get a warning, it will be just ignored. (So good luck figuring out what went wrong in your tests.)|
| -FR |  | Do a 'factory reset': re-create the database with the current or newly set instrument type and then start up. |
| -l | <URL> | Connect to LabX identified by the URL. <br><br> This one is a bit more complicated than whatever fits in a table cell. See the [section on Connecting to LabX](#using-the-command-line). |
| -u |  | Use a 'unique' sub-path ("snr_<serial_number>") for database, logs, results, harddisc, eeprom_*.dat and resources/config/*.* <br><br> Chances are, you will **not** use this one **on its own**, but it can be **super useful** in combination **with other settings**, so you can run the Simulator in some configuration using a specific serial number, and still keep the default or other configurations, each associated with their own unique serial numbers. |
| -dbCreate |  | Just create the database and exit. This can be combined with -t option. |
| -sim | interface:port | Listen on given interface:port, on of the network interfaces, 127.0.0.1 or loopback for loopback or 0.0.0.0 for any interface. <br><br> This one is really more for test automation. In a nutshell: the instrument has a a gRPC interface for simulating certain events programmatically, from test automation scripts.|
|-qmljsdebugger||Not for mortals. Presumably some help with debugging JavaScript in QML files.|
|-inst| interface:port | Similarly to the *-sim* option, this one sets the connection details of a gRPC interface. The difference is, this one is for the communication between the instrument (the box) and the terminal (the screen). Currently this interface can only handle one connection at a time, which is used by the terminal, so there isn't much you can do with it in testing.|

For an  up-to-date list of these options, check the *appparameters.cpp* file in the G5 Instrument Git repository. 
(Currently under /dep/tfw/source/app/src/startup)

##Configuration files
###Overview
###Simulation
###WebUI
The simulator has a web interface where the user (tester) can set the log levels.

It is disabled by default, but enabling it is quite simple. 

1. Open the resources/config directory in the Simulator's install directory
2. Rename the _webui.xml file to webui.xml (i.e. remove the underscore)
3. Edit the *port* in the webui.xml file in a text editor (or XML editor if you have one)
    1. If you're unsure which port to use, you can check the available ports on your host machine with the *netstat* command
    2. Set the port number to some value that won't interfere with other services running on the host. Default value is 80, so if you have a web server running, this is probably not your best choice.
###DB Initialization


##Settings Database


#Use cases
##Connecting to LabX

Note: all of the below settings depend on the configuration of LabX and the landing service, so if you are not running those yourself, or don't have control over them, then your first step should be finding out their settings.

###Using the command line
Starting the Simulator from the command line allows you to set certain configuration values right at the startup. (See the [section on Command Line Options](#command-line-options) for more details)

To set the LabX connection details from the command line, you can use the **-l** switch and pass a URL in one of the below formats.

####DNS Service lookup
This option is the gambler's choice.

If you start the Simulator with the **-l dns://service** option, it will perform a DNS lookup for the specified service. 

When an application asks a DNS server to find the hosts running a particular service, the server returns a list of DNS SRV records with the connection details of each host that matches the criteria. The order in which these records are returned are set by *preference* settings on the particular DNS server(s), so there is no guarantee where the application might end up connecting to. If you have 3 hosts running LabX on the same domain, or the same host is running any number of LabX instances (if that's possible), it will be hard to tell which one will be *the one*. 

That's (probably one of the reasons) why this option isn't used for specifying a direct connection, but the URL of the [*landing service*](#labx-landing-service)

This option is a bit of a gamble in yet another way. DNS SRV records don't magically appear on DNS servers. It's not *taken care of by the network*. The application - in this case LabX - has to broadcast its information and the DNS server has to be perceptive to it (i.e. it shouldn't just throw it away) or the network administrators have to create the records manually. 
The records can also vanish over time. Some DNS servers like to keep their records up-to-date through funnily named processes like *scavenging*, so a service that was found today, might not be there in a week if it was unavailable when the DNS server was maintaining its records.

What this means is that you can't just fire up LabX randomly for a test and expect this option to work.

But the option is there, so how to use it? 
Let's see the URL structure:

| Part | Description |
|--|--|
| dns:// | The first part of a URL is basically the protocol. (Although it's actually called a [*scheme* and it isn't necessarily a protocol.](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml))  In this case it's DNS, because that's the system the application will use to find the service.|
| service | This is the trickier part. In the real world (outside of MT) a service identifier in a DNS SRV record would include the protocol and the domain. At this point, we can only assume that the Simulator expects the the same format. <br><br>Based on that assumption, the *service* part might look something like this: *_labx._http.eu.mt.mtnet*, where <br><br>  *_labx* is the service name, unless that changed in the meantime. It's certainly not [registered with IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), so nobody could stop the developers from using *smorgasbord* as the service name from Tuesday on. <br><br> *_http* is the protocol used by the landing service, the one the application is trying to find. <br><br>*eu.mt.mtnet* is the domain where the service should be running, and where the DNS server should try to find it. You would need to adjust the domain to your location of course. Ideally, you should be on the same domain as the LabX server.|

####Landing service with known host name and port
If you know where the LabX landing service is listening, use the **-l http: //host[:port]** option.
| Part | Description |
|--|--|
| http:// | The first part of a URL is basically the protocol. (Although it's actually called a [*scheme* and it isn't necessarily a protocol.](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml))  In this case it's http, that's what the landing service is (supposed to be) using. |
| host | The host name where the landing service is listening. |
| port | The port where the landing service is listening. It's in square brackets because it's optional to pass it in the command line. If it's not specified by the user, the default value, 8080 will be used.|

####Direct connection using gRPC
The previous two options instructed the Simulator to try and connect to the Landing Service. The actual communication channel between LabX and the instrument is using gRPC and this option is the one to use if you want to skip the whole back-and-forth with the landing service. (The details of how gRPC works are outside the scope of this manual.)

The syntax of the option **-l grpc://host:port**

| Part | Description |
|--|--|
| grpc:// | The first part of a URL is usually the protocol. (Although it's actually called a [*scheme* and it isn't necessarily a protocol.](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml))  In this case it's *grpc* (so NOT a protocol), because that's the type of communication channel we want the Simulator to build with LabX. |
| host | The host name where LabX is running |
| port | The port where LabX is listening for gRPC connections. |













