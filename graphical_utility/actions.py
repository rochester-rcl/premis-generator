import uuid

def action_enable(event_type, event_info, date_executed, date_executed_button, executer, role):
    event_type.update(disabled=False)
    event_info.update(disabled=False)
    date_executed.update(disabled=False)
    date_executed_button.update(disabled=False)
    executer.update(disabled=False)
    role.update(disabled=False)

def action_disable(event_type, event_info, date_executed, date_executed_button, executer, role):
    event_type.update(disabled=True)
    event_info.update(disabled=True)
    date_executed.update(disabled=True)
    date_executed_button.update(disabled=True)
    executer.update(disabled=True)
    role.update(disabled=True)

def premis_action_generate(event_type_value, event_info_value, date_executed_value, executor_value, role_value, id):
    action_uuid = uuid.uuid4()
    premis_action = '''\t<premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>event_uuid</premis:eventIdentifierType>
            <premis:eventIdentifierValue>{action_uuid}</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>{event_type}</premis:eventType>
        <premis:eventDateTime>{datetime}</premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>{event_info}</premis:eventDetail>
        </premis:eventDetailInformation>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">{role}</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
        </premis:linkingObjectIdentifier>
    </premis:event>\n'''.format(action_uuid=action_uuid, event_type=event_type_value, datetime=date_executed_value, event_info=event_info_value, agent=executor_value, role=role_value, system_identifier=id)
    return premis_action