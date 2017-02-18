# -*- coding: utf-8 -*-
import re


class Function(object):
    def md5(self, str):
        import hashlib
        m2 = hashlib.md5()
        m2.update(str)
        return m2.hexdigest()
