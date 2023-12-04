Developing Squish test scripts in PyCharm requires a little extra effort compared to the Squish IDE, but it pays off. More importantly: it is necessary, for running the tests unsupervised on the test server without modifications, so it's not a question of personal preference.

1. The Squish IDE automatically **starts the Squish server** when it is executing a test script. PyCharm can also be set up to do the same, but it is much more convenient to start the server manually from the command line and keep it running.
1.1 Open a command line (type *cmd* in the Windows Menu)
1.2 Navigate to your Squish installation directory
`C:\>cd %SQUISH_DIR%`  (If you have the environment variable)
1.3 Start the server without any parameters
`C:\Program Files\SquishForQt661\bin>squishserver.exe`
Alternatively, you can start it from any directory with `C:\>"C:\Program Files\SquishForQt661\bin\squishserver.exe"` or `"C:\>%SQUISH_DIR%\bin\squishserver.exe"`. Please note that the double quotes are only necessary if your Squish installation path includes a whitespace.
![image.png](/.attachments/image-6aa8f4fc-72c9-4645-87ae-4528826712ee.png)
2. The Squish API is provided by the _squishtest_ package. Since this package is not a standard Python package, autocomplete cannot help because the **function headers are not available**. 
Also, the `from squishtest import waitForObject` syntax won't work. Normally the signatures are found in a package's `__init__.py` file, so if we look at the _squishtest_ init file, it's clear why we can't reference its members:
```
from importlib import import_module
import sys

try:
    sys.modules[__name__] = import_module('squishtest%d' % sys.version_info.major)
except ImportError as e:
    if 'No module named' in str(e):
        raise ImportError("Cannot load %s module with this Python version" % __name__)
    else:
        raise
```

3. Squish IDE starts the AUT for you. You can start it for yourself with `squishtest.startApplication(aut_name)`. Before you start it, don't forget to set the Qt wrappers: `squishtest.testSettings.setWrappersForApplication(aut_name, "Qt")`. 
Here the `aut_name` variable is a string, that is the name of the AUT as it is registered in the Squish server settings.
![image.png](/.attachments/image-d110a724-5f11-446c-996a-42c058de3981.png)

4. The **_Object Map_** is your responsibility. 
4.1 In PyCharm the **names.py** file is not a special element, you have to treat it like **any other module** . It also means that you **get to** treat it like any other module. 
It is a good idea to keep an object map for each version of the AUT, and you can simply import the one you are working on ATM. Currently there is a package in the Titrator System Tests repo where you can store your object maps under `squish_taf\object_maps`. You can create your own Python files under that directory/package with any name, then simply import it into your test script. It is a good idea to stick with the standard "names" name for the object map within the code for compatibility, so when you import your object map, import it as "names" please. For example: `from squish_taf.object_maps import terminal_10016 as names`
4.2 **Updating the object map** is also up to you, but you can get help from the Squish IDE for that. 
4.2.1 Using the Spy Perspective, launch the AUT and select your GUI element that you want to use. 
4.2.2 Right-click to get to the context menu and select _Copy Real Name_
4.2.3 Paste the real name into your object map and give it a symbolic name of your liking
`myFavoriteStackView = {"container": main_QQuickApplicationWindow, "id": "stackView", "type": "StackView", "unnamed": 1, "visible": True}`
![image.png](/.attachments/image-e5346c86-5f3f-402b-996a-270cb52fe2d9.png)

And that's pretty much all there is to getting started with Squish test development in PyCharm.

