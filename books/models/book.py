# -*- coding: utf-8 -*-

from odoo import models, fields


class my_module(models.Model):
    _name = 'book.book'
    name = fields.Char(string="Pavadinimas")
    description = fields.Char(string="Aprašymas")
    company = fields.Many2one('res.company', string="Įmonė")


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
