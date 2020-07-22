import logging
_logger = logging.getLogger(__name__)

from odoo import models,api,fields
from odoo.exceptions import UserError

class QualsysCourses(models.Model):
	_name = 'qualsys.courses'
	_description = 'Cursos'

	@api.depends("attendees_ids")
	def get_courses_attendees(self):
		for data in self:
			data.attendees_number = len(data.attendees_ids)
			
	name = fields.Char(string = "Nombre",required=True)
	duration = fields.Integer(string="Duracion",required=True)
	start_date = fields.Date(string="Fecha de Inicio",required=True)
	end_date = fields.Date(string="Fecha de Termino",required=True)
	code = fields.Char(string="Codigo",required=True)
	attendees_number = fields.Integer(compute = get_courses_attendees, string="No. Asistentes")

	attendees_ids = fields.Many2many(
		'qualsys.attendees',
		string = "Asistentes"
	)

	teacher_id = fields.Many2one(
		'res.users',
		string="Maestro"
	)
	
	school_id = fields.Many2one(
		'qualsys.school',
		string="Escuela"
		)