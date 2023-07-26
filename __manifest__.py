{
    'name': "School",

    'summary': """
        School Management System """,

    'description': """
        This System To Manage School Departments
    """,
    'author': "Abdelrahman",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'portal', 'mail', 'utm'],

    # always loaded
    'data': [
        'security/school_ms_security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
