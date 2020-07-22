# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class WizardCourseAssign(models.TransientModel):
	_name = "wizard.course.assign"
	_description = "Asignacion: Asistente a Curso"
	
	courses_ids = fields.Many2many('qualsys.courses', string="Cursos")

	def asignar_curso(self):
		context = dict(self._context or {})
		attendees = self.env['qualsys.attendees'].browse(context.get('active_ids'))

		for asistente in self.courses_ids:
			asistente.attendees_ids |= attendees
			_logger.info("### Curso: %s" % asistente.attendees_ids)
			for cur in attendees:
				cur.courses_id |= asistente
				_logger.info("### Asistente: %s" % cur.courses_id)
		pass