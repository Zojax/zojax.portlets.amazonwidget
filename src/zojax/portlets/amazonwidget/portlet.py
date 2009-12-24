##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from interfaces import _
from zojax.statusmessage.interfaces import IStatusMessage


class PortletEdit(object):

    def update(self):
        request = self.request
        context = self.context

        if 'form.add' in request:
            source = request.get('form.amazon.widget', '').strip()

            if not source:
                IStatusMessage(request).add(_("You can't add empty string."))
            else:
                widgets = list(self.context.widgets)
                widgets.append(source)
                self.context.widgets = widgets
                IStatusMessage(request).add(_("Amazon widget has been added."))

        elif 'form.widget.save' in request:
            idx = request.get('widgetIdx')

            source = request.get('form.widget', '').strip()
            if not source:
                IStatusMessage(request).add(_("You can't set empty string."))
            else:
                widgets = list(self.context.widgets)
                widgets[idx] = source
                self.context.widgets = widgets
                IStatusMessage(request).add(_("Amazon widget has been saved."))

        elif 'form.widget.remove' in request:
            idx = request.get('widgetIdx')
            widgets = list(self.context.widgets)
            del widgets[idx]
            self.context.widgets = widgets
            IStatusMessage(request).add(_("Amazon widget has been removed."))
