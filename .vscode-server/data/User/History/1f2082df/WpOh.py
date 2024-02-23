# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesores(models.Model):
    _name = 'tarea04abm.profesores'
    _description = 'tarea04abm.profesores'

    # Al no tener un "name", odoo usará el valor dado aquí:
    _rec_name = 'nombreProfesor'

    nombreProfesor = fields.Char("Nombre")
    apellidoProfesor = fields.Char("Apellido")
    modulosImparte = fields.One2many('tarea04abm.modulos', 'profesorImparte')

    alumnosMatriculados = fields.Many2many('tarea04abm.alumnos', related="alumnosMatriculados" ,string="Alumnos")