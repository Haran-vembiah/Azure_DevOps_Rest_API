If for some reason you cannot install the pylint plugin, you can still set up pylint as an external tool in PyCharm.
1. Open PyCharm and navigate to _**File > Settings**_
1. Select _**Tools > External Tools**_ from the sidebar
![PyLint_ET_Step_1.png](/.attachments/PyLint_ET_Step_1-4256b92a-c625-4e42-a3f5-238788b0639c.png)
1. Click the ![PyLint_ET_Step_2.png](/.attachments/PyLint_ET_Step_2-4cfd0813-31b9-470d-b2de-7e7f3433a2f9.png) button.
1. Select the pylint executable, or just paste the path.
![PyLint_ET_Step_3.png](/.attachments/PyLint_ET_Step_3-f90615a0-8665-4ef7-ab32-a15afdfe14d3.png)
1. Click the _**Insert macro...**_ button next to the _Arguments_ field and select the _FilePath_ macro from the list. Click _**Insert**_
1. Insert the _ProjectFileDir_ macro in the _Working directory_ field
![PyLint_ET_Step_4.png](/.attachments/PyLint_ET_Step_4-889a91f9-7424-402c-8e24-ea3fcc090149.png)
1. Give the tool a name and a description
![PyLint_ET_Step_5.png](/.attachments/PyLint_ET_Step_5-c3015cc0-23d8-4467-bbcd-f4de86fb9e34.png)
1. Click _**OK**_
1. Done
![PyLint_ET_Step_6.png](/.attachments/PyLint_ET_Step_6-cb8b4304-0dc8-416b-9d27-5cb9de0391ac.png)