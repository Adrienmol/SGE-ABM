# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea01abm(http.Controller):
#     @http.route('/tarea01abm/tarea01abm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea01abm/tarea01abm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea01abm.listing', {
#             'root': '/tarea01abm/tarea01abm',
#             'objects': http.request.env['tarea01abm.tarea01abm'].search([]),
#         })

#     @http.route('/tarea01abm/tarea01abm/objects/<model("tarea01abm.tarea01abm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea01abm.object', {
#             'object': obj
#         })

