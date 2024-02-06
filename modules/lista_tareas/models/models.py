# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'
    
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    # Este computo depende de la variable prioridad
    @api.depends('prioridad')
    
    # Funcion para calcular el valor de urgente
    def _value_urgente(self):
        # Para cada registro
        for record in self:
            # Si la prioridad es mayor que 30, se considera urgente, en otro caso no lo es
            if record.prioridad > 30:
                record.urgente = True
            else:
                record.urgente = False
