[[_TOC_]]

# Foundations

## Clean Server

### Disks

**DO**: Order an additional disk from IT and have them install it, then create two partitions on it; one for the DB backup files, one for all other backups.  
**WHY**:
It's a good idea to have an additional disk in the test server, because the database can generate quite big files, the logs can grow out of control if debug mode is overused, the installed SUT instances take up a lot of space and then you still have to store the generated reports somewhere.
Even if you don't run out of space, the system might need a fresh install every now and then, and it's better to keep the test data away from the system files on a separate disk, that can be removed conveniently before attempting to reinstall the system.  
The partitioning helps with keeping the backup processes running smoothly. 

### Peripherals

**DO**: Attach a monitor or a display emulator to the server or PC.  
**WHY**:
Unlike *Selenium* and other test automation tools designed for browser-based testing, *Squish for Qt* cannot run in so-called headless mode. That means that it needs a display where the SUT can be... well, displayed :-).  
Sometimes it is not feasible to attach actual hardware displays to the device where the tests are executed, but you can use *display emulators* instead. These are available online for $20-$50 and most of them don't require any kind of drivers or special configuration. 

**DO**: Attach a mouse and keyboard to the server or PC (temporarily)  
**WHY**:
You'll need to enable remote desktop connections while you are logged in directly.
You can remove these peripherals once the remote desktop is set up and tested.  
**Why is it even a question?**
Because you don't actually need peripherals - including displays - if remote desktop is already enabled on the host, and your user is whitelisted for remote desktop connections.  
With a clean, newly installed machine, this is rarely the case though, unless you arranged it with your IT department.

## Local Admin User

Installing SW and modifying the configuration on the Test Server requires Local Administrator rights. Here's how you can set it up.

### Long-term options

🧨Important to know before you jump in: you can't use your regular MT user account as a local administrator long-term! It is an acceptable solution for a day, but MT IT services enforce their policy by removing the non-administrative accounts from the administrator groups periodically (probably overnight), leaving only the "A-accounts", i.e. the administrative accounts whose username follows the `a-<regular_username>` pattern, and the accounts with general security exceptions.
To make sure that you have long-term administrator access to the host, you can go with either of these options:
1. Get an "A-account"
	1. If you already have one, make sure that it's working, meaning that it's not locked or expired, and you remember the password. 
	2. If you don't have one, request one in SNOW:  *Service Catalog>IT Services>Messaging / AD services>Administrative Domain User Service*
