[[_TOC_]]

# Installation
## From binaries
If you are using the Terminal Simulator on Windows, you can install Squish from the binaries provided by Froglogic.

### Selecting a Squish version
*Squish for Qt* requires "binary compatibility", which means that the toolchain used to build Squish must be the same as the toolchain used to build the application under test. 
Before you install Squish, you must determine which version of Qt was used to build the SUT (Terminal Simulator).

Currently, the Terminal Simulator is built for 64bit architecture with Qt 5.15 using the MSVC tools. 
To fulfill this "binary compatibility" requirement, you must install Squish for Qt 5.15, msvc64.

Since the Qt company bought Froglogic, the licensing prices went up by a factor that was not acceptable for us.
Therefore, we are using the last version of Squish that was released before the expiry of our licenses.
The binary packages are available on the Project Orion SharePoint site under [10_Testing > 02_TestAutomation > 01_Squish > 05_Tools](https://mt1.sharepoint.com/:f:/r/sites/intranet_anachem/RnD/pj_g5orion/10_Testing/02_TestAutomation/05_Tools?csf=1&web=1&e=kKVhoP).
Another location where you can find the Squish binaries is the Test Automation Server's secondary disk: `F:\Squish_Installers`.  

The version installed on the Test Automation Server and in our local development environments is Squish 6.6.2. for Qt 5.15, msvc64.

### Installing Squish

To be able to install Squish using the installer: 
1. You *should* have administrator rights on your computer, but it is not strictly necessary.
2. You must have a valid Squish license

To install Squish:
1. Download the Squish installer from the Project Orion SharePoint site or from the Test Automation Server.
2. Run the installer and follow the instructions.
3. When prompted, enter the Squish license key.
4. On the **Components** page: 
   1. Select the *Squish IDE* component.
   2. The *Squish Tools* component is selected by default.
   3. Unselect the *Test Center* component. We don't need it and it requires a license.
5. On the **Script Languages** page, select *Python* version 3.8.
6. The **Installation Folder** defaults to your home directory. 
   1. It is alright to leave it as is on your local development machine, but on the Test Automation Server, you should change it to a directory accessible to other users (e.g. `C:\opt\squish-<version>-<qt_version>`). This is where you need Admin rights.
   2. In some cases - depending on how Squish was used by other processes and tools - we had issues with spaces in the installation path. If you want to be sure to avoid this issue, use a path without spaces.
7. Create **Shortcuts** as you see fit.
8. On the **Ready to Install** page, click **Install**.
9. Wait for the installation to complete.
10. If you can, restart your computer. (You will have to, eventually, before you can use Squish anyway.)

## From source

# Configuration
## PATH environment variable
If you only have one version of Squish installed, you can add the installation path to the `PATH` environment variable. This will allow you to run Squish tools from the command line without having to specify the full path to the executable. 
    1. On Windows 10, you can do this by searching for "Edit the system environment variables" in the Start menu.
    2. Click on the **Environment Variables** button.
    3. In the **System variables** section, select the `Path` variable and click **Edit**.
    4. Click **New** and enter the path to the Squish installation directory (e.g. `C:\opt\squish-6.6.2-qt515-msvc64\bin`).
    5. Click **OK** to close all the windows.

# Quick start guide
# Next steps