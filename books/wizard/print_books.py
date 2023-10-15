from odoo import models, fields, api, _


class PrintBookWizard(models.TransientModel):
    _name = 'print.book.wizard'
    _description = 'Print Book Wizard'

    date_from = fields.Datetime(string='Data nuo')
    date_to = fields.Datetime(string='Data iki')

    def action_print_books(self):
        books_between_dates = []
        books = self.env['book.book'].search_read([])
        date_from = self.date_from
        date_to = self.date_to

        for book in books:
            if book['create_date'] <= date_to and book['create_date'] >= date_from:
                books_between_dates.append(book)

        data = {
            'books': books_between_dates,
        }

        return self.env.ref('books.action_report_books').report_action(self, data=data)

