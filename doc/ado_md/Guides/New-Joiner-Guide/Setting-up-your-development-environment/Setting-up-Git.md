The code base of the test automation framework as well as the instrument-specific tests is stored in Git repositories. To be able to contribute to those repositories, you must have Git installed.

# Download and install
For the standard Git installation, just go to https://git-scm.com/download and click the _**Windows**_ link
![Download_Win.png](/.attachments/Download_Win-924b9ae1-bdda-43a2-b56a-55c2f4a7c95e.png)

The installation process is rather simple.
![Install_License.png](/.attachments/Install_License-72f77a78-daa3-4161-bcf4-aafc65df842d.png)
Click _**Install**_ 
![Install_Progress.png](/.attachments/Install_Progress-e1906e5b-3c3a-4cb8-87cc-a0fd587516cd.png)

Done!

# Configure
The Windows installer does pretty much everything there is to be done.
One thing left to do - as usual - enable Git to escape the corporate proxy. This is not always necessary. In fact, the only reason to do this is if you know you're going to need something from an external source, like GitHub. You can safely skip this section for now.

## Configure the proxy from the command line

```
git config --global http.proxy http://mydomain\\myusername:mypassword@myproxyserver:port
```
Then repeat for the https version (we don't have https proxies, so it's just to let Git know to use the same as for the http version)
```
git config --global https.proxy http://mydomain\\myusername:mypassword@myproxyserver:port
```
If you still decide to set it up permanently, just in case, then here's how you do it:
1. Open your .gitconfig file. It should be in your home directory. Make sure to show hidden files in that folder.
1. Add the below configuration after replacing your personal details:
```
[user]
	email = <corporate email>
	name = <name>

[http]
	proxy = http://mydomain\\myusername:mypassword@myproxyserver:port
	sslVerify = false
[https]
	proxy = http://mydomain\\myusername:mypassword@myproxyserver:8080
[credential]
	helper = wincred
```

Once this configuration is done, Git will always try to get to the repositories via the proxy, but since our own internal repos are inside the corporate network, it will always fail to connect.

To get around that, you can create an environment variable: 'no_proxy'
1. Open the Control Panel
1. In the search field (upper fight corner) enter 'env'
![Search_env.png](/.attachments/Search_env-db8d6b83-2c00-4da2-8d44-fa64e336be49.png)
1. From the search results, select  _**Edit environment variables for your account**_.
![edit_user_envs.png](/.attachments/edit_user_envs-3452083c-8e7d-4da5-b69b-acb230d0512f.png)
1. Click the _**New...**_ button
![new_env_var.png](/.attachments/new_env_var-aa4c1052-ba5b-4eb9-a30e-028c3e9484d7.png)
1. Enter 'no_proxy' for the variable name
1. Enter the Git repository's hostname in the value field. (In our case it's 'tfsanachem')
![no_proxy.png](/.attachments/no_proxy-53c8938f-ff4f-459d-ab35-3e23e4aedc7a.png)
1. Click _**OK**_


# Optional GUI clients
If you prefer to manage your git repositories from a GUI application, there are several available.
In general, this is not necessary, as most of the time it's easiest to control Git from PyCharm, and when there's a problem, you'll probably end up using git from the command line.

However, the one GUI Client that's quite mature and usable, is TortoiseGit. You can download it here: https://tortoisegit.org/, if you want to, and there's a list of other available GUI clients here: https://git-scm.com/downloads/guis.
