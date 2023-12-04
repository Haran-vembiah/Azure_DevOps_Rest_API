If you keep running into connection problems when trying to install a Python package with pip, you are probably being held back by the corporate proxy. To overcome this issue, there are two solutions.

#### Add the proxy details as command line arguments
You need to pass the proxy's host name and port, along with your credentials in the command line. To be sure, you should also add a list of trusted hosts, where pip might try to connect to download dependencies.
```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  --proxy http://<windows_user>:<windows_passowrd>@<proxy_host>:<proxy_port> <package_name>
```
#### Configure the proxy in a pip.ini file
For a more permanent solution, create a pip.ini file in your ```%APPDATA%\pip``` folder

```
[global]
proxy = http://<proxy_host>:<proxy_port>

trusted-host = 
	pypi.org
	pypi.python.org
	files.pythonhosted.org
```
You can also add your credentials ```proxy = http://<windows_user>:<windows_passowrd>@<proxy_host>:<proxy_port>```, but that is a very ill-advised solution to say the least.

More details on the topic: https://pip.readthedocs.io/en/stable/user_guide/#config-file