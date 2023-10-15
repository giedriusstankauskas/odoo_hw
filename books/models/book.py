# -*- coding: utf-8 -*-

from odoo import models, fields


class my_module(models.Model):
    _name = 'book.book'
    name = fields.Char(string="Pavadinimas")
    description = fields.Char(string="Aprašymas")
    company = fields.Many2one('res.company', string="Įmonė")
