{
    'name': 'Library Management',
    'version': '1.0.0',
    'summary': 'Module for managing books and authors',
    'author': 'Tu Nombre',
    'category': 'Library Management',
    'depends': ['base'],
'data': [
    'security/ir.model.access.csv',  # Primero la seguridad
    'views/library_book_views.xml',    # Luego las vistas que definen acciones
    'views/library_views.xml',         # Luego las vistas que usan las acciones
    'views/library_author_views.xml',
],




    'installable': True,
    'application': True,
}
