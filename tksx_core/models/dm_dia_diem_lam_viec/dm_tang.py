# -*- coding: utf-8 -*-
###############################################################################
#
#    VNITPro Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY VNITPro(<http://vnitpro.vn>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class Tang(models.Model):
    _name = 'dm.tang'
    _inherit = 'mail.thread'
    _description = 'Via'
    _rec_name = 'ten_tang'

    ma_tang = fields.Char('Mã', required=True, track_visibility='onchange')
    ten_tang = fields.Char('Tên', required=True, track_visibility='onchange')
    ma_via = fields.Many2one('dm.via', 'Vỉa', required=True, track_visibility='onchange')
    cao_do = fields.Integer('Cao độ', required=True, track_visibility='onchange')
    mo_ta = fields.Text('Mô tả', size=300, track_visibility='onchange')

    @api.multi
    @api.onchange('ma_tang')
    def _compute_upper_code(self):
        for record in self:
            if record.ma_tang:
                ma_tang = record.ma_tang
                record.ma_tang = ma_tang.upper()

    @api.multi
    @api.constrains('ma_tang')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.ma_tang):
                raise ValidationError(_("Mã tầng chỉ gồm chữ, số hoặc dấu _"))

    _sql_constraints = [('unique_ma_tang', 'unique(ma_tang)', 'Đã tồn tại mã tầng!')]
