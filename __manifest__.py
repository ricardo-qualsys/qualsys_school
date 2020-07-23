{
	'name' : "qualsys_school",
	'description':" Escuela de cursos Odoo",
	'author':"Qualsys-Ricardo",
	'depends': [
		'base'
	],
	'data':[
		'views/qualsys_school_views.xml',
		'views/qualsys_courses_views.xml',
		'views/qualsys_attendees_views.xml',
		'views/qualsys_partner_views.xml',
		'wizard/wizard_course_assign_view.xml',
		'wizard/wizard_school_assign_view.xml',
		'reports/qualsys_school_report.xml',
		'reports/qualsys_school_template.xml',
		'reports/qualsys_courses_report.xml',
		'reports/qualsys_courses_template.xml',
		'security/security.xml',
		'security/ir.model.access.csv'
	]
}
