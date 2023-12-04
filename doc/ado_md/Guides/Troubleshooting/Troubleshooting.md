## Missing or misconfigured Squish license

When you run `tafrunner.exe`, or when a pipeline triggers a run you might find a long exception traceback with this message hidden in it somewhere:
```
ImportError: Could not find license file '.squish-3-license', searched the following user directory: 
C:\WINDOWS\ServiceProfiles\NetworkService/
You can specify the directory where Squish looks for the file by setting the environment variable SQUISH_LICENSEKEY_DIR before starting Squish.
****************************************************************
* This is an UNLICENSED version of Squish. Please install your *
* license key provided by froglogic. For assistance, please    *
* contact sales@froglogic.com                                  *
****************************************************************
```

As the exception shows, it usually means that the SQUISH_LICENSEKEY_DIR environment variable is not configured. Not a big issue to fix, just pay attention here first.
1. Whatever Squish version you're running, it is definitely NOT licensed to your local *Network Service* user.
2. Wherever your .squish-3-license file is, the *Network Service* user, or whatever other user is running the Azure agent, will need access to that directory.

##### Proper Solution
Set the SQUISH_LICENSEKEY_DIR environment variable as described in this guide: [[GUIDE#SQUISH_LICENSEKEY_DIR]]

##### Lazy (and risky) Solution:
Copy the Squish license file into the directory where Squish was looking for it. In this case, the `C:\WINDOWS\ServiceProfiles\NetworkService/` directory. By default, if the SQUISH_LICENSEKEY_DIR variable is not set, Squish will look into the $HOME directory of the user running it.
**BUT, modifying a system user's $HOME directory (or anything related to a system user, really) is never a good idea.**


## Outdated gRPC code

The error message might look something like this:
```
TypeError: Descriptors cannot be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
```

The message is pretty clear, you need to regenerate the gRPC code in the test automation framework codebase.
A temporary solution is setting the PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION environment variable: [[GUIDE#PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION]]

