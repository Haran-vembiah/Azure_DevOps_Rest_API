Handling Python package dependencies can get quite cumbersome if you're not using the PyPI-recommended package installer; pip. if you've made it this far, you must already have installed Python 3.7.x, which comes with pip installed. There's only one thing left to do, and that is enabling pip to install packages from behind the corporate proxy.

One of your options is to simple pass the proxy details in the command line every time you use pip.

#### Add the proxy details as command line arguments
You need to pass the proxy's host name and port, along with your credentials in the command line. To be sure, you should also add a list of trusted hosts, where pip might try to connect to download dependencies.
```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  --proxy http://<windows_user>:<windows_passowrd>@<proxy_host>:<proxy_port> <package_name>
```

Note that you don't have to include your domain in the username.


If you're going to use PyCharm to install packages - which is the preferred way - then you'll want to create a PIP.INI file for your proxy configuration.

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

