# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError

class PhanXuong(models.Model):
    _name = 'dm.phanxuong'
    _inherit = 'mail.thread'
    _description = 'DM PhanXuong'
    _rec_name = 'tenPX'
    tenPX = fields.Char('Tên phân xưởng', size=200, required=True,
                        track_visibility="onchange")
    maPX = fields.Char('Mã phân xưởng', size=30, required=True,
                       track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=1000,
                       track_visibility="onchange")
    maCT = fields.Many2one('dm.congtruong', 'Công trường', required=True, track_visibility="onchange")
    @api.multi
    @api.onchange('maPX')
    def _compute_upper_code(self):
        for record in self:
            if record.maCT:
                maPX = record.maPX
                record.maCT = maPX.upper()

    @api.multi
    @api.constrains('maPX')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.maPX):
                raise ValidationError(_("Mã phân xưởng ko được có kí tự đặc biệt"))