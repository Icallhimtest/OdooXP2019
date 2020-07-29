import logging
# import time

from odoo import http
#from odoo.http import request

_logger = logging.getLogger(__name__)


class worker(http.Controller):
    @http.route('/slowpoke1', type='http', auth='none')
    def slowpoke1(self, **params):
        a = 0
        while a < 10**7:
            a += 1
        return '200 OK'

    @http.route('/slowpoke2', type='http', auth='none')
    def slowpoke2(self, **params):
        a = 0
        while a < 10**8:
            a += 1
        return '200 OK'

    @http.route('/slowpoke3', type='http', auth='none')
    def slowpoke3(self, **params):
        a = 0
        while a < 3 * 10**8:
            a += 1
        return '200 OK'
