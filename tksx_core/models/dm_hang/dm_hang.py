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


class Hang(models.Model):
    _name = 'dm.hang'
    _inherit = 'mail.thread'
    _description = 'Hàng'
    _rec_name = 'ten_hang'

    ma_hang = fields.Char('Mã hàng', required=True, track_visibility='onchange')
    ten_hang = fields.Char('Tên hàng', required=True, track_visbility='onchange')
    ma_dat = fields.Many2one('dm.dat', 'Đất', track_visibility='onchange')
    ma_than = fields.Many2one('dm.than', 'Than', track_visibility='onchange')
    ma_thai = fields.Many2one('dm.thai', 'Thải', track_visibility='onchange')
    mo_ta = fields.Text('Mô tả', track_visibility='onchange')

    @api.multi
    @api.onchange('ma_hang')
    def _compute_upper_code(self):
        for record in self:
            if record.ma_hang:
                ma_hang = record.ma_hang
                record.ma_hang = ma_hang.upper()

    @api.multi
    @api.constrains('ma_hang')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.ma_hang):
                raise ValidationError(_("Mã hàng chỉ gồm chữ, số hoặc dấu _"))

    _sql_constraints = [('unique_ma_hang', 'unique(ma_hang)', 'Đã tồn tại mã hàng!')]
