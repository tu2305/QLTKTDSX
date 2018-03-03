# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Xe(models.Model):
    _name = 'dm.xe'
    _inherit = 'mail.thread'
    _description = 'DM Xe'

    soHieu = fields.Char('Số hiệu xe', size=200, required=True,
                         track_visibility="onchange")
    maXe = fields.Many2one('dm.maloaixe', 'Loại xe', required=True, track_visibility="onchange")
    maTT = fields.Many2one('dm.chatluongxe', 'Tình trạng xe', required=True, track_visibility="onchange")
    tenXe = fields.Char('Tên xe', size=200, required=True,
                        track_visibility="onchange")
    dinhMuc = fields.Many2one('dm.nhienlieu', 'Định mức nhiên liệu', required=True, track_visibility="onchange")
    moTa = fields.Text('Mô tả', size=1000, track_visibility="onchange")
    maCT = fields.Many2one('dm.congtruong', 'Công trường', required=True, track_visibility="onchange")
    maPX = fields.Many2one('dm.phanxuong', 'Phân xưởng', required=True, track_visibility="onchange",
                           domain="[('maCT' , '=', maCT)]")
    maTo = fields.Many2one('dm.tocongviec', 'Tổ', required=True, track_visibility="onchange",
                           domain="[('maPX' , '=', maPX)]")
    anh = fields.Binary('Ảnh xe')

    @api.onchange('maCT')
    def _change_maCT(self):
        self.maPX = False

    @api.onchange('maPX')
    def _change_maPX(self):
        self.maTo = False
