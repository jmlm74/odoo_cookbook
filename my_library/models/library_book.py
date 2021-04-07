# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'

    short_name = fields.Char('Short Title', required=True)
    name = fields.Char('Title', required=True)

    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages')
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4),  # Optional precision decimals,
    )
    cost_price = fields.Float(
        'Book Cost', digits='Book Price')
    retail_price = fields.Monetary(
        'Retail Price',
        # optional: currency_field='currency_id',
    )

    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
    )
    author_ids = fields.Many2many('res.partner', string='Authors')
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    category_id = fields.Many2one('library.book.category')

    """
    Methods
    """
    def name_get(self):
        """" correspond au _str """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
        result.append((record.id, rec_name))
        return result


class ResPartner(models.Model):
    _inherit = 'res.partner'

    published_book_ids = fields.One2many(
        'library.book', 'publisher_id',
        string='Published Books')

    authored_book_ids = fields.Many2many(
        'library.book',
        string='Authored Books',
        # relation='library_book_res_partner_rel',
        # optional
    )

