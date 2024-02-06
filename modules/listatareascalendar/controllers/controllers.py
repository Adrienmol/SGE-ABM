# -*- coding: utf-8 -*-
# from odoo import http


# class Listatareascalendar(http.Controller):
#     @http.route('/listatareascalendar/listatareascalendar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/listatareascalendar/listatareascalendar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('listatareascalendar.listing', {
#             'root': '/listatareascalendar/listatareascalendar',
#             'objects': http.request.env['listatareascalendar.listatareascalendar'].search([]),
#         })

#     @http.route('/listatareascalendar/listatareascalendar/objects/<model("listatareascalendar.listatareascalendar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('listatareascalendar.object', {
#             'object': obj
#         })

