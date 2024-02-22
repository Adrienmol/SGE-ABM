# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ciclos(models.Model):
    _name = 'tarea04abm.ciclos'
    _description = 'tarea04abm.ciclos'

    # Al no tener un "name", odoo usará el valor dado aquí:
    _rec_name = 'nombreCiclo'

    nombreCiclo = fields.Char("Nombre")
    modulosAsociados= fields.One2many(tarea04abm.)

