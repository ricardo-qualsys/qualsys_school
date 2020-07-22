# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class WizardSchoolAssign(models.TransientModel):
	_name = "wizard.school.assign"
	_description = "Asignacion: Curso a Escuela"
	
	school_ids = fields.Many2one('qualsys.school', string="Escuela", requiered=True)
	
	
	def asigar_escuela(self):
		context = dict(self._context or {})
		courses = self.env['qualsys.courses'].browse(context.get('active_ids'))

		for record in self.school_ids:
			record.courses_ids = courses
			for school in courses:
				school.school_ids = record
		return {}