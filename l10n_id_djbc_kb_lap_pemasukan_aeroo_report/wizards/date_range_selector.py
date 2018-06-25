# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class KBLapPemasukanWizard(models.TransientModel):
    _inherit = "l10n_id.kb_lap_pemasukan_wizard"

    @api.multi
    def action_print_xls(self):
        datas = {}
        datas['form'] = self.read()[0]
        return {
            'type': 'ir.actions.report.xml',
            'report_name': "aeroo_reportLapPemasukanXls",
            'datas': datas,
        }

    @api.multi
    def action_print_ods(self):
        datas = {}
        datas['form'] = self.read()[0]
        return {
            'type': 'ir.actions.report.xml',
            'report_name': "aeroo_reportLapPemasukanOds",
            'datas': datas,
        }
