# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class NhienLieu(models.Model):
    _name = 'dm.nhienlieu'
    _inherit = 'mail.thread'
    _description = 'DM NhienLieu'
    _rec_name = 'maDM'
    maDM = fields.Char('Mã định mức nhiên liệu', size=200, required=True,
                     track_visibility="onchange")
    DMDau = fields.Char('Định mức dầu', size=200,required=True, track_visibility="onchange")
    DMGio = fields.Char('Định mức giờ', size=200,required=True, track_visibility="onchange")
    moTa = fields.Text('Mô tả định mức', size=200, track_visibility="onchange")

