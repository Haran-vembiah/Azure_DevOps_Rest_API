Installing Python is a fairly straightforward task, but making sure that everything works the same way in your local development environment as in your teammates' can get tricky sometimes.

In our case the only real hurdle is to make sure that we're all using the same version, and that version is supported by the Squish binary we're using. We'll go into detail about that in another guide, so for now just follow along.


# Download

The current version we're using - and for which we have a compatible Squish binary - is **3.8.10**, but theoretically any 3.8.x version should work. Since the target platform of the System Under Test (SUT) is **64bit**, we'll also use the **64bit** version of Python.

When you want to download such a legacy version of Python, it can be a bit cumbersome to find the right links on the [Python Downloads for Windows](https://www.python.org/downloads/windows) page, so search for 3.8.10 there, because "*Python 3.8.10 was the last full bugfix release of Python 3.8 with binary installers*". All later releases are patches only.  
Here's a link to the download page of the version you need:[Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
Download the **Windows installer (64-bit)**. (Bottom of the page.)

The download used to get a bit hectic due to our corporate proxy, and initially it would report the download time as a few hundred days, but it was actually done in a few minutes. The proxy issue has been resolved since then, so it should be a smooth ride for you. Fingers crossed.

# Install
1. Double click the executable to start the installer
2. Make sure you check the *Add Python 3.8 to PATH* checkbox
3. Make sure you check the *Install launcher for all users* checkbox. That one only works if you have local admin rights on your machine.The [Test Automation Server Setup guide has some instructions on getting those rights](/DevOps/Test-Automation-Server-Setup.md#local-admin-user))
4. Click **Customize installation** instead of *Install Now*
5. On the next screen - **Optional Features** - select the features you need: 
   1. Make sure you select *Documentation* and *pip*. The former is useful for offline reference, and the latter is essential for installing 3rd party packages.
   2. Installing *tcl/tk and IDLE* is pointless, because we won't use either of those, but it doesn't hurt, so feel free to select that option.
   3. Same is true for the *Python test suite* option, because we will be using PyTest instead, but once again, id doesn't hurt anyone. Perhaps you'll be doing a course which requires one or both of these features, so it's up to you.
   4. The *py launcher* and *for all users* checkboxes will be selected by default if you opted for *Install launcher for all users* on the previous screen. Keep them selected.
6. On the next screen - **Advanced Options** - the important options to un/select are 
   1. *Install for all users* - Check
   2. *Associate files with Python* - Whatever you prefer
   3. *Create shortcuts for installed applications* - Check. Cause why not?
   4. *Add Python to environment variables* - Check 
   5. *Precompile standard library* - Check 
   6. *Download debugging symbols*
   7. *Download debug binaries* - It can be quite useful, but it requires Visual Studio 2015, which you might not have. If that's the case, uncheck that checkbox.
   8. *Customize installation location* - Make sure to choose a standard location for your installations. I recommend creating a *Python* sub-directory under *C:\Program Files*, then another sub-directory under that one for your specific Python version. This way it's easy to maintain multiple installed versions and you can recognize straight from the path which version you're dealing with.
7. Click *Install* and confirm the 🛡 UAC (User Account Control) prompt if you get one
8. Sit back and wait for the installer to finish its job
9. Once you get the *Setup was successful* message, the option to 🛡 *Disable path length limit* might be offered. 
   Take it. It's a good idea to have that option enabled. Having said that, it should be enabled by default on Windows 10, but it doesn't hurt to make sure. 
10. Click *Close*

# Configure
## PATH environment variable
The installer should have added the Python installation directory to the PATH environment variable, but it's a good idea to check it, and make sure it's near the top of the list. If you have multiple Python installations, make sure the one you want to use is the first one in the list.

The test automation framework is able to handle multiple versions of the SUT at the same time, but that requires multiple versions of *Squish for Qt* to be installed, and each of those may require a specific version of Python. 
This should not be an issue, since we're using virtual environments, but it's still a good idea to make sure that the Python version you want to use system-wide is the first one in the list.

1. Open Control Panel
2. In the search field (upper fight corner) enter 'env'
3. From the search results, select *Edit the system environment variables*, if you have local admin access, but if you don't, the *Edit environment variables for your account* will work too.
4. In the *System Properties* dialog click the *Environment Variables...* button
5. If you have local admin access, select the *Path* variable from the *System variables* list. If not, select the same from the *User variables for ...* list, then click *Edit...*
6. If you're **Path** variable already includes the recently installed Python version's installation directory and *Scripts* sub-directory, you just need to make sure that it's near the top of the list, or at least before all other Python installations (if there are others).
7. If it's missing, you can add it by clicking *New* and entering the recently created installation path, then repeating the same for the *Scripts* sub-directory. 
8. Click *OK*.

At this point we don't need to worry about the rest of the environment variables if you're starting from zero.