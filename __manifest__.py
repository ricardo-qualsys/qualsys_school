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
		'wizard/wizard_course_assign_view.xml',
		'wizard/wizard_school_assign_view.xml',
		'security/security.xml',
		'security/ir.model.access.csv'
	]
}