# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Quality Manual',
    'version': '1.0',
    'category': 'Management System',
    'complexity': "easy",
    'description': """
Quality Manual Template.
========================

It provides the Wiki Category and a Wiki Page
for the Quality Manual.
    """,
    'author': "OpenERP SA,Odoo Community Association (OCA)",
    'website': 'http://openerp.com',
    'license': 'AGPL-3',
    'depends': ['mgmtsystem_manuals'],
    'data': ['document_page_quality_manual.xml'],
    'demo': [],
    'installable': False,
    'auto_install': False,
    'certificate': '',
    'images': ['images/wiki_pages_quality_manual.jpeg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
