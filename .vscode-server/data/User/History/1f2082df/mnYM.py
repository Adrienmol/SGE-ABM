# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesores(models.Model):
    _name = 'tarea04abm.profesores'
    _description = 'tarea04abm.profesores'

    _rec_name = 'nombreProfesor'

    nombreProfesor = fields.Char("Nombre")