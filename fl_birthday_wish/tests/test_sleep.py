# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import time

from odoo.tests.common import TransactionCase

log = logging.getLogger(__name__)


class Zzzzzzz(TransactionCase):

    def test_timeout(self):
        log.info('starting the sleep test')
        for i in range(1, 121):
            log.info('sleeping 60')
            time.sleep(60)
            log.info('slept %s', i * 60)
