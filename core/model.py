from typing import List


class Class:
    def __init__(self, name):
        self.name = name
        self.mts: List[Method] = []
        self.flds: List[Field] = []


class Method:
    def __init__(self, name, tp, md, extr=""):
        self.name = name
        self.tp = tp
        self.md = md
        self.params: List[Param] = []
        self.extr = extr


class Field:
    def __init__(self, name, tp, md, extr=""):
        self.name = name
        self.tp = tp
        self.md = md
        self.extr = extr


class Param:
    def __init__(self, name, tp):
        self.name = name
        self.tp = tp


class Link:
    def __init__(self, tp, cl1, cl2, left="", right=""):
        self.tp = tp
        self.cl1 = cl1
        self.cl2 = cl2
        self.left = left
        self.right = right
