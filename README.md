# Overview
The PREMIS Utilty is a graphical utility used to generate [PREMIS](https://www.loc.gov/standards/premis/) metadata records for use in digital preservation systems and digital asset management systems. Records can be exported in both XML and JSON formats. This utility is specifically created to address gaps in administrative metadata that might not be automatically created by a software platform, and specifically seeks to address the following:
+ Unambigious assertion of whether the resource is born digital or digitized
+ Rights related information about the resource, such as if the intellectual content is in the public domain or protected by copyright
+ Information about any digital preservation activities happening outside the software platform, such as manual migrations
The graphical utility was created to make the creation of these records easier and more approachable for librarians, archivists, and other cultural heritage workers that may not be comfortable in the command line or know Python. The overall workflow is that a list of identifiers are provided to the utility, selections are made in the interface and information is provided, and ultimately it spits out XML or JSON files that each have that identifier as the filename. The idea here is that while I don't have any notion what system you might be working within, you should hopefully have a means of using that identifier in the filename to link up or import the metadata into your system.

Currently this utility is only packaged as an .exe for Windows computers. If you are comfortable with some Python you should be able use the raw Python files (after installing the nonstandard Python libraries listed below) to run the graphical utility in a Linux or MacOS environment. If there are Linux/MacOS users out there that would like to help me create packages for those operating systems, I'm super game.

Additionally this utility is designed and meant for a United States locality. A big part of this tool relates to copyright, and while I am not a lawyer and the utility in graphical format or code and the metadata records that it exports absolutely do not constitute legal advice, I do have training in US copyright law and am leveraging that for the tool. I do not however have any non-US copyright training, so this will be of very limited use outside the United States.
# Python Environment and Libraries
The utility was created entirely in Python, specifically version 3.11.7. The list of libraries used in the development was:
+ Standard Python Libraries
  + os
  + json
  + csv
  + webbrowser
  + uuid
+ Nonstandard Python Libraries
  + PySimpleGUI
  + xmltodict
# Interface Overview
This documentation will cover every field and element present in the PREMIS Utility to describe what its purpose is and how to use it properly. One important point to note that will be consistent throughout this documentation: this program does no data validation whatsoever. Whatever you type into a free text field will be entered into the XML/JSON just as you typed it.
## Project Setup
The top section of the utility contains the fields used to set up the metadata creation job before we get into the content be saved in the metadata itself.
### ID CSV
This field contains the path to the CSV file that stores the list of identifiers that will be embedded in the PREMIS metadata as well as act as the filename. You can click on the yellow Browse button to open a file explorer to navigate to the appropriate CSV file to select it and the intput field to the left of the Browse button will then hold the path. The file explorer is set up to only display *.csv files to make it easier to find and navigate to them. The CSV file should be formatted so the identifiers are in the first column of the spreadsheet (A1, A2, A3...).
### Output Folder
This selects where you would like the newly created PREMIS metadata records to be stored. Similar to the above, you can click on the yellow Browse button to open a folder explorer to navigate to the appropriate folder. When you do, the folder path will appear in the input to the left of the Browse button.
### Encoding for Output
This is a simple dropdown menu that allows the user to toggle between XML and JSON encoding for the created PREMIS metadata records.
### GitHub Repo
This amber button opens up the GitHub repository page for the project (which you are presumably at currently) for easy access to the documentation. This will open the webpage in a new tab of your default browser.
## Origin Tab
The fields present in this tab will not be enabled upton the Enable? checkbox is ticked, indicating that you would like to use this tab. Enabling the tab will allow information to be included on the origin/nature of the digital assets, that is, whether or not they are born digital or digitized resources.
### Born Digital or Digitized
This dropdown menu allows for four options taken from the Metadata Object Description Schema (MODS), specifically the [<digitalOrigin> subelement](https://www.loc.gov/standards/mods/userguide/physicaldescription.html#digitalorigin) of the <physicalDescription> element, and uses these terms as a controlled vocabulary. The definitions of the terms are:
+ born digital – A resource was created in digital form and is intended to remain in digital form.
+ reformatted digital – A resource that was created by digitizing an original analog resource.
+ digitized microfilm – A resource that was created by digitizing a microform.
+ digitized other analog – A resource that was created by digitizing a non-original, second-generation type analog resource, such as a photocopy.
### Date Created
The Origin tab is simply a specficially targetted use case of the PREMIS *event* schema (more generalized use of PREMIS events available in the **Actions** tab), in this case the *creation* event. While clicking on the "Date Picker" button will pop up a small calendar utility letting you click on a specific day, this can be whatever you want with whatever desired level of granularity, though ISO 8601 is always recommended. If you don't have a specific day (YYYY-MM-DD) then using YYYY-MM or YYYY is advised. Feel free to use ranges as well (though consistency is always your friend).
### Created By
This creates the PREMIS *agent* associated with the *creation* event and gives them the role of *implementor* as pulled from the [**Event Related Agent Role**](https://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole.html) controlled vocabulary. This need not be an individual person, but the more detail entered here the better. For instance locally we include the name of the person, their title, their department, and the overall organization (e.g. John Dewees, Digital Asset Mangement Lead, Digital Initiatves department, River Campus Libraries, University of Rochester). This can also be an outsourced digitization vendor. I strongly recommend you develop a local controlled vocabulary of agent names to utilize for this field, and other similar ones throughout the utility.
## Rights Tab
The fields present in this tab will not be enabled upton the Enable? checkbox is ticked, indicating that you would like to use this tab. Enabling the tab will allow information related to the rights status (meaning the copyright) of the digital asset/intellectual property. This is one of the areas of the utility that is likely to grow over time as more rights-related situations make themselves apparent based on user feedback.
### Rights Basis
There are four situations that can be encoded in PREMIS metadata records using this tool. The *rights basis* is directly drawn from the PREMIS data dictionary, specificically semantic unit **4.1.2 rightsBasis** which utilizes [**Rights Basis**](https://id.loc.gov/vocabulary/preservation/rightsBasis.html) controlled vocabulary. The bulleted list below contains the values you will see in the dropdown menu and parenthetically what controlled vocabulary term they map to.
+ Under Copyright (copyright)
+ Public Domain (copyright)
+ Fair Use (statute)
+ License Agreement (license)
# Known Issues
When hitting the Close Window/"X" button in the top right of the screen, the following error is displayed:
```
Traceback (most recent call last):
  File "premis_utility.py", line 105, in <module>
TypeError: 'NoneType' object is not subscriptable
```
This doesn't affect functionality, but I still need to squash that bug at some point.
