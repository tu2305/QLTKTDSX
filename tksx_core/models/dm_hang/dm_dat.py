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


class Dat(models.Model):
    _name = 'dm.dat'
    _inherit = 'mail.thread'
    _description = 'Đất'
    _rec_name = 'ten_dat'

    ma_dat = fields.Char('Mã đất', required=True, track_visibility='onchange')
    ten_dat = fields.Char('Tên đất', required=True, track_visibility='onchange')
    ti_trong = fields.Char('Tỉ trọng', required=True, track_visibility='onchange')
    mo_ta = fields.Text('Mô tả', size=300, track_visibility='onchange')

    @api.multi
    @api.onchange('ma_dat')
    def _compute_upper_code(self):
        for record in self:
            if record.ma_dat:
                ma_dat = record.ma_dat
                record.ma_dat = ma_dat.upper()

    @api.multi
    @api.constrains('ma_dat')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.ma_dat):
                raise ValidationError(_("Mã đất chỉ gồm chữ, số hoặc dấu _"))

    _sql_constraints = [('unique_ma_dat', 'unique(ma_dat)', 'Đã tồn tại mã đất!')]
