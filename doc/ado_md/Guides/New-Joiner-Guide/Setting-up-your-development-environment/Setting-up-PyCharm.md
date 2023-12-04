[[_TOC_]]


# Download and install PyCharm CE

1. Go to https://www.jetbrains.com/pycharm/download/#section=windows and download the Community Edition of PyCharm for Windows
![download_community.png](/.attachments/download_community-abd91bb7-c924-42ce-bfc5-8784ee55a753.png)
(The download - as always - will start slowly and at first it will predict that it will take several hundred days to finish, but once it starts it done in a few minutes.)
1. Start the installer, once the download is complete.
1. If you get a Security Warning, click **_Run_**
![01_security_warning.png](/.attachments/01_security_warning-91636496-180d-42a4-825e-ab91111c3e43.png)
1. You will likely be presented with the usual _Do you want to allow this app to make changes to your device?_ dialog. Just click _**Yes**_
1. _**Next**_
![02_welcome.png](/.attachments/02_welcome-d43accdf-9dbe-4c60-8f6c-0ac81fd04c61.png)
1. The default location is fine, _**Next**_
![03_Location.png](/.attachments/03_Location-9d02da59-0638-41d8-a3f9-228b80963f68.png)
1. From the _Installation Options_, feel free to select any. Usually even adding the launcher to the PATH is pointless, as there's no scenario where you'd want to start PyCharm from the command line. _**Next**_
![04_options.png](/.attachments/04_options-90e61643-328d-4ff1-b216-955450fd1623.png)
1. The default _Start menu Folder_ is fine. _**Next**_
![05_Start_folder.png](/.attachments/05_Start_folder-db25c3dc-e779-4d32-bbeb-f9c49cb8ef95.png)
1. Wait for the installation to finish
![06_installing.png](/.attachments/06_installing-ea14633a-cd60-42e2-a8d4-311494d92590.png)
1. Sometimes the installer tries to launch PyCharm at the end of the process even if you don't confirm it in this window:
![10_Finish.png](/.attachments/10_Finish-f47a10a9-f8a6-4f25-ba78-077ce62e1fd9.png)
1. In that case, first you'll see a Windows Security Alert, where you'll have to **_Allow access_**
![07_defender.png](/.attachments/07_defender-bbd5df1c-7a82-4fd2-af2b-8c2237fa3327.png)
1. Then, because MT is using self-signed certificates, you'll get a warning. You have to Accept the certificate. You might get more than one of these warnings, just click _**Accept**_
![08_certificate.png](/.attachments/08_certificate-f5ff4df7-ca37-422c-8acc-f6467409b9b5.png)
1. If you have a previous installation of PyCharm, it will offer to import the settings. If you want to use those, go ahead, there are no team-wide settings you have to use.
1. The installation should be complete, just verify it by launching it from the Start menu.



# Configure the proxy
To be able to install plugins and allow PyCharm to access the internet in general, you'll need to configure the proxy.
1. Open the Settings window via _**File > Settings...**_
![11_File_Settings.png](/.attachments/11_File_Settings-7f92824e-feb0-47cc-a247-5508e1dd2f94.png)
1. In the Settings window select _**Appearance & Behavior > System Settings > HTTP Proxy**_
1. Select the _**Manual proxy configuration**_ radiobutton
1. Fill the details:
    - **Host name**: The proxy server you're normally connecting to. If you don't know it, you can find out by checking the automatic configuration script. Just enter http://wpad/wpad.dat in a browser and save the wpad.dat file. You can find the proxy server's name based on your IP address.
    - **Port**: Usually 8080 but the _wpad.dat_ file contains that along with the host name
    - **No proxy for**: _\*tfsanachem\*_ Thisis is to ensure that all connections going to our internal Git repo will have a direct connection, not via the proxy.
    - **Proxy authentication**: Checked
    - **Login**: Your Windows username, without the domain prefix.
    - **Password**: Your normal Windows password. **NOTE:** Every time you change your Windows password, remember to change it here too, otherwise PyCharm might try to access the proxy in the background and your account gets locked after 5 failed tries.
    - **Remember**: Checked
1. Click _**Check connection**_
    - Enter any external URL (e.g. https://stackoverflow.com)
      ![13_Check_Connection.png](/.attachments/13_Check_Connection-3d946d6a-13a8-4167-846e-f86f3c79aeb0.png)
    - Click **_OK_**
    - **NOTE**: It's possible that you receive another warning because of the self-signed certificate, just _**Accept**_ it.
    - The connection should be OK, unless you wait too long to Accept the certificate. In that case, just check again, this time PyCharm should remember the certificate and the connection should be OK.
      ![14_OK_Connection.png](/.attachments/14_OK_Connection-71946787-c221-400f-9430-b625935d9bc6.png)


# Configure Python Integrated Tools

1. Click _**File**_, A list of item will be displayed
   ![Click_Files.png](/.attachments/Click_Files.png)
2. Click _**Settings**_.
   ![Click_Settings.png](/.attachments/Click_Settings.png)
3. Select _**Tools**_ on the displayed box.
   ![Select_Tools.png](/.attachments/Select_Tools.png)
4. Click on _**Python Integarted Tools**_.
   ![Click_Python_integrated_tools.png](/.attachments/Click_Python_integrated_tools.png)
   - Select "Default test runner" as "pytest"
   - Select "Docstring format" as "reStructuredText"
   ![select_test_runner_doc_string.png](/.attachments/select_test_runner_doc_string.png)
   - Click **_OK_**