import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from odoo.exceptions import UserError

class QualsysPartner(models.Model):
	_inherit = 'res.partner'

	is_attendant = fields.Boolean(string = "Inscrito a Curso", readonly = True)
