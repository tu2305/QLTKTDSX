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


class DiaDiemChatTai(models.Model):
    _name = 'dm.chattai'
    _inherit = 'mail.thread'
    _description = 'Địa Điểm Chất Tải'
    _rec_name = 'ten_chat_tai'

    ma_chat_tai = fields.Char('Mã', required=True, track_visibility='onchange')
    ten_chat_tai = fields.Char('Tên', required=True, track_visibility='onchange')
    cao_do = fields.Integer('Cao độ', required=True, track_visibility='onchange')
    ma_via = fields.Many2one('dm.via', 'Vỉa', track_visibility='onchange')
    ma_tang = fields.Many2one('dm.tang', 'Tầng', domain="[('ma_via','=',ma_via)]", track_visibility='onchange')
    mo_ta = fields.Text('Mô tả', size=300, track_visibility='onchange')

    @api.multi
    @api.onchange('ma_via')
    def _check_via(self):
        self.ma_tang = False

    @api.multi
    @api.onchange('ma_tang')
    def _check_tang(self):
        self.cao_do = self.ma_tang.cao_do

    @api.multi
    @api.onchange('ma_chat_tai')
    def _compute_upper_code(self):
        for record in self:
            if record.ma_chat_tai:
                ma_chat_tai = record.ma_chat_tai
                record.ma_chat_tai = ma_chat_tai.upper()

    @api.multi
    @api.constrains('ma_chat_tai')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.ma_chat_tai):
                raise ValidationError(_("Mã địa điểm chất tải chỉ gồm chữ, số hoặc dấu _"))

    _sql_constraints = [('unique_ma_chat_tai', 'unique(ma_chat_tai)', 'Đã tồn tại mã địa điểm chất tải!')]
