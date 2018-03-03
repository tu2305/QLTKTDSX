# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError

class ChungLoaiXe(models.Model):
    _name = 'dm.chungloaixe'
    _inherit = 'mail.thread'
    _description = 'DM ChungLoaiXe'
    _rec_name = 'ma'

    ma = fields.Char('Mã chủng loại xe', size=200, required=True,
                     track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=1000, track_visibility="onchange")
    @api.multi
    @api.onchange('ma')
    def _compute_upper_code(self):
        for record in self:
            if record.ma:
                ma = record.ma
                record.ma = ma.upper()

    @api.multi
    @api.constrains('maTT')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.ma):
                raise ValidationError(_("Mã chủng loại xe ko được có kí tự đặc biệt"))