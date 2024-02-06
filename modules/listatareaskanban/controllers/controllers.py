# -*- coding: utf-8 -*-
# from odoo import http


# class Listatareaskanban(http.Controller):
#     @http.route('/listatareaskanban/listatareaskanban', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/listatareaskanban/listatareaskanban/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('listatareaskanban.listing', {
#             'root': '/listatareaskanban/listatareaskanban',
#             'objects': http.request.env['listatareaskanban.listatareaskanban'].search([]),
#         })

#     @http.route('/listatareaskanban/listatareaskanban/objects/<model("listatareaskanban.listatareaskanban"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('listatareaskanban.object', {
#             'object': obj
#         })

