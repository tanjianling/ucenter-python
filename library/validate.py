# -*- coding: utf-8 -*-
import re
from func import Function


class Validate(Function):
    def email(self, email):
        return re.match(r'^\w{1,16}\@([a-zA-Z|0-9]){2,10}\.([a-zA-Z]){2,4}$', email)

    def mobile(self, mobile):
        return re.match(r'^1\d{10}$', mobile)

    def qq(self, qq):
        return re.match(r'^\d{5,13}$', qq)
