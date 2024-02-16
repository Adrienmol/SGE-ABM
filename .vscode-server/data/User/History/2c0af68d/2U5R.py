# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medico(models.Model):
   _name = 'tarea03abm.medico'
   _description = 'tarea03abm.medico'

   name = fields.Char("Nombre del médico")
   apellidos = fields.Char("Apellidos del médico")
   ncolegiado = fields.Integer("Número del colegiado")

   #Relación con el modelo "diagnostico".
   diagnostico = fields.One2many("tarea03.diagnostico", "medico")