from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Name')
    title = fields.Char(string='Title')
    publication_date = fields.Date(string='Publication Date')
    author_id = fields.Many2one('library.author', string='Author')


