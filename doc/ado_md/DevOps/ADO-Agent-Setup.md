
[[_TOC_]]  
  
# Overview  
  
**TL;DR**: The test automation framework is connected to the ADO pipelines via an agent running on a Windows machine and this guide will walk you through the installation and configuration.  
  
An ADO agent is a piece of software that runs on a machine and is responsible for executing the tasks in an ADO pipeline.  
In order to be able to run the CI/CD tests, we need to install an agent on the test automation server.  
  
Microsoft offers multiple options for running an Azure agent, depending on the available infrastructure and the requirements of the project.  
A non-exhaustive list of options is:  
- [Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml)  
- [Azure Virtual Machine Scale Set agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/scale-set-agents?view=azure-devops)  
- [Self-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser#install)  
  - [Self-hosted agents on Windows](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-windows?view=azure-devops)  
  - [Self-hosted agents on Linux](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops)  
  - [Self-hosted agents on Docker](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/docker?view=azure-devops)  
  
We will use a self-hosted agent on a Windows machine, because:   
- It is a flexible solution, and we can customize it to our needs.   
- The test automation framework is using *Squish for Qt* (at the time of writing this article), which is a GUI testing tool, so it needs a graphical environment to run in. This means that we cannot use a Microsoft-hosted Linux agent or a Docker agent without customization, because those are headless.  
- MT policy is to keep all intellectual property on-premises, therefore the project cannot use Azure DevOps Services (i.e. cloud), and so we are stuck with the Azure DevOps Server.  
  
📢 Microsoft is pushing the cloud version of Azure DevOps, and the on-premises version is lagging behind in terms of features and support.  
Other companies, like Atlassian have already discontinued their on-premises products in favor of the cloud version, but Microsoft is adhering to its own [Fixed Lifecycle Policy, and will support ADO Server 2022 until at least January 11 2028](https://learn.microsoft.com/en-us/lifecycle/products/azure-devops-server-2022).    
This, however, does not mean that it will keep the features available in Azure DevOps Server in sync with the cloud version's features.  
🌧 One of these limitations is already affecting the test automation framework. Currently the Orion project is using Azure DevOps Services, but the migration back to Azure DevOps Server is imminent (probably already complete by the time you are reading this), and that means that **the agent will have to be (or already is) downgraded to version 2.x from version 3.x.** The differences between the two versions that impact the installation process must be included in this guide.

In general, the installation process is very well documented on Microsoft Learn.
- [Self-hosted Windows agents (2.x)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-windows-agent?view=azure-devops)
- [Self-hosted Windows agents (3.x)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops)
There are some undocumented steps and unanswered questions, though, so the rest of this article will guide you through the installation process step-by-step.
  
# Prerequisites  

## Think first

This guide is for installing a new ADO agent on a more-or-less clean host.
If you already have agent(s) installed, or you have agent pools set up and active in ADO, this might not be what you need.  
The Microsoft documentation on agents is quite extensive and provides instructions for various situations, so perhaps you want to take a look at those first.
- [Replace an agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#replace-an-agent)
- [Remove and reconfigure an agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#remove-and-reconfigure-an-agent)
- [Diagnostics](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#diagnostics)

And there are many other topics which might help you with your issue, before you apply a scorched earth policy, so browse the [Azure Pipelines agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser) docs first.

## Azure DevOps  
### ADO Access and Permissions 

**TL;DR**: If you are a member of the *Orion Test Automation* group, you have access to the TAF agent pool, which is the one you need.

![ADO_TAF_Pool_Security_Tab.png](/.attachments/ADO_TAF_Pool_Security_Tab.png)


In order to be able to install and configure the agent, you need to have access to the ADO project and the necessary permissions to create and manage agents. 

A simple way to check it is making sure that the the *New agent* button is enabled when you navigate to *Organization settings>Pipelines>Agent pools* and select the agent pool used by the test automation framework, which is currently called TAF.

Beyond this, it can get way too complicated to discuss it in this article, so check out the Microsoft Guides:
- [Confirm the user has permission](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#confirm-the-user-has-permission) 
	  To some extent, this one also applies to the permissions required for setting up the agent on the host.
- [Prepare permissions](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#permissions)

## Host

### PowerShell

Make sure that the version is 3.0 or higher.  
If you're on Windows 10, the PS version is definitely higher than 3.0, the standard is 5.1.

1. Open *Windows PowerShell* on the host machine
   💥**Not** *Windows PowerShell ISE*  
   ![NOT_PowerShell_ISE.png](/.attachments/NOT_PowerShell_ISE.png)
2. Type `$PSVersionTable.PSVersion` at the prompt and hit *Enter*
3. Make sure that the number in the `Major` column is at least 3  
![PowerShell_Version_Check.png](/.attachments/PowerShell_Version_Check.png)


### Directory structure and permissions

**TL;DR**: Create a new directory on the host: `C:\agent`

Theoretically, you can install the agent wherever you want to. In practice, it's easiest to stick with the convention: `C:\agent`. You don't gain anything by playing around with the installation location, but it can come back to bite you later.

If you're conscious about security or your host is too exposed, make sure to limit the access to the installation folder. It is a good idea in general, but at MT, administrator privileges are hard to come by, and if you need to do something in a panic as admin, but IT services is forcing you to jump through hoops because your temporary security exception expired, you'll be very unhappy.



# Installation

## Download

When you checked your user's permissions, you opened the *Agent pools* page in ADO and selected the agent pool you wanted to use.
On that same page, the upper right corner has a *New agent* button. Click it.

ADO will display a dialog with all the details you need. 
1. Select the tab matching your platform
	1. Select the **Windows** tab
	2. Select **x64** on the left sidebar of the dialog
2. Copy the first two commands into a text file, because you might need to edit their arguments.
	1. *Create the agent*
		1. Here, you might want to change the command before you run it later, so that you create the directory with a name you actually want, in the parent directory you actually want.
	2. *Configure the agent*
		1. One of the arguments passed here is the location of the downloaded zip file, containing the agent. The command presumes that it will be in your user's Downloads folder: `ExtractToDirectory("$HOME\Downloads\vsts-agent-win-x64-3.230.0.zip"` If you saved the file elsewhere, edit the command accordingly.
		2. The other argument is the directory where you want to extract the zip file, i.e. the "target" directory. The default is `$PWD`, so whatever directory you're standing in. You might want to update that, if you want to run the command from another directory. (You shouldn't. You should just `cd` into the target directory before running the command.)
	3. *Optionally run the agent interactively*
		1. Don't run this command at all.
3. Click *Download*

## Before your start

### Clean up
#### Jobs
Check if there are queued jobs in the agent pool (*Agent Pools > YOUR_POOL_NAME*, then select the *Jobs* tab). If there are, make sure that the agent does not start automatically after installation, or you'll have a bunch of failed runs, unless all other tasks on the host are complete, and you can actually complete the tests. (This step is also mentioned in the installation instructions below.)

#### Agents
If there are agents in the agent pool, make sure that those which no longer have an actual ADO agent installation behind them are deleted.
Also, if you want to reuse the name of an agent that is defunct, delete that agent first from the agent pool.


### Prepare your answers

The ADO agent installation script is going to ask you a few questions, so make sure you have the answers ready.

|**Question**|**Answer**|**Comments**|
|------------------|------------|------------------|
|`Enter server URL`|https://dev.azure.com/AnaChem|It's simply your ADO URL up to and including the organization name, but not the project name.|
|`Enter authentication type (press enter for PAT)`|PAT (or just hit enter)|We use Personal Authentication Tokens for this registration process, so make sure you have one for the same user that has access to the Agent Pools.|
|`Enter personal access token`|The user's PAT (the long funny string), who clicked *New agent* on the *Agent pools* page|If you don't know how to get a PAT, here's how: [Create a personal access token for agent registration](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/personal-access-token-agent-registration?view=azure-devops#create-a-personal-access-token-for-agent-registration)|
|`Enter agent pool (press enter for default)`|TAF|At least that was the name of the pool at the time of writing this article. If you're reading this after the regression to on-prem ADO, it might be different.|
|`Enter agent name (press enter for <YOUR_HOST_NAME>)`|OTASRV|A short name, that does not exist in the agent pool yet.|
|`Enter work folder (press enter for _work)`|Just press enter. |There's no reason to change it, unless you have a special use case and you know what you're doing.|
|`Enter run agent as service? (Y/N) (press enter for N)`|Y| We definitely need it to run as a service. 📢 Note that for this option you need to be administrator, which means you have to start the PowerShell CLI as Administrator.|
|`Enter enable SERVICE_SID_TYPE_UNRESTRICTED for agent service (Y/N) (press enter for N) `|Y| For various reasons. See the discussion about it on the Microsoft GitHub repo, issue [#2814](https://github.com/microsoft/azure-pipelines-agent/issues/2814) |
|`Enter User account to use for the service (press enter for NT AUTHORITY\NETWORK SERVICE)`|Just press enter.| NEVER user an actual user account to run a service. You can't stay logged into the host all the time, others might need to do some maintenance there.|
|`Enter whether to prevent service starting immediately after configuration is finished? (Y/N) (press enter for N)`|Y| Don't need to start the agent service right away. Do some checks first and make sure that when you ***do*** start it, the queued jobs won't fail one after the other.|


## Start 
### Run the installation scripts

This is easy-peasy, now that you have all your answers prepared, and your commands modified to your needs, you can run the installation script.

1. Open a **PowerShell CLI** as **Administrator** on the host where you want to install the agent. (You probably have one open already from the step where you checked that the PS version is >= 3)  
   ![NOT_PowerShell_ISE.png](/.attachments/NOT_PowerShell_ISE.png)
2. `cd` into the directory you created, where you want to install the agent, most likely `C:\agent` or `C:\agents`
3. Run the command that starts with `Add-Type`. This is the one that was in the *Create the agent* code box in the agent download dialog. Make sure you run your modified version, if you modified it.
	1. All it really does is extract the zip file into a directory.
4. Start the configuration script in the same directory: `.\config.cmd`
5. Answer all the questions with your prepared answers.

At this point your agent should be installed as a service, but it should not be running yet. You can continue setting up your environment, for example by following the instructions on the [Test Automation Server Setup](Test-Automation-Server-Setup.md) page, and once you're ready, start the agent service: [Run as a service](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent?view=azure-devops#run-as-a-service)

