[[_TOC_]]  

# Version compatibility

The test automation framework is using SQLAlchemy to connect to the database, so we have to consider which versions of PostgreSQL it supports. At the time of writing this article, SQLAlchemy supported the following versions of PostgreSQL: 

|**SQLAlchemy version**|**Support type**|**PostgreSQL version**|
|------------------|------------|------------------|
|1.4.50 (Legacy version)|Fully tested in CI|9.6, 10, 11, 12, 13, 14|
|1.4.50 (Legacy version)|Normal support|9.6+|
|1.4.50 (Legacy version)|Best effort|8+|
|2.0 (Current release)|Fully tested in CI|9.6, 10, 11, 12, 13, 14, 15|
|2.0 (Current release)|Normal support|9.6+|
|2.0 (Current release)|Best effort|9+|

The up-to-date information on SQLAlchemy's support for different RDBMSs is available on 
- [SQLAlchemy 1.4 docs](https://docs.sqlalchemy.org/en/14/dialects/index.html#support-levels-for-included-dialects)
- [SQLAlchemy 2.0 docs](https://docs.sqlalchemy.org/en/20/dialects/index.html#support-levels-for-included-dialects)

(At the time of writing this article, SQLAlchemy 2.0 just moved from Beta to *Current release* 2 weeks before, and a switch to the new version was not warranted yet.)

So there is support for PostgreSQL 14, and according to the [**PostgreSQL Feature Matrix**](https://www.postgresql.org/about/featurematrix/), the extra functionality in version 15 is not really essential for the test automation framework, however, whenever possible, it would be worth upgrading to it, because there are some improvements in replication, and some extra regex functions.

**But why not an older version of PostgreSQL?**   
Mostly because the test automation framework is using JSON fields in numerous tables, and those are not supported in earlier versions.

# Installing PostgreSQL


1. Download the installer for version 14 (14.10 at the time of writing this guide)
	1. Start from the list of [Interactive installers by EDB](https://www.postgresql.org/download/windows/) for Windows
		1. Click the link to the *actual* list of installers: "***Download the installer** certified by EDB for all supported PostgreSQL versions*" at the top of the page
	2. **OR** go straight to the [actual list](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads), but this link can change any time
	3. Download the Windows x86-64 version
2. Start the installer. It's the usual Windows *Next...Next...Finish* dance. 

|**Setting**| **Description**                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Installation Directory| The default (`C:\Program Files\PostgreSQL\14`) is fine                                                                                                                                                                                                                                                                                                                                                                     
|Components| The only questionable component is the Stack Builder. It is not required, but it doesn't really bother anyone either. However, it may allow you to install 3rd party components with commercial licenses.                                                                                                                                                                                                                  |
|Data Directory| The default (`C:\Program Files\PostgreSQL\14\data`) is fine. If you have a partition where you can keep this data safe, and the disk the partition it is on is fast enough, then it's actually a good idea to keep the data directory separate from the system. (On the current test server at MT-CH, the extra disk is a regular SATA SSD, while the system disk is NVMe M.2, so the data files stay on the system disk.) |
|Password for postgres| Just enter a reasonably safe password and make sure you don't lose it.                                                                                                                                                                                                                                                                                                                                                     |
|Port| Default `5432`is fine, unless you have more instances running on the same host. If so, pick any available port and make sure to adjust the configuration in the test automation framework.                                                                                                                                                                                                                                 |
|Locale| The test automation framework database stores multilingual data, so the only safe option here is **C**. **NOT** *\[Default locale\]*.|

After you set the above options, you'll get a **Pre Installation Summary**. It's a good idea to save it in a text file, and copy the installation log (the last line on the installation summary list) to a safe place.

Now you're **Ready to Install**, so click *Next* and wait a couple of minutes for the installer to finish its job.

If you installed the **Stack Builder** component, the installer will ask you if you want to launch it. I suggest you leave that for the time being, and uncheck it. If you want to install additional components, you can always launch it later from the Start menu.  

# Post-installation steps (optional)
## Firewall
If your database is on a remote host - e.g. on the test server - and you want to log into it sometimes from your local machine, then you'll need to open at least one port in the firewall.
You can check out the [Test Automation Server Setup Guide](/DevOps/Test-Automation-Server-Setup.md#firewall) for more details on how to do that.

## Path environment variable
It's a good idea to add the PostgreSQL bin directory to the path environment variable, so you can run the command-line tools from anywhere. The default location is `C:\Program Files\PostgreSQL\14\bin`.  

If you have multiple versions of PostgreSQL installed, you can add the bin directory of the version you want to use to the path, or you can add all of them, but make sure the version you want to use is the first one in the path.


