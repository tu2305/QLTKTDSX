# -*- coding: utf-8 -*-
###############################################################################
#
#    Công ty giải pháp phần mềm VNITPro.
#    Copyright (C) 2018-TODAY VNITPro(<http://vnitpro.vn>).
#
###############################################################################

{
    'name': 'TKSX Core',
    'description': 'Quản lý thống kê theo dõi sản xuất chung',
    'summary': 'Quản lý thống kê theo dõi sản xuất công ty than',
    'category': 'Website',
    "sequence": 3,
    'version': '1.0.0',
    'author': 'VNITPro',
    'website': 'http://vnitpro.vn',
    'data': [
        'views/dm_dia_diem_lam_viec/dm_via_view.xml',
        'views/dm_dia_diem_lam_viec/dm_tang_view.xml',
        'views/dm_dia_diem_lam_viec/dm_bai_thai_view.xml',
        'views/dm_dia_diem_lam_viec/dm_chat_tai_view.xml',
        'views/dm_dia_diem_lam_viec/dm_ha_tai_view.xml',
        'views/dm_dia_diem_lam_viec/dm_che_bien_view.xml',
        'views/dm_hang/dm_hang_view.xml',
        'views/dm_hang/dm_dat_view.xml',
        'views/dm_hang/dm_thai_view.xml',
        'views/dm_hang/dm_than_view.xml',
        'views/dm_cong_truong/dm_cong_truong_view.xml',
        'views/dm_cong_truong/dm_nhan_su_view.xml',
        'views/dm_cong_truong/dm_phan_xuong_view.xml',
        'views/dm_cong_truong/dm_to_cong_viec_view.xml',
        'views/dm_thiet_bi_phuong_tien/dm_chung_loai_xe_view.xml',
        'views/dm_thiet_bi_phuong_tien/dm_ma_loai_xe_view.xml',
        'views/dm_thiet_bi_phuong_tien/dm_xe_view.xml',
        'views/dm_thiet_bi_phuong_tien/dm_chat_luong_xe_view.xml',
        'views/dm_cong_viec/dm_cong_viec_view.xml',
        'views/dinh_muc/dinh_muc_nhien_lieu_view.xml',
        'menu/danh_muc_menu.xml',
        'menu/dm_cong_truong_menu.xml',
        'menu/dm_thiet_bi_phuong_tien_menu.xml',
        'menu/dinh_muc_menu.xml',
        'menu/dm_dia_diem_lam_viec_menu.xml',
        'menu/dm_hang_menu.xml',
        'menu/dm_cong_viec_menu.xml',
    ],
    'depends': ['base', 'web', 'document', 'board', 'mail'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
