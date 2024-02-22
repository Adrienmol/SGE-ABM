# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos(models.Model):
    _name = 'tarea04abm.alumnos'
    _description = 'tarea04abm.alumnos'

    # Al no tener un "name", odoo usará el valor dado aquí:
    _rec_name = 'nombreAlumno'

    nombreAlumno = fields.Char("Nombre")
    apellidoAlumno = fields.Char("Apellido")