import uuid

enabled_color = '#7edcf0'
disabled_color = '#6b6565'

def rights_enable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner):
    rights_basis.update(disabled=False)
    date_determ.update(disabled=False)
    date_determ_button.update(disabled=False)
    terms.update(disabled=False)
    rights_notes.update(disabled=False)
    determiner.update(disabled=False)

def rights_disable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner):
    rights_basis.update(disabled=True)
    date_determ.update(disabled=True)
    date_determ_button.update(disabled=True)
    terms.update(disabled=True)
    rights_notes.update(disabled=True)
    determiner.update(disabled=True)

def rights_fields_toggle(rights_basis_value, terms_label, terms, date_determ_label, date_determ, date_determ_button):
    if rights_basis_value == 'Public Domain':
        terms_label.update(text_color=disabled_color)
        terms.update(disabled=True)
        date_determ_label.update(text_color=enabled_color)
        date_determ.update(disabled=False)
        date_determ_button.update(disabled=False)
    elif rights_basis_value == 'Under Copyright':
        terms_label.update(text_color=disabled_color)
        terms.update(disabled=True)
        date_determ_label.update(text_color=enabled_color)
        date_determ.update(disabled=False)
        date_determ_button.update(disabled=False)
    elif rights_basis_value == 'Fair Use':
        terms_label.update(text_color=disabled_color)
        terms.update(disabled=True)
        date_determ_label.update(text_color=enabled_color)
        date_determ.update(disabled=False)
        date_determ_button.update(disabled=False)
    elif rights_basis_value == 'License Agreement':
        terms_label.update(text_color=enabled_color)
        terms.update(disabled=False)
        date_determ_label.update(text_color=disabled_color)
        date_determ.update(disabled=True)
        date_determ_button.update(disabled=True)

