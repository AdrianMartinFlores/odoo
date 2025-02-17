from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birth Date')
    biography = fields.Text(string='Biography')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')
