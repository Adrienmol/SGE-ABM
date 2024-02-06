# -*- coding: utf-8 -*-
# from odoo import http


# class Comicsavanzada(http.Controller):
#     @http.route('/comicsavanzada/comicsavanzada', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comicsavanzada/comicsavanzada/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comicsavanzada.listing', {
#             'root': '/comicsavanzada/comicsavanzada',
#             'objects': http.request.env['comicsavanzada.comicsavanzada'].search([]),
#         })

#     @http.route('/comicsavanzada/comicsavanzada/objects/<model("comicsavanzada.comicsavanzada"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comicsavanzada.object', {
#             'object': obj
#         })

