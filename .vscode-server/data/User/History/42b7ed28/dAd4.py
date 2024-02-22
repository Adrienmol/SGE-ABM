# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos(models.Model):
    _name = 'tarea04abm.alumnos'
    _description = 'tarea04abm.alumnos'

    _rec_name = 'nombreAlumno'

    nombreAlumno = fields.Char("Nombre")
    apellidoAlumno = fields.Char("Apellido")