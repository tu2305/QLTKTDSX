# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError

class ToCongViec(models.Model):
    _name = 'dm.tocongviec'
    _inherit = 'mail.thread'
    _description = 'DM ToCongViec'
    _rec_name = 'tenTo'
    maTo = fields.Char('Mã tổ', size=30, required=True,
                       track_visibility="onchange")
    tenTo = fields.Char('Tên tổ', size=200, required=True,
                       track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=1000,
                       track_visibility="onchange")
    maCT = fields.Many2one('dm.congtruong', 'Công trường', required=True, track_visibility="onchange")
    maPX = fields.Many2one('dm.phanxuong', 'Phân xưởng', required=True, track_visibility="onchange",domain="[('maCT' , '=', maCT)]")

    @api.multi
    @api.onchange('maTo')
    def _compute_upper_code(self):
        for record in self:
            if record.maTo:
                maTo = record.maTo
                record.maTo = maTo.upper()

    @api.multi
    @api.constrains('maTo')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.maTo):
                raise ValidationError(_("Mã tổ ko được có kí tự đặc biệt"))

    @api.onchange('maCT')
    def _change_maCT(self):
        self.maPX = False

