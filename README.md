# Overview
The PREMIS Utilty is a graphical utility used to generate [PREMIS](https://www.loc.gov/standards/premis/) metadata records for use in digital preservation systems and digital asset management systems. Records can be exported in both XML and JSON formats. This utility is specifically created to address gaps in administrative metadata that might not be automatically created by a software platform, and specifically seeks to address the following:
+ Unambigious assertion of whether the resource is born digital or digitized
+ Rights related information about the resource, such as if the intellectual content is in the public domain or protected by copyright
+ Information about any digital preservation activities happening outside the software platform, such as manual migrations
The graphical utility was created to make the creation of these records easier and more approachable for librarians, archivists, and other cultural heritage workers that may not be comfortable in the command line or know Python. The overall workflow is that a list of identifiers are provided to the utility and it spits out XML or JSON files that each have that identifier as the filename. The idea here is that while I don't have any notion what system you might be working within, but you should hopefully have a means of using that identifier to link up or import the metadata into your system.
# Python Environment and Libraries
The entire utilility was created entirely in Python, specifically version 3.11.7. The list of libraries used in the development was:
+ Standard Python Libraries
  + os
  + json
  + csv
  + webbrowser
  + uuid
+ Nonstandard Python Libraries
  + PySimpleGUI
  + xmltodict
# 
