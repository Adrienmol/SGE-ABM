# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tarea01abm(models.Model):
#     _name = 'tarea01abm.tarea01abm'
#     _description = 'tarea01abm.tarea01abm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

