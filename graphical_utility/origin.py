import uuid

def origin_enable(bd_digit, date_created, date_created_button, creator):
    bd_digit.update(disabled=False)
    date_created.update(disabled=False)
    date_created_button.update(disabled=False)
    creator.update(disabled=False)

def origin_disable(bd_digit, date_created, date_created_button, creator):
    bd_digit.update(disabled=True)
    date_created.update(disabled=True)
    date_created_button.update(disabled=True)
    creator.update(disabled=True)

def premis_origin_generate(id, bd_digit_value, date_created_value, creator_value):
    origin_uuid = uuid.uuid4()
    premis_origin = '''\t<premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>event_uuid</premis:eventIdentifierType>
            <premis:eventIdentifierValue>{origin_uuid}</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>creation</premis:eventType>
        <premis:eventDateTime>{datetime}</premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>{bd_digit}</premis:eventDetail>
        </premis:eventDetailInformation>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
        </premis:linkingObjectIdentifier>
    </premis:event>\n'''.format(origin_uuid=origin_uuid, datetime=date_created_value, bd_digit=bd_digit_value, agent=creator_value, system_identifier=id)
    return premis_origin
