# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
from datetime import date
from datetime import datetime, timedelta
from odoo import fields, models, exceptions, _, api
import logging
_logger = logging.getLogger(__name__)

class HrStandby(models.Model):
    _name = "hr.standby"

    def _default_employee(self):
        return self.env.user.employee_id

    employee_id = fields.Many2one('hr.employee', string="Employee", default=_default_employee, required=True,
                                  ondelete='cascade', index=True)
    department_id = fields.Many2one('hr.department', string="Department", related="employee_id.department_id",
                                    readonly=True)
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string="Check Out")
    worked_hours = fields.Float(string='Worked Hours', compute='_compute_worked_hours', store=True, readonly=True)


    @api.depends('check_in', 'check_out')
    def _compute_worked_hours(self):
        for attendance in self:
            if attendance.check_out and attendance.check_in:
                delta = attendance.check_out - attendance.check_in
                attendance.worked_hours = delta.total_seconds() / 3600.0
            else:
                attendance.worked_hours = False

    def create_hr_standby(self,next_action):
        employee = self.env['hr.employee'].search([('id', '=', self.id)], limit=1)

        action_date = fields.Datetime.now()

        vals = {
            'employee_id': self.id,
            'check_in': action_date,
        }
        self.env['hr.standby'].sudo().create(vals)

        return employee._attendance_action(next_action)

    def close_hr_standby(self):

        action_date = fields.Datetime.now()
        attendance = self.env['hr.standby'].sudo().search([('employee_id', '=', self.id), ('check_out', '=', False)],
                                                   limit=1)
        if attendance:
            attendance.check_out = action_date




