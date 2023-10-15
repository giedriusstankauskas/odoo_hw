# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Books(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def display_book(self, **kw):
        books = request.env['book.book'].search([])
        vals = {'books': books}
        return request.render('books.display_books', vals)

    @http.route('/books/create', auth='public', type='http', website=True)
    def redirect_to_form_book_create(self, **kw):
        return request.render('books.create_book_form')

    @http.route('/create', auth='public', type='http', website=True)
    def create_new_book(self, **kw):
        request.env['book.book'].create({
            'name': kw.get('name'),
            'description': kw.get('description'),
            'company': kw.get('company')
        })
        return request.redirect('/')

    @http.route('/update', auth='public', type='http', website=True)
    def redirect_to_form_update(self, **kw):
        vals = {}
        book_object = request.env['book.book'].search([('id', '=', kw.get('id'))])
        vals.update({
            'book': book_object,
        })
        return request.render('books.update_book_form', vals)

    @http.route('/update/book', auth='public', type='http', website=True)
    def update_book(self, **kw):
        id = int(kw.get('id'))
        request.env['book.book'].search([('id', '=', id)]).write({
            'name': kw.get('name'),
            'description': kw.get('description'),
            'company': kw.get('company')
        })
        return request.redirect('/')

    @http.route('/delete', auth='public', type='http', website=True)
    def delete_book(self, **kw):
        book_id = int(kw.get('id'))
        request.env['book.book'].search([('id', '=', book_id)]).unlink()
        return request.redirect('/')

