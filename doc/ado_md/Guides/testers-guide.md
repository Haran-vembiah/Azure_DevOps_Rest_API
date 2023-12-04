
[[_TOC_]]

#Overview
---

The embedded software for the G5 instruments is available as a *simulator*, which is fundamentally the same code as you would find on the actual target hardware, but it is compiled for 64bit Windows, and comes with a few handy features that make the testers' lives easier.

The vast majority of tests is carried out on the simulator, so it's important to get familiar with its basic operations and settings.

---
#Download
---
##Official release (at the end of each iteration)

The official release at the end of each iteration is uploaded to the SharePoint and you will receive an email to notify you. The same email will also warn you that the release files are too large to be downloaded using File Explorer.
1. If you are working from home, connect to your favorite MT VPN
2. Open the link from the email in a browser.
3. Click the *ellipsis* (...) next to the file name
4. Click the *ellipsis* in the context menu
5. Click Download
6. Repeat steps 3-5 for all 3 files: .7Zip, .exe and the Release Notes

![Download From SharePoint](../source/shared_resources/screenshots/01_01_Download_Sharepoint.png)


##CI/CD build (any time during the active iteration)
In the current setup, every time the developers push their changes to a branch in the main G5 instrument Git repository (*mt-anachem-instrument*), a new build is created and the artifacts are made available in Azure DevOps.

Unlike those of the official iteration releases, these artifacts are not uploaded to the SharePoint. However, they are still accessible to anyone who wants to take a peak at the half-baked features before they are released for testing.

Keep in mind, though, that any bugs or complaints based on such a build will be rejected and half of your reputation points will be deducted ;-).

1. No need for VPN connection, in fact it will just slow you down
2. Navigation panel (left) in Azure DevOps > Pipelines > Pipelines

   ![Pipelines-Pipelines](../source/shared_resources/screenshots/01_02_Download_Azure_Artifacts.png)
3. On the **Recently run pipelines** page, click on the latest run of the *mt-anachem-instrument* pipeline

   ![Pipelines-mt-anachem-instrument](../source/shared_resources/screenshots/01_03_Download_Azure_Artifacts_Pipeline.png)
4. On the pipeline's page, the **Runs** tab lists all the available run results. Click on a successful one
   (green disc with white checkmark icon)

   ![Pipelines-Latest-Run](../source/shared_resources/screenshots/01_04_Download_Azure_Artifacts_Pipeline_Run.png)
5. Counterintuitively, the artifacts aren't under the *Artifactory* tab.
   Click on the Job at the top of the list in the **Jobs** section

   ![Pipelines-Latest-Run-Job](../source/shared_resources/screenshots/01_05_Download_Azure_Artifacts_Pipeline_Run_Job.png)
6. The next page lists the tasks executed in the given job.
   The panel on the right shows the logs for the task on a black background. Click the link that reads *<u>1 artifact</u> produced*

   ![1-artifact-produced](../source/shared_resources/screenshots/01_06_Download_Azure_Artifacts_Pipeline_Run_Job_Artifact_Link.png)
7. On the **Artifacts** page,
   1. expand the list of files
   2. Click the *ellipsis* (the three vertically aligned dots at the end of the row)
   3. Click *Download artifacts*

      ![1-artifact-Download](../source/shared_resources/screenshots/01_07_Download_Azure_Artifacts_Pipeline_Run_Job_Artifact_Download.png)

---
#Installation
---
The G5 Terminal Simulator can be installed using the official installer or by simply extracting the 7Zip file to a convenient location.

- The **installer** is more convenient, but it overwrites previous installations of the simulator.
- The **7Zip** file is not much more complicated than using the installer, but it has the added benefit of allowing you to keep multiple versions and even multiple installations of the same version at the same time. (This can be quite useful for comparing the behavior of the application between releases to find exactly when a specific issue occurred, or for *freezing* an installation for further investigation without having to suspend your testing activities.)

##Using the installer

##Installing from the 7Zip file
---