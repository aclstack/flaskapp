# -*- coding: utf-8 -*-
import json


class JsonObject():
    def __init__(self):
        self.dic = {}

    def put(self, key, value):
        self.dic[key] = value

    def get(self,key):
        return self.dic[key]

    def getJson(self):
        return json.dumps(self.dic, ensure_ascii=False)
    def getDic(self):
        return self.dic
