# -*- coding: utf-8 -*-
# from odoo import http


# class Comicssimple(http.Controller):
#     @http.route('/comicssimple/comicssimple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comicssimple/comicssimple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comicssimple.listing', {
#             'root': '/comicssimple/comicssimple',
#             'objects': http.request.env['comicssimple.comicssimple'].search([]),
#         })

#     @http.route('/comicssimple/comicssimple/objects/<model("comicssimple.comicssimple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comicssimple.object', {
#             'object': obj
#         })

