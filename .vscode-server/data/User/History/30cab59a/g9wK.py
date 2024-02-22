# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulos(models.Model):
    _name = 'tarea04abm.modulos'
    _description = 'tarea04abm.modulos'

    # Al no tener un "name", odoo usará el valor dado aquí:
    _rec_name = 'nombreModulo'

    nombreModulo = fields.Char("Nombre")
    cicloPertenece = fields.Many2one('tarea04abm.cicloPertenece')
