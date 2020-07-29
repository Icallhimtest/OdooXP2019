import logging
import random
import time

from odoo import http
#from odoo.http import request

log = logging.getLogger(__name__)


class worker(http.Controller):
    def coucou(a):
        fake_sql_reqs = int(random.random() * 100)
        breaks = sorted([random.randrange(1, a) for i in range(fake_sql_reqs)], reverse=1)
        for b in breaks:
            while a > b:
                a -= 1
            time.sleep(random.random() / 100)

    @http.route('/slowpoke1', type='http', auth='none')
    def slowpoke1(self, **params):
        self.coucou(10**7)
        return '200 OK'

    @http.route('/slowpoke2', type='http', auth='none')
    def slowpoke2(self, **params):
        self.coucou(10**8)
        return '200 OK'

    @http.route('/slowpoke3', type='http', auth='none')
    def slowpoke3(self, **params):
        self.coucou(10**9)
        return '200 OK'

    @http.route('/slowpoke4', type='http', auth='none')
    def slowpoke4(self, **params):
        self.coucou(10**10)
        return '200 OK'
