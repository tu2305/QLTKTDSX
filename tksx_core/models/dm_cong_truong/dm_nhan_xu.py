# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class NhanSu(models.Model):
    _name = 'dm.nhansu'
    _inherit = 'mail.thread'
    _description = 'DM NhanSu'

    soThe = fields.Char('Số thẻ nhân sự', size=200, required=True,
                        track_visibility="onchange")
    tenNS = fields.Char('Tên nhân sự', size=30, required=True,
                        track_visibility="onchange")
    chucVu = fields.Char('Chức vụ', size=200, required=True,
                         track_visibility="onchange")
    heSoLuong = fields.Char('Hệ số lương', size=200, required=True,
                            track_visibility="onchange")
    CMTND = fields.Char('CMTND', size=200, required=True,
                            track_visibility="onchange")
    anh = fields.Binary('Ảnh')
    maCT = fields.Many2one('dm.congtruong', 'Công trường', required=True, track_visibility="onchange")
    maPX = fields.Many2one('dm.phanxuong', 'Phân xưởng', required=True, track_visibility="onchange",domain="[('maCT' , '=', maCT)]")
    maTo = fields.Many2one('dm.tocongviec', 'Tổ', required=True, track_visibility="onchange",domain="[('maPX' , '=', maPX)]")
    moTa = fields.Text('Mô tả', size=200,track_visibility="onchange")

    @api.onchange('maCT')
    def _change_maCT(self):
        self.maPX = False

    @api.onchange('maPX')
    def _change_maPX(self):
            self.maTo = False