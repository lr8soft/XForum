# -*- coding: utf-8 -*-

import hashlib


class Encryptor(object):

    @classmethod
    def md5_encrypt(cls, password):
        md5 = hashlib.md5()
        md5.update(password.encode())
        password = md5.hexdigest()
        return password
