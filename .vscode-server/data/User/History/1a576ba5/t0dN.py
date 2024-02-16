# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class tarea03abm(models.Model):
     _name = 'tarea03abm.paciente'
     _description = 'tarea03abm.paciente'

     name = fields.Char("Nombre del paciente")
     apellidos = fields.Char("Apellidos del paciente")
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

  


