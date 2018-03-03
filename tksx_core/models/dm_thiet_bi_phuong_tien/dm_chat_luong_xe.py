# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError

class ChatLuongXe(models.Model):
    _name = 'dm.chatluongxe'
    _inherit = 'mail.thread'
    _description = 'DM ChatLuongXe'
    _rec_name = 'maTT'
    maTT = fields.Char('Mã tình trạng xe', size=200, required=True,
                     track_visibility="onchange")
    heSoCL = fields.Char('Hệ số chất lượng', size=200,required=True, track_visibility="onchange")
    heSoHM = fields.Char('Hệ số hao mòn', size=200,required=True, track_visibility="onchange")
    maDM = fields.Many2one('dm.nhienlieu', 'Định mức nhiên liệu', required=True, track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=200, track_visibility="onchange")

    @api.multi
    @api.onchange('maTT')
    def _compute_upper_code(self):
        for record in self:
            if record.maTT:
                maTT = record.maTT
                record.maTT = maTT.upper()

    @api.multi
    @api.constrains('maTT')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.maTT):
                raise ValidationError(_("Mã tình trạng xe ko được có kí tự đặc biệt"))