2. Get a security exception for your regular MT account
	1. You can create a request in SNOW, please see their *Knowledge Base* for details: [Local Admin Exception Workflow](https://mt.service-now.com/sp?id=kb_article_view&sysparm_article=KB0001767&sys_kb_id=c9e619e81b17e0d0b33da64bab4bcbb5&spa=1) .   
	   👍 This option might be preferable for you, because your regular account is most likely already included in Azure DevOps groups with the permissions you need, and you can create a Personal Access Token for it without any fuss. This can make things easier when you need to register and install a new self-hosted Azure Agent.

### Weekly Local Admin Password

🎁 Until you get the user permissions sorted out, you can continue with a Weekly Local Admin Password. In fact, if you can finish the setup within a week and you don't have to log in to the test server to make changes, you might not even need a local admin, because the day-to-day operation does not require any elevated privileges, since the Azure agent runs as a system user, and the processes started by it inherit its permissions.

1. Request a weekly admin password via [SNOW](https://mt.service-now.com/sp?id=sc_cat_item&sys_id=ac0a612ddba350d0e4580688f496196a&sysparm_category=)  
   ![Weekly_Local_Admin_Password.png](/.attachments/Weekly_Local_Admin_Password.png)
2. Log in as the weekly admin user
3. Add your user(s) to the *Administrator* local group
	1. Right click on the Start menu
	2. Select *Computer Management*
	3. Open the *Groups* folder under *Local Users and Groups* in the side panel 
	4. Right click the *Administrators* group and select *Add to Group...*
	5. In the next dialog, click *Add...* (You don't have to select any of the listed groups or users)
	6. At this point, the system will probably prompt you to enter a network user's credentials. You can enter your regular username and password. (This network user does not have to be an administrator, it just needs to be known to the network, because the weekly local admin us a local user only.)
	7. In the *Select Users, Computers, Service Accounts, or Groups* dialog enter the username you want to add to the *Administrators* group, then click *Check Names*
	8. If the user exists, the email address will be added next to the username. Click OK.
	9. Repeat for the rest of the users you want to add to the *Administrators* group
	10. In the *Administrators Properties* dialog click *Apply*, then click *OK*


From now on you can log in and do administrator-stuff with the users you just added to the *Administrators* local group.

## Power settings

The default power settings of Windows 10 are geared towards energy saving, but if you use your machine as the test server, it needs to be available all the time.

The simplest power configuration for 24/7 availability is not allowing the machine to turn off ever:

1. Log in to the test server as local admin
2. From the *Start* menu select *Settings* (the little gear icon)
3. In the *Windows Settings* window select *System*
4. From the left sidebar select *Power & sleep*
5. In the *Power & sleep* section
	1. *Screen > When plugged in, turn off after*: **Never**
	2. *Sleep > When plugged in, PC goes to sleep after*: **Never**

🌷 If your PC/NIC allows it, and you can configure the ADO pipeline somehow to try to wake up the PC if it goes to sleep, you can get a bit more environmentally friendly with a *Wake-on-Lan* solution. However, this usually also requires modifications in the BIOS/UEFI settings, which is not something that MT IT services usually allows. Plus you need to know the MAC address of the agent machine, and you need a third party tool that you can run in your pipeline to send a magic packet to the agent machine to wake it up, then wait for the response and so on. And it's a serious security vulnerability you're introducing by enabling WoL packets to roam the network, especially because they are originating from a source external to the MT domain.

## Remote Desktop Access

If the test server is not easily accessible physically/geographically, or some people need remote access to it because they work from home etc., then remote desktop access is a must.

### Enable remote desktop connections
1. Log in to the test server as local admin
2. From the *Start* menu select *Settings* (the little gear icon)
3. In the *Windows Settings* window select *System*
4. From the left sidebar select *Remote Desktop*
5. Toggle the *Enable Remote Desktop* switch to *On*
6. If you followed the instructions in the **Power settings** section, the *Keep my PC awake for connections when it is plugged in* checkbox should be checked and disabled.
7. The *Make my PC discoverable...* checkbox should be checked and disabled.

### Configure who can connect
1. Scroll to **User accounts** in the *Remote Desktop* section of *Windows Settings*
2. Click the *Select users that can remotely access this PC* link
3. Add the users who require remote access to the test server

# Test Automation

## Software Installation

### Dependencies

On the top of the ever-changing software version and Python (package) version dependencies, there are some environment settings that must be taken into consideration.

1. Some of the environment variables...
	1. refer to directories that must be created.
	2. are also used in the pipelines 
2. The directories used by the test automation framework must be accessible by the user running the Azure agent
3. The directories accessed by the pipeline (the Azure agent, actually) must match the directory structure on the server
4. All of the above must match the test automation framework configuration file

### Python
NOTE: As long as the `tafrunner.exe` is installed on the test server, the correct Python interpreter will be included with it. It is not necessary to install Python separately just to run automated tests. However, the test automation framework's own pipeline(s) might need Python, so it's best to install it anyway.

The Python version used in the Test Automation Framework at the time of writing this article is 3.8. This is due to the Squish dependencies.
When you want to download such a legacy version of Python, it can be a bit cumbersome to find the right links on the [Python Downloads for Windows](https://www.python.org/downloads/windows) page, so search for 3.8.10 there, because "*Python 3.8.10 was the last full bugfix release of Python 3.8 with binary installers*". All later releases are patches only.

Follow this guide for details: - [Setting up Python](/Guides/New-Joiner-Guide/Setting-up-your-development-environment/Setting-up-Python.md)

### PostgreSQL

**DO**: Install PostgreSQL 14 as a **service**.  
**WHY**:
What you actually need to do is, install the latest version of PostgreSQL supported by the latest version of SQLAlchemy compatible with the latest Python version supported by the automation engine used in the test automation framework :-D That is version 14 at the time of writing this article.

Follow this guide for [Installing PostgreSQL](/Guides/New-Joiner-Guide/Installing-PostgreSQL.md)

### Squish

The Squish version currently used by the Test Automation Framework is 6.6.2.
An installer for the correct version of Squish with the correct "binary compatibility" is available on the server on the secondary disk's TAR partition under the `F:\Squish_Installers` folder. (If there are multiple installers in the folder at the time you're reading this, use `squish-6.6.2-qt515x-win64-msvc14.exe`)

Follow this guide for details: [Installing Squish](/Guides/Squish.md#installation)

### Azure Agent

Installing and configuring the Azure/VSTS agent is inseparable from the process of setting up agent pools and pipelines in ADO itself, so please refer to : [ADO Agent Setup](/DevOps/ADO-Agent-Setup.md) for details.

## Environment Variables 

Setting the environment variables correctly means keeping all of their occurrences in sync. You might need to come back to this section AFTER you've installed the test automation framework or some of its components on the test server.

📢 Relying on environment variables is bad practice, and more importantly, it's an excellent way to trap yourself in a configuration hell-loop. 
However, we can't get rid of all of them, because they are out of our control. In the test automation framework (code and config), try to avoid using them, or at least avoid creating new ones.

📢 You need to edit the **System** variables! When the tafrunner is executed by the pipeline, i.e. the user running the Azure agent, the settings of the System Network user will be in effect, so if you define your environment variables for your own user, those will not be seen when they are needed.

📢 You need to restart the Azure agent after setting or updating the environment variables. You can do that from *Services* on Windows.

1. Log on to the test server as an Administrator.
2. Control Panel > type "*env*" in the search field
3. Click the 🛡*Edit the system environment variables* link
4. Press *Environment Variables...* at the bottom of the dialog
5. Set each of the below variables as ***System variables*

#### TAF_ROOT

Simply the directory where the test automation framework is installed. 

This environment variable is used in the configuration file as well as the pipeline definition .yaml file, so if you modify the directory structure under the TAF_ROOT directory you also need to update the .yaml file:
- `downloadPath: '$(TAF_ROOT)/AUT_DEPLOY/INSTALL'` in the DownloadBuildArtifacts@1 task
- `workingDirectory: '$(TAF_ROOT)/AUT_DEPLOY/INSTALL/$(artifact_name)'` in the CmdLine@2 task that creates the `*_pipeline_info.txt` files
- `script: '$(TAF_ROOT)/tools/tafrunner/tafrunner.exe -t smoke --sut new -c DEV'` and `workingDirectory: '$(TAF_ROOT)/tools/tafrunner'` in the CmdLine@2 task that actually starts `tafrunner.exe`
	- There are paths defined inside the script as well, so check those too
- `$Env:TAF_ROOT` in the PowerShell@2 task that checks if a report has been generated successfully
- `reportDir: '$(TAF_ROOT)\REPORTS\ADO...` in the PublishHtmlReport@1 task

#### SQUISH_DIR 
It must point to the active Squish installation directory. The only real reason to set this variable is because the [Froglogic Knowledge Base article on using the Squish module in external Python scripts](https://kb.froglogic.com/squish/howto/using-squish-module-python-scripts-applications/#microsoft-windows) provides this solution as *THE* solution, but even in that guide, the SQUISH_DIR variable is only used to add the Squish installation path to the PYTHONPATH variable. However, currently the test automation framework is going along with this setup, and uses the SQUISH_DIR to start the Squish Server. (Subject to change in the future.)

Couple of things to point out here:
1. It is not crucial to set this variable on the test server, as long as the `tafrunner` is installed as an .exe file or in a virtual environment and the configuration file contains the same variable with the correct value.
2. It is bad practice to use the PYTHONPATH environment variable and should be avoided. (The Froglogic developers are C++ developers and even their Python experts are primarily C++ developers whose job mostly consists of writing Python wrappers around C++ extensions, so don't listen to them.)

#### SQUISH_LICENSEKEY_DIR 
It is where the Squish license file (e.g. `.squish-3-license`) is stored. During the installation process, Squish doesn't ask where it should be stored, but you're free to move it around afterwards. The default location is the user's home, usually something like `C:\Users\testuser-1\.squish-3-license`. The user running the Azure agent may not have access to this directory by default, so it's usually better to move the license file to a more accessible location.

1. Copy the license file to either
	1. `C:\test_resources`  (or whatever name you choose)
	2. `%TAF_ROOT%/resources`
2. Give the user that runs the Azure agent (e.g. *Network Service*) permission to the directory
3. Set the SQUISH_LICENSEKEY_DIR environment variable to the location of the squish license file. If it isn't clear, the value of the variable should not be the file itself, but the directory where it is located.

#### PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION
If the protocol buffer package is outdated, you might need to set this variable, so that the tests can keep running until you regenerate the gRPC code.

Set it as a **System variable**. Its value is simply `python`. 


## Firewall

Whatever services are running on the test server, you need to open a port for them on the firewall.

At MT, we only have to worry about the Windows Defender Firewall. You can either open each port, specifically, like in this guide for PostgreSQL: [Open a Firewall Port for PostgreSQL](https://manifold.net/doc/mfd9/open_a_firewall_port_for_postgresql.htm) or you can open a port for the application itself. The latter is what you see currently on the test server.

On the test server, you'll want to make sure that (at least) these four applications are allowed to communicate through the Windows Firewall:
- squishserver.exe
- \_squishserver.exe
- startaut.exe
- postgres.exe

**This is how you open the firewall for an application**
1. Open the Windows *Control Panel*
2. Navigate to *System and Security > Windows Defender Firewall*
3. Click *Advanced settings* (The page will look a bit weird, telling you that you need admin rights for everything, and it's all controlled by company policy etc.)
4. In the *Windows Defender Firewall with Advanced Security* window: 
	1. Select *Inbound Rules* from the left side panel
	2. Select  *New Rule...* from the right side panel
	3. In the *New Inbound Rule Wizard*
		1. Select **Program** for the *Rule Type*, click *Next*  

		   ![PgSQL_Open_Port_Rule_Type.png](/.attachments/PgSQL_Open_Port_Rule_Type.png)
		   
		2. Browse to the executable of the software you want to allow through the firewall installation and select the actual .exe file in the **This program path** input field, then click *Next*    

		   ![PgSQL_Open_Port_Program_Path.png](/.attachments/PgSQL_Open_Port_Program_Path.png)
		   
		3. Select **Allow the connection**, click *Next*
		4. Check the **Domain** and **Private** checkboxes and UNCHECK **Public**, when you're asked *"When does this rule apply?"*, click *Next*
		5. Give your new rule a descriptive name and click *Finish*


## Test Automation Framework
### Initialize the Database
There are a few ways to do this. Check out the dedicated page: [Database Setup](/Test-Automation-Framework/Database/Database-Setup.md)

### Runner Installation
Currently there is no complicated deployment process defined for the test automation framework. To make it easily manageable for the Azure agent, it can be used as a single executable: `tafrunner.exe`  
All you need to do is copy the executable into the correct directory on the test server, modify the configuration file and wait for the pipeline to trigger the test execution, or run it manually.
- [Test Automation Framework Configuration](/Test-Automation-Framework/Test-Automation-Framework-Configuration.md)
- [Test Automation Pipelines](/DevOps/Test-Automation-Pipelines.md)

Of course there are some other prerequisites, but those were covered by all the steps leading up to this point in this guide. Here's a quick checklist:
- Environment variables are set up with the correct values
- The directory structure is matching the configuration
- Dependencies are installed and configured
	- The database is running (as a service) and the credentials are known to the framework
	- The binary compatible version of Squish for Qt is installed
	- Matching Python version is installed (optional... kinda)

#### Directory structure

Once again, you have to keep in mind the usual dependency loop: *environment variables - directory structure - pipeline yaml - configuration file*.

1. Create the directory where you will install the framework.
	1. This path will be the value of $TAF_ROOT
2. Create the directories used by the pipeline(s). 
	1. Location of `tafrunner.exe`, usually $TAF_ROOT\\tools\\tafrunner
	2. The directory where the agent downloads the SUT artifacts, usually $TAF_ROOT\\sut_deploy\\install
	3. The CI/CD reports are picked up by the pipeline usually from $TAF_ROOT\\reports\\ado
3. 📢 The user running the Azure agent will also need access to these directories. It's better to set that up now, before there is anything in those directories, otherwise when you add the new permissions, Windows will apply it to all directories and files under it, and that can take a very long time. 
	1. Make sure that the directories references in the .yaml file (the ones you just created) are accessible for the user running the Azure agent (probably the user *Network Service*)
4. You can also create the directories used in the test automation framework configuration file, but those are automatically created if they don't exist, so it's not necessary

## Restart
When you you're done, Windows will need a restart to apply all these changes.

After the restart, you can check that the Azure agent is configured to run as a service, with the correct user.

![Azure_Agent_Services_User.png](/.attachments/Azure_Agent_Services_User.png)

The Status of the agent will depend on how you set it up during installation. It is OK if it's not running yet. You can start it now and set the Startup Type to Automatic, or you can do it after a quick test of the `tafrunner.exe`.  

## Test

It's a good idea to test the test automation framework before letting the pipeline do the job.

1. Download an artifact from the SUT's pipeline
2. Copy the artifact into the $TAF_ROOT\\sut_deploy\\install directory (or whatever other directory you configured in the pipeline and in the framework config file)
3. Open a command line and `cd` into $TAF_ROOT\\tools\\tafrunner
4. Run the tafrunner command: `tafrunner.exe -t smoke --sut new -c DEFAULT`
	1. If you don't have a "smoke" test set, change it to the ID of another, short and simple test set
	2. Change the "DEFAULT" configuration profile to whatever profile you will use on the test server, which should be the same you configured for the SUT's CI/CD pipeline
5. Check that the reports are created in the subdirectories of the $TAF_ROOT\\reports\\ado directory and the path and naming follows the configured values (according to the test automation framework config file)

# Troubleshooting

See the dedicated pages: [Troubleshooting](/Guides/Troubleshooting/Troubleshooting.md)