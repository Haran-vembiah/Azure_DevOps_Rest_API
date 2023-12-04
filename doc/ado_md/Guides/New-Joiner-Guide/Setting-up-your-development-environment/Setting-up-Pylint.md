Pylint is a Python code analysis tool. Visit the official website for more details: https://www.pylint.org/

##### Check if pylint is installed
Chances are; pylint is already installed along with Python. You can verify this either from the command line: 
``` dos
C:\>where pylint
C:\Program Files (x86)\Python\Python37-32\Scripts\pylint.exe
```
Or by going to your Python installation directory and checking the _Scripts_ sub-directory.
**Note**: If the _where_ command didn't find pylint, but it was actually in the _Scripts_ directory, you forgot to add _%PYTHONHOME%\Scripts_ your **PATH** environment variable.

##### Install pylint with pip
If pylint is not available, you can install it with pip. The only hurdle is the corporate proxy, but there's a fairly easy solution here: [Using PIP from behind a proxy](/Guides/Troubleshooting/Using-PIP-from-behind-a-proxy))
``` dos
C:\>pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  --proxy http://<windows_user>:<windows_passowrd>@<proxy_host>:<proxy_port> pylint
```
This command will install pylint globally - not just in your virtual environment - and now you can check the actual installation path with 
``` dos
C:\>where pylint
```

Note: Consider adding squishtest to extension-pkg-whitelist.