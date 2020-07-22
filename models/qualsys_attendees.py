import logging
_logger = logging.getLogger(__name__)

from odoo import models,api,fields
from odoo.exceptions import UserError

class QualsysAttendees(models.Model):
    _name = 'qualsys.attendees'
    _description = 'Asistentes'

    partner_id = fields.Many2one(
        'res.partner',
        string = "Nombre",
        required = True,
    )
    courses_id = fields.Many2many(
        'qualsys.courses',
        string = "Curso"
    )
    age = fields.Integer(string="Edad",required=True)