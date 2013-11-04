# -*- coding: utf-8 -*-
#
# File: duweevent.py
#
# Copyright (c) 2010 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from zope.interface import Interface

from config import *

##code-section module-header #fill in your manual code here
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.base import registerATCT as registerType
from Products.ATContentTypes import ATCTMessageFactory as _
from DateTime import DateTime

##/code-section module-header

schema = Schema((
    LinesField(
        name='event_type',
        vocabulary_expr="""content_instance.getAdapter('portal')().getBrowser('easyvoc').get('duweevent-event_type')""",
        widget=MultiSelectionWidget(
            label='Event type',
            i18n_domain='plone',
        ),
    ),
))

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TCEvent_schema = ATEvent.schema.copy()+schema.copy()

TCEvent_schema.addField(ATFolder.schema['constrainTypesMode'].copy())
TCEvent_schema.addField(ATFolder.schema['nextPreviousEnabled'].copy())

##code-section after-schema #fill in your manual code here
TCEvent_schema['creation_date'].widget.visible={'edit':'visible', 'view':'invisible'}
##/code-section after-schema

class ITCEvent(Interface):
    """ """

class TCEvent(ATFolder,ATEvent):
    """
    """
    security = ClassSecurityInfo()

    implements(ITCEvent)

    meta_type = 'TCEvent'
    _at_rename_after_creation = True

    schema = TCEvent_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(TCEvent, PROJECTNAME)

##code-section module-footer #fill in your manual code here
##/code-section module-footer



