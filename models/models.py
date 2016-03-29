# -*- coding: utf-8 -*-

from openerp import models, fields, api

class People_List(models.Model):
    _name = 'mfmodoo.people_list'

    surname = fields.Char(string="Фамилия", required=True)
    name = fields.Char(string="Имя", required=True)
    second_name = fields.Char(string="Отчество", required=True)
    born = fields.Date(string="Дата рождения", required=True)
    department_id = fields.Many2one('mfmodoo.department_list', ondelete='restrict', string='Отдел', required=True)
    position_id = fields.Many2one('mfmodoo.position_list', ondelete='restrict', string='Должность', required=True)

class Department_List(models.Model):
    _name = 'mfmodoo.department_list'

    name = fields.Char(string='Название Отдела', required=True)
    description = fields.Text()
    people_ids = fields.One2many('mfmodoo.people_list', 'department_id' string='Сотрудники')

class Position_List(models.Model):
    _name = 'mfmodoo.position_list'

    name = fields.Char(string='Должность', required=True)

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
