import csv
import os
import uuid

fhand = open('project_1.csv', 'r')
csv_reader = csv.reader(fhand, delimiter=',')
count = 0

for row in csv_reader:
    count += 1
    preservica_uuid = row[0]
    rights_uuid = uuid.uuid4()
    rights_basis = row[1]
    rights_status = row[2]
    rights_jurisdiction = row[3]
    rights_date = row[4]
    rights_note = row[5]
    rights_doc_text = row[6]
    rights_doc_uri = row[7]
    event_1_uuid = uuid.uuid4()
    event_1_type = row[8]
    event_1_datetime = row[9]
    event_1_details = row[10]
    event_1_agent = row[11]
    premis = '''<premis:premis xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd" version="3.0">
        <premis:object xsi:type="premis:intellectualEntity">
            <premis:objectIdentifier>
                <premis:objectIdentifierType>preservica_uuid</premis:objectIdentifierType>
                <premis:objectIdentifierValue>{preservica_uuid}</premis:objectIdentifierValue>
            </premis:objectIdentifier>
        </premis:object>
        <premis:rights>
            <premis:rightsStatement>
                <premis:rightsStatementIdentifier>
                    <premis:rightsStatementIdentifierType>rights_uuid</premis:rightsStatementIdentifierType>
                    <premis:rightsStatementIdentifierValue>{rights_uuid}</premis:rightsStatementIdentifierValue>
                </premis:rightsStatementIdentifier>
                <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">{rights_basis}</premis:rightsBasis>
                <premis:copyrightInformation>
                    <premis:copyrightStatus>{rights_status}</premis:copyrightStatus>
                    <premis:copyrightJurisdiction>{rights_jurisdiction}</premis:copyrightJurisdiction>
                    <premis:copyrightStatusDeterminationDate>{rights_date}</premis:copyrightStatusDeterminationDate>
                    <premis:copyrightNote>{rights_note}</premis:copyrightNote>
                    <premis:copyrightDocumentationIdentifier>
                        <premis:copyrightDocumentationIdentifierType>{rights_doc_text}</premis:copyrightDocumentationIdentifierType>
                        <premis:copyrightDocumentationIdentifierValue>{rights_doc_uri}</premis:copyrightDocumentationIdentifierValue>
                    </premis:copyrightDocumentationIdentifier>
                </premis:copyrightInformation>
                <premis:linkingObjectIdentifier>
                    <premis:linkingObjectIdentifierType>preservica_uuid</premis:linkingObjectIdentifierType>
                    <premis:linkingObjectIdentifierValue>{preservica_uuid}</premis:linkingObjectIdentifierValue>
                </premis:linkingObjectIdentifier>
            </premis:rightsStatement>
        </premis:rights>
        <premis:event>
            <premis:eventIdentifier>
                <premis:eventIdentifierType>event_uuid</premis:eventIdentifierType>
                <premis:eventIdentifierValue>{event_1_uuid}</premis:eventIdentifierValue>
            </premis:eventIdentifier>
            <premis:eventType>{event_1_type}</premis:eventType>
            <premis:eventDateTime>{event_1_datetime}</premis:eventDateTime>
            <premis:eventDetailInformation>
                <premis:eventDetail>{event_1_details}</premis:eventDetail>
            </premis:eventDetailInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>{event_1_agent}</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>preservica_uuid</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>{preservica_uuid}</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:event>
    </premis:premis>'''.format(preservica_uuid=preservica_uuid, rights_uuid=rights_uuid, rights_basis=rights_basis, rights_status=rights_status, rights_jurisdiction=rights_jurisdiction, rights_date=rights_date, rights_note=rights_note, rights_doc_text=rights_doc_text, rights_doc_uri=rights_doc_uri, event_1_uuid=event_1_uuid, event_1_type=event_1_type, event_1_datetime=event_1_datetime, event_1_details=event_1_details, event_1_agent=event_1_agent)
    premis_path = os.path.join('project_1', preservica_uuid + '.xml')
    with open(premis_path, 'w') as premis_hand:
        premis_hand.write(premis)
    print('created {}'.format(premis_path))
fhand.close()
print('created {} PREMIS files'.format(count))
