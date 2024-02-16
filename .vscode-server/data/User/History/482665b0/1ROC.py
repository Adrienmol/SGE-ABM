# -*- coding: utf-8 -*-

from odoo import models, fields, api


class diagnostico(models.Model):
   _name = 'tarea03abm.diagnostico'
   _description = 'tarea03abm.paciente'

   _rec_name = diagnostico

   diagnostico = fields.Char("Diagnostico")
   medico = fields.Many2one("tarea03abm.diagnostico")
   paciente = fields.("Síntomas del paciente")