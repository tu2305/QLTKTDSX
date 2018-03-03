# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError


class CongTruong(models.Model):
    _name = 'dm.congtruong'
    _inherit = 'mail.thread'
    _description = 'DM CongTruong'
    _rec_name = 'tenCT'

    tenCT = fields.Char('Tên công trường', size=200, required=True,
                        track_visibility="onchange")
    maCT = fields.Char('Mã công trường', size=30, required=True,
                       track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=1000,
                       track_visibility="onchange")
    nguoiQL = fields.Char('Người quản lý', size=200, required=True, track_visibility="onchange")

    @api.multi
    @api.onchange('maCT')
    def _compute_upper_code(self):
        for record in self:
            if record.maCT:
                maCT = record.maCT
                record.maCT = maCT.upper()

    @api.multi
    @api.constrains('maCT')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.maCT):
                raise ValidationError(_("Mã công trường ko được có kí tự đặc biệt"))