def premis_rights_generate(id, rights_basis_value, deter_date_value, note_value, terms_value, determiner_value):
    rights_uuid = uuid.uuid4()
    if rights_basis_value == 'Public Domain':
        premis_rights = '''\t<premis:rights>
        <premis:rightsStatement>
            <premis:rightsStatementIdentifier>
                <premis:rightsStatementIdentifierType>event_uuid</premis:rightsStatementIdentifierType>
                <premis:rightsStatementIdentifierValue>{rights_uuid}</premis:rightsStatementIdentifierValue>
            </premis:rightsStatementIdentifier>
            <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">copyright</premis:rightsBasis>
            <premis:copyrightInformation>
                <premis:copyrightStatus>publicdomain</premis:copyrightStatus>
                <premis:copyrightJurisdiction>us</premis:copyrightJurisdiction>
                <premis:copyrightStatusDeterminationDate>{deter_date}</premis:copyrightStatusDeterminationDate>
                <premis:copyrightNote>{note}</premis:copyrightNote>
                <premis:copyrightDocumentationIdentifier>
                    <premis:copyrightDocumentationIdentifierType>Rights Statement: No Copyright - United States</premis:copyrightDocumentationIdentifierType>
                    <premis:copyrightDocumentationIdentifierValue>http://rightsstatements.org/vocab/NoC-US/1.0/</premis:copyrightDocumentationIdentifierValue>
                </premis:copyrightDocumentationIdentifier>
            </premis:copyrightInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:rightsStatement>
    </premis:rights>\n'''.format(rights_uuid=rights_uuid, deter_date=deter_date_value, note=note_value, agent=determiner_value, system_identifier=id)
        return premis_rights
    elif rights_basis_value == 'Under Copyright':
        premis_rights = '''\t<premis:rights>
        <premis:rightsStatement>
            <premis:rightsStatementIdentifier>
                <premis:rightsStatementIdentifierType>event_uuid</premis:rightsStatementIdentifierType>
                <premis:rightsStatementIdentifierValue>{rights_uuid}</premis:rightsStatementIdentifierValue>
            </premis:rightsStatementIdentifier>
            <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">copyright</premis:rightsBasis>
            <premis:copyrightInformation>
                <premis:copyrightStatus>copyrighted</premis:copyrightStatus>
                <premis:copyrightJurisdiction>us</premis:copyrightJurisdiction>
                <premis:copyrightStatusDeterminationDate>{deter_date}</premis:copyrightStatusDeterminationDate>
                <premis:copyrightNote>{note}</premis:copyrightNote>
                <premis:copyrightDocumentationIdentifier>
                    <premis:copyrightDocumentationIdentifierType>Rights Statement: In Copyright</premis:copyrightDocumentationIdentifierType>
                    <premis:copyrightDocumentationIdentifierValue>http://rightsstatements.org/vocab/InC/1.0/</premis:copyrightDocumentationIdentifierValue>
                </premis:copyrightDocumentationIdentifier>
            </premis:copyrightInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:rightsStatement>
    </premis:rights>\n'''.format(rights_uuid=rights_uuid, deter_date=deter_date_value, note=note_value, agent=determiner_value, system_identifier=id)
        return premis_rights
    elif rights_basis_value == 'Fair Use':
        premis_rights = '''\t<premis:rights>
        <premis:rightsStatement>
            <premis:rightsStatementIdentifier>
                <premis:rightsStatementIdentifierType>event_uuid</premis:rightsStatementIdentifierType>
                <premis:rightsStatementIdentifierValue>{rights_uuid}</premis:rightsStatementIdentifierValue>
            </premis:rightsStatementIdentifier>
            <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">statute</premis:rightsBasis>
            <premis:statuteInformation>
                <premis:statuteJurisdiction>us</premis:statuteJurisdiction>
                <premis:statuteCitation>Copyright Law of the United States (Title 17), Chapter 1: Subject Matter and Scope of Copyright, Section 107. Limitations on exclusive rights: Fair use (https://www.copyright.gov/title17/92chap1.html#107)</premis:statuteCitation>
                <premis:statuteInformationDeterminationDate>{deter_date}</premis:statuteInformationDeterminationDate>
                <premis:statuteNote>{note}</premis:statuteNote>
                <premis:statuteDocumentationIdentifier>
                    <premis:statuteDocumentationIdentifierType>Rights Statement: In Copyright</premis:statuteDocumentationIdentifierType>
                    <premis:statuteDocumentationIdentifierValue>http://rightsstatements.org/vocab/InC/1.0/</premis:statuteDocumentationIdentifierValue>
                </premis:statuteDocumentationIdentifier>
            </premis:statuteInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:rightsStatement>
    </premis:rights>\n'''.format(rights_uuid=rights_uuid, deter_date=deter_date_value, note=note_value, agent=determiner_value, system_identifier=id)
        return premis_rights
    elif rights_basis_value == 'License Agreement':
        premis_rights = '''\t<premis:rights>
        <premis:rightsStatement>
            <premis:rightsStatementIdentifier>
                <premis:rightsStatementIdentifierType>event_uuid</premis:rightsStatementIdentifierType>
                <premis:rightsStatementIdentifierValue>{rights_uuid}</premis:rightsStatementIdentifierValue>
            </premis:rightsStatementIdentifier>
            <premis:rightsBasis authority="rightsBasis" authorityURI="http://id.loc.gov/vocabulary/preservation/rightsBasis" valueURI="http://id.loc.gov/vocabulary/preservation/rightsBasis/cop">license</premis:rightsBasis>
            <premis:licenseInformation>
                <premis:licenseTerms>{terms}</premis:licenseTerms>
                <premis:licenseNote>{note}</premis:licenseNote>
            </premis:licenseInformation>
            <premis:linkingAgentIdentifier>
                <premis:linkingAgentIdentifierType>local</premis:linkingAgentIdentifierType>
                <premis:linkingAgentIdentifierValue>{agent}</premis:linkingAgentIdentifierValue>
                <premis:linkingAgentRole authority="eventRelatedAgentRole" authorityURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole" valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
            </premis:linkingAgentIdentifier>                
            <premis:linkingObjectIdentifier>
                <premis:linkingObjectIdentifierType>system_identifier</premis:linkingObjectIdentifierType>
                <premis:linkingObjectIdentifierValue>{system_identifier}</premis:linkingObjectIdentifierValue>
            </premis:linkingObjectIdentifier>
        </premis:rightsStatement>
    </premis:rights>\n'''.format(rights_uuid=rights_uuid, note=note_value, terms=terms_value, agent=determiner_value, system_identifier=id)
        return premis_rights