# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea04abm(http.Controller):
#     @http.route('/tarea04abm/tarea04abm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea04abm/tarea04abm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea04abm.listing', {
#             'root': '/tarea04abm/tarea04abm',
#             'objects': http.request.env['tarea04abm.tarea04abm'].search([]),
#         })

#     @http.route('/tarea04abm/tarea04abm/objects/<model("tarea04abm.tarea04abm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea04abm.object', {
#             'object': obj
#         })

