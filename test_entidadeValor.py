# -*- coding: utf-8 -*-
import unittest
from entidadeValor import *

schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]

# O objetivo aqui é adotar a metodologia utilizada nos Conding Dojos onde o
# problema é atacado de forma didática, utilizando TDD e baby steps.
# Cada teste é um pequeno passo em direção à solução do problema

class TestEntidadeValor(unittest.TestCase):
    def test_uma_tupla(self):
        fatos = [('joão', 'endereço', 'rua alice, 10', True)]
        self.assertEqual(entidadesAtivas(fatos, schema), fatos)



if __name__ == "__main__":
    unittest.main()
