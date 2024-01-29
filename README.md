# Overview
The PREMIS Utilty is a graphical utility used to generate [PREMIS](https://www.loc.gov/standards/premis/) metadata records for use in digital preservation systems and digital asset management systems. Records can be exported in both XML and JSON formats. This utility is specifically created to address gaps in administrative metadata that might not be automatically created by a software platform, and specifically seeks to address the following:
+ Unambigious assertion of whether the resource is born digital or digitized
+ Rights related information about the resource, such as if the intellectual content is in the public domain or protected by copyright
+ Information about any digital preservation activities happening outside the software platform, such as manual migrations

The graphical utility was created to make the creation of these records easier and more approachable for librarians, archivists, and other cultural heritage workers that may not be comfortable in the command line or know Python. The overall workflow is that a list of identifiers are provided to the utility, selections are made in the interface and information is provided, and ultimately it spits out XML or JSON files that each have that identifier as the filename. The idea here is that while I don't have any notion what system you might be working within, you should hopefully have a means of using that identifier in the filename to link up or import the metadata into your system.

Currently this utility is only packaged as an .exe for Windows computers. If you are comfortable with some Python you should be able use the raw Python files (after installing the nonstandard Python libraries listed below) to run the graphical utility in a Linux or MacOS environment. If there are Linux/MacOS users out there that would like to help me create packages for those operating systems, I'm super game.

Additionally this utility is designed and meant for a United States locality. A big part of this tool relates to copyright, and while I am not a lawyer and the utility in graphical format or code and the metadata records that it exports absolutely do not constitute legal advice, I do have training in US copyright law and am leveraging that for the tool. I do not however have any non-US copyright training, so this will be of very limited use outside the United States.

The **premis_generator.py** file is the starting point for this entire project and is a standalone script that can take data from a CSV and input it into a multiline string template in a Python script and spit out PREMIS XML records. It is available for context and should you wish to embed that in your own script work, rather than utilizing a graphical utility.
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
This documentation will cover every field and element present in the PREMIS Utility to describe what its purpose is and how to use it properly. One important point to note, and this will be consistent throughout this documentation: *this program does no data validation whatsoever*. Whatever you type into a free text field will be entered into the XML/JSON just as you typed it.
## Project Setup
The top section of the utility contains the fields used to set up the metadata creation job before we get into the content to be saved in the metadata itself.
### ID CSV
This field contains the path to the CSV file that stores the list of identifiers that will be embedded in the PREMIS metadata as well as acting as the filename. You can click on the yellow Browse button to open a file explorer to navigate to the appropriate CSV file to select it and the intput field to the left of the Browse button will then hold the path. The file explorer is set up to only display *.csv files to make it easier to find and navigate to them. The CSV file should be formatted so the identifiers are in the first column of the spreadsheet (A1, A2, A3...).
### Output Folder
This selects where you would like the newly created PREMIS metadata records to be stored. Similar to the above, you can click on the yellow Browse button to open a folder explorer to navigate to the appropriate folder. When you do, the folder path will appear in the input to the left of the Browse button.
### Encoding for Output
This is a simple dropdown menu that allows the user to toggle between XML and JSON encoding for the created PREMIS metadata records.
### GitHub Repo
This amber button opens up the GitHub repository page for the project (which you are presumably at currently) for easy access to the documentation. This will open the webpage in a new tab of your default browser.
## Origin Tab
The fields present in this tab will not be enabled until the **Enable?** checkbox is ticked, indicating that you would like to use this tab. Enabling the tab will allow information to be included on the origin/nature of the digital assets, that is, whether or not they are born digital or digitized resources. This assigns the PREMIS event type of *creation* which is drawn from the [Event Type](https://id.loc.gov/vocabulary/preservation/eventType.html) controlled vocabulary.
### Born Digital or Digitized
This dropdown menu allows for four options taken from the Metadata Object Description Schema (MODS), specifically the [digitalOrigin subelement](https://www.loc.gov/standards/mods/userguide/physicaldescription.html#digitalorigin) of the physicalDescription element, and uses these terms as a controlled vocabulary. The definitions of the terms are:
+ born digital – A resource was created in digital form and is intended to remain in digital form.
+ reformatted digital – A resource that was created by digitizing an original analog resource.
+ digitized microfilm – A resource that was created by digitizing a microform.
+ digitized other analog – A resource that was created by digitizing a non-original, second-generation type analog resource, such as a photocopy.
### Date Created
The Origin tab is simply a specficially targetted use case of the PREMIS *event* schema (more generalized use of PREMIS events available in the **Actions** tab), in this case the *creation* event. While clicking on the "Date Picker" button will pop up a small calendar utility letting you click on a specific day, this can be whatever you want with whatever desired level of granularity, though ISO 8601 is always recommended. If you don't have a specific day (YYYY-MM-DD) then using YYYY-MM or YYYY is advised. Feel free to use ranges as well (though consistency is always your friend).
### Created By
This creates the PREMIS *agent* associated with the *creation* event and gives them the role of *implementer* as pulled from the [**Event Related Agent Role**](https://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole.html) controlled vocabulary. This need not be an individual person, but the more detail entered here the better. For instance locally we include the name of the person, their title, their department, and the overall organization (e.g. John Dewees, Digital Asset Mangement Lead, Digital Initiatves department, River Campus Libraries, University of Rochester). This can also be an outsourced digitization vendor. I strongly recommend you develop a local controlled vocabulary of agent names to utilize for this field, and other similar ones throughout the utility.
## Rights Tab
The fields present in this tab will not be enabled until the **Enable?** checkbox is ticked, indicating that you would like to use this tab. Enabling the tab will allow information related to the rights status (meaning the copyright) of the digital asset/intellectual property. This is one of the areas of the utility that is likely to grow over time as more rights-related situations make themselves apparent based on user feedback.
### Rights Basis
There are four situations that can be encoded in PREMIS metadata records using this tool. The *rights basis* is directly drawn from the PREMIS data dictionary, specificically semantic unit **4.1.2 rightsBasis** which utilizes the [**Rights Basis**](https://id.loc.gov/vocabulary/preservation/rightsBasis.html) controlled vocabulary. The bulleted list below contains the values you will see in the dropdown menu and parenthetically what controlled vocabulary term they map to.
+ Under Copyright (copyright) - Use of this option indicates that the intellecutal property represented in the digital assets are currently protected by copyright in the United States and the metadata record will include a link to the [In Copyright RightsStatement](http://rightsstatements.org/vocab/InC/1.0/).
+ Public Domain (copyright) - Use of this option indicates that the intellectual property represented in the digital assets has either fallen into the public domain in the United States after copyright protection has lapsed, or been dedicated to the public domain via a [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/). A link to the [No Copyright - United States RightsStatement](http://rightsstatements.org/vocab/NoC-US/1.0) is included in the metadata record.
+ Fair Use (statute) - Use of this option indicates that the intellectual property represented in the digital assets are currently protected by copyright, but they are in some way being shared or copied in a fashion not otherwise enshrined as an exception in the Copyright Act and as such a fair use justification is being utilized. The metadata record will include a link to the [In Copyright RightsStatement](http://rightsstatements.org/vocab/InC/1.0/)
+ License Agreement (license) - Use of this option indicates that the intellectual property is still protected by copyright, but the custodial organization has a licensed or contractual right to preserve, share, or otherwise work with the digital assets. The metadata record will include a link to the [In Copyright RightsStatement](http://rightsstatements.org/vocab/InC/1.0/)
### Date Determined
This field allows the inclusion of a specific or approximate date on which the copyright status of the intellectual content was determined. While clicking on the "Date Picker" button will pop up a small calendar utility letting you click on a specific day, this can be whatever you want with whatever desired level of granularity, though ISO 8601 is always recommended. If you don't have a specific day (YYYY-MM-DD) then using YYYY-MM or YYYY is advised. Feel free to use ranges as well (though consistency is always your friend). This field is not used for the *License Agreement* Rights Basis.
### Terms
This field is only used with the *License Agreement* Rights Basis. A summary of the associated license or contract should be included here to provide a broad understanding of why the resources are in the organization's custody and what they are permitted to do with them.
### Notes
This field can be used with all the Rights Bases, and should at a minimum link out to more robust documentation that can discuss the copyright status of a work. This might include a reference to the research completed to determine that a work is still under copyright or in the public domain, to the license agreement, and to the fair use calcuation. This is a bit of a kludge in the case of linking out to the license agreement. Technically speaking the metadata field being used to link out to the *In Copyright* RightsStatement is being repurposed and should link out to the license documentation and its associated identifier. Instead we recommend keeping this information in the Notes field. Real metadata librarians out there, feel free to @ me to let me know how I can do this better.
### Determined By
This creates the PREMIS *agent* associated with the person specifically doing this copyright evaluation and work. If you have a copyright librarian at your org, *their* name should be used here if it is different than the person mashing the **Generate PREMIS Records** button in this utility. It gives them the role of *implementer* as pulled from the [**Event Related Agent Role**](https://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole.html) controlled vocabulary. This need not be an individual person, but the more detail entered here the better. For instance locally we include the name of the person, their title, their department, and the overall organization (e.g. John Dewees, Digital Asset Mangement Lead, Digital Initiatves department, River Campus Libraries, University of Rochester). This could also link out to a department for instance. I strongly recommend you develop a local controlled vocabulary of agent names to utilize for this field, and other similar ones throughout the utility.
## Actions Tab
The fields present in this tab will not be enabled until the **Enable?** checkbox is ticked, indicating that you would like to use this tab. Enabling the tab will allow information related to any preservation actions that are happening outside your preservation software/platform/environment and thus will not be captured in automated histories or logs.
### Event Type
This is a very long list of possible preservation activities starting with *accession* and ending with *virus check* that is drawn from the [Event Type](https://id.loc.gov/vocabulary/preservation/eventType.html) controlled vocabulary. The only option omitted is *creation* as that has its own dedicated tab in the PREMIS utility.
### Notes
This is where as much information about the preservation activity as the user wants can be entered. This might include virtualization environments, software/hardware specifications, reasoning for why the action didn't take place in the relevant preservation system, and any other narrative information that will help preservationists in the future.
### Date Executed
This field allows the inclusion of a specific or approximate date on which the preservation action was taken. While clicking on the "Date Picker" button will pop up a small calendar utility letting you click on a specific day, this can be whatever you want with whatever desired level of granularity, though ISO 8601 is always recommended. If you don't have a specific day (YYYY-MM-DD) then using YYYY-MM or YYYY is advised. Feel free to use ranges as well (though consistency is always your friend).
### Executed By
This creates the PREMIS *agent* associated with the person specifically doing the preservation action. This need not be an individual person, but the more detail entered here the better. For instance locally we include the name of the person, their title, their department, and the overall organization (e.g. John Dewees, Digital Asset Mangement Lead, Digital Initiatves department, River Campus Libraries, University of Rochester). This could also link out to a department for instance. I strongly recommend you develop a local controlled vocabulary of agent names to utilize for this field, and other similar ones throughout the utility.
### Role
This allows greater specification in who or what executed the preservation action. The options are drawn from the [**Event Related Agent Role**](https://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole.html) controlled vocabulary. Whereas all the other agents in the previous tabs are assumed to be *implementers* this allows for the options of an *authorizer*, *executing program*, or *validator* as well. When in doubt, go with *implementer*.
## Project Run
The bottom of the PREMIS Utility is where you will actually start the metadata creation process and will provide live feedback as records are generated.
### Generate PREMIS Records
Hitting this button will start the metadata generation process and start spitting out PREMIS records. Once the process completes a popup will appear letting the user know how many records were created and where they were output to.
### Progress Bar
The rectangle to the right of the *Generate PREMIS Records* button is a progross bar that will fill up with an amber colored bar as records are created. It will turn green when complete.
### About
This button will display a popup showing the name of the creator, the version of the software, the last date the software was updated, and contact informaton for the creator.
### Exit
This button will exit the program.
### Status Bar
This utility-wide rectangle will update to show which record is being created as they are created after hitting the *Generate PREMIS Records* button.
# Output Examples
70ed50ef-923b-4c7c-9ffd-9d6c056d3474.xml
```
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd" version="3.0">
    <premis:object xsi:type="premis:intellectualEntity">
        <premis:objectIdentifier>
            <premis:objectIdentifierType>system_identifier</premis:objectIdentifierType>
            <premis:objectIdentifierValue>70ed50ef-923b-4c7c-9ffd-9d6c056d3474</premis:objectIdentifierValue>
        </premis:objectIdentifier>
    </premis:object>
	<premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>event_uuid</premis:eventIdentifierType>
            <premis:eventIdentifierValue>f49af9a1-0817-4266-a7bd-16922baadcd2</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>creation</premis:eventType>
        <premis:eventDateTime>2021-12-08</premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>reformatted digital</premis:eventDetail>
        </premis:eventDetailInformation>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>Jane Smith, A/V Preservation Librarian, Special Collections, University of Old York</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>70ed50ef-923b-4c7c-9ffd-9d6c056d3474</premis:linkingObjectIdentifierValue>
        </premis:linkingObjectIdentifier>
    </premis:event>
	<premis:rights>
        <premis:rightsStatement>
            <premis:rightsStatementIdentifier>
                <premis:rightsStatementIdentifierType>event_uuid</premis:rightsStatementIdentifierType>
                <premis:rightsStatementIdentifierValue>c1872789-3c69-447f-a257-b99a5c63f1be</premis:rightsStatementIdentifierValue>
            </premis:rightsStatementIdentifier>
            <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">copyright</premis:rightsBasis>
            <premis:copyrightInformation>
                <premis:copyrightStatus>publicdomain</premis:copyrightStatus>
                <premis:copyrightJurisdiction>us</premis:copyrightJurisdiction>
                <premis:copyrightStatusDeterminationDate>2024-01-02</premis:copyrightStatusDeterminationDate>
                <premis:copyrightNote>This work was determined to have fallen into the public domain on January 1, 2021 due to the passage of 70 years past the creators death. Please find more information on this determination in the relevant documentation: copyright_determination_205468.docx</premis:copyrightNote>
                <premis:copyrightDocumentationIdentifier>
                    <premis:copyrightDocumentationIdentifierType>Rights Statement: No Copyright - United States</premis:copyrightDocumentationIdentifierType>
                    <premis:copyrightDocumentationIdentifierValue>http://rightsstatements.org/vocab/NoC-US/1.0/</premis:copyrightDocumentationIdentifierValue>
                </premis:copyrightDocumentationIdentifier>
            </premis:copyrightInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>Trudy Mills, Copyright Librarian, Copyright Clearance Center, University of Old York</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>70ed50ef-923b-4c7c-9ffd-9d6c056d3474</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:rightsStatement>
    </premis:rights>
	<premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>event_uuid</premis:eventIdentifierType>
            <premis:eventIdentifierValue>dfce32dc-c0ea-4433-a5b0-568a95a49128</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>normalization</premis:eventType>
        <premis:eventDateTime>2024-01-20</premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>These files were normalized manually from a proprietary video format into standard uncompressed video files.</premis:eventDetail>
        </premis:eventDetailInformation>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>Stacy Archer, Digital Preservation Librarian, Digital Initiatives Department, University of Old York</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>70ed50ef-923b-4c7c-9ffd-9d6c056d3474</premis:linkingObjectIdentifierValue>
        </premis:linkingObjectIdentifier>
    </premis:event>
</premis:premis>
```
70ed50ef-923b-4c7c-9ffd-9d6c056d3474.json
```
{
    "http://www.loc.gov/premis/v3:premis": {
        "@http://www.w3.org/2001/XMLSchema-instance:schemaLocation": "http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd",
        "@version": "3.0",
        "@xmlns": {
            "premis": "http://www.loc.gov/premis/v3",
            "xlink": "http://www.w3.org/1999/xlink",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance"
        },
        "http://www.loc.gov/premis/v3:object": {
            "@http://www.w3.org/2001/XMLSchema-instance:type": "premis:intellectualEntity",
            "http://www.loc.gov/premis/v3:objectIdentifier": {
                "http://www.loc.gov/premis/v3:objectIdentifierType": "system_identifier",
                "http://www.loc.gov/premis/v3:objectIdentifierValue": "70ed50ef-923b-4c7c-9ffd-9d6c056d3474"
            }
        },
        "http://www.loc.gov/premis/v3:event": [
            {
                "http://www.loc.gov/premis/v3:eventIdentifier": {
                    "http://www.loc.gov/premis/v3:eventIdentifierType": "event_uuid",
                    "http://www.loc.gov/premis/v3:eventIdentifierValue": "2294cb91-e474-47bb-8627-21a2277b1aa4"
                },
                "http://www.loc.gov/premis/v3:eventType": "creation",
                "http://www.loc.gov/premis/v3:eventDateTime": "2021-12-08",
                "http://www.loc.gov/premis/v3:eventDetailInformation": {
                    "http://www.loc.gov/premis/v3:eventDetail": "reformatted digital"
                },
                "http://www.loc.gov/premis/v3:linkingAgentIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierType": "local",
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierValue": "Jane Smith, A/V Preservation Librarian, Special Collections, University of Old York",
                    "http://www.loc.gov/premis/v3:linkingAgentRole": {
                        "@authority": "eventRelatedAgentRole",
                        "@authorityURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole",
                        "@valueURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp",
                        "#text": "implementer"
                    }
                },
                "http://www.loc.gov/premis/v3:linkingObjectIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierType": "system_identifier",
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierValue": "70ed50ef-923b-4c7c-9ffd-9d6c056d3474"
                }
            },
            {
                "http://www.loc.gov/premis/v3:eventIdentifier": {
                    "http://www.loc.gov/premis/v3:eventIdentifierType": "event_uuid",
                    "http://www.loc.gov/premis/v3:eventIdentifierValue": "b9de946d-267b-4c5b-a6ee-3ad689d38494"
                },
                "http://www.loc.gov/premis/v3:eventType": "normalization",
                "http://www.loc.gov/premis/v3:eventDateTime": "2024-01-20",
                "http://www.loc.gov/premis/v3:eventDetailInformation": {
                    "http://www.loc.gov/premis/v3:eventDetail": "These files were normalized manually from a proprietary video format into standard uncompressed video files."
                },
                "http://www.loc.gov/premis/v3:linkingAgentIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierType": "local",
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierValue": "Stacy Archer, Digital Preservation Librarian, Digital Initiatives Department, University of Old York",
                    "http://www.loc.gov/premis/v3:linkingAgentRole": {
                        "@authority": "eventRelatedAgentRole",
                        "@authorityURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole",
                        "@valueURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp",
                        "#text": "implementer"
                    }
                },
                "http://www.loc.gov/premis/v3:linkingObjectIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierType": "system_identifier",
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierValue": "70ed50ef-923b-4c7c-9ffd-9d6c056d3474"
                }
            }
        ],
        "http://www.loc.gov/premis/v3:rights": {
            "http://www.loc.gov/premis/v3:rightsStatement": {
                "http://www.loc.gov/premis/v3:rightsStatementIdentifier": {
                    "http://www.loc.gov/premis/v3:rightsStatementIdentifierType": "event_uuid",
                    "http://www.loc.gov/premis/v3:rightsStatementIdentifierValue": "ed9190da-ac9e-4017-b78d-6bd1b346f262"
                },
                "http://www.loc.gov/premis/v3:rightsBasis": {
                    "@authority": "rightsBasis",
                    "@authorityURI": "http://id.loc.gov/vocabulary/preservation/rightsBasis",
                    "@valueURI": "http://id.loc.gov/vocabulary/preservation/rightsBasis/cop",
                    "#text": "copyright"
                },
                "http://www.loc.gov/premis/v3:copyrightInformation": {
                    "http://www.loc.gov/premis/v3:copyrightStatus": "publicdomain",
                    "http://www.loc.gov/premis/v3:copyrightJurisdiction": "us",
                    "http://www.loc.gov/premis/v3:copyrightStatusDeterminationDate": "2024-01-02",
                    "http://www.loc.gov/premis/v3:copyrightNote": "This work was determined to have fallen into the public domain on January 1, 2021 due to the passage of 70 years past the creators death. Please find more information on this determination in the relevant documentation: copyright_determination_205468.docx",
                    "http://www.loc.gov/premis/v3:copyrightDocumentationIdentifier": {
                        "http://www.loc.gov/premis/v3:copyrightDocumentationIdentifierType": "Rights Statement: No Copyright - United States",
                        "http://www.loc.gov/premis/v3:copyrightDocumentationIdentifierValue": "http://rightsstatements.org/vocab/NoC-US/1.0/"
                    }
                },
                "http://www.loc.gov/premis/v3:linkingAgentIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierType": "local",
                    "http://www.loc.gov/premis/v3:linkingAgentIdentifierValue": "Trudy Mills, Copyright Librarian, Copyright Clearance Center, University of Old York",
                    "http://www.loc.gov/premis/v3:linkingAgentRole": {
                        "@authority": "eventRelatedAgentRole",
                        "@authorityURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole",
                        "@valueURI": "http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp",
                        "#text": "implementer"
                    }
                },
                "http://www.loc.gov/premis/v3:linkingObjectIdentifier": {
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierType": "system_identifier",
                    "http://www.loc.gov/premis/v3:linkingObjectIdentifierValue": "70ed50ef-923b-4c7c-9ffd-9d6c056d3474"
                }
            }
        }
    }
}
```
# Known Issues
Ongoing issues and enhancements that need to be added are listed below to let folks know what is on the roadmap.
## Hitting the X Button
When hitting the Close Window/"X" button in the top right of the screen, the following error is displayed:
```
Traceback (most recent call last):
  File "premis_utility.py", line 105, in <module>
TypeError: 'NoneType' object is not subscriptable
```
This doesn't affect functionality, but I still need to squash that bug at some point.
## Basic Input Validation
The PREMIS Utility will run just fine even if no options are selected, input fields have content, or even an encoding schema is selected. The resulting files will not be particularly useful, but they will be created nonetheless. Including some basic validation to throw up a warning if you click to enable one of the tabs but don't bother to input any data is probably a good idea. If you don't include the path to the CSV file the program just throws up an error and crashes. If you don't include the path to an output folder, it puts the metadata files in the same place you have the program executable itself stored. None of this is ideal and should be handled better in future releases.
