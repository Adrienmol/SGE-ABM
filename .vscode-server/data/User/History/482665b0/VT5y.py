# -*- coding: utf-8 -*-

from odoo import models, fields, api


class diagnostico(models.Model):
   _name = 'tarea03abm.diagnostico'
   _description = 'tarea03abm.paciente'

   _rec_name = diagnostico

   diagnostico = fields.Char("Diagnostico")
   medicoatiende = fields.Many2one("")
   pacienteatendido = fields.Text("Síntomas del paciente")