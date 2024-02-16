# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea03abm(http.Controller):
#     @http.route('/tarea03abm/tarea03abm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea03abm/tarea03abm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea03abm.listing', {
#             'root': '/tarea03abm/tarea03abm',
#             'objects': http.request.env['tarea03abm.tarea03abm'].search([]),
#         })

#     @http.route('/tarea03abm/tarea03abm/objects/<model("tarea03abm.tarea03abm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea03abm.object', {
#             'object': obj
#         })

