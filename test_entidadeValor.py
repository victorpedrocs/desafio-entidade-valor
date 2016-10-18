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

    def test_duas_tuplas_cardinalidade_um(self):
        fatos = [
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua einstein, 88', True),
        ]
        resultado = [
            ('joão', 'endereço', 'rua einstein, 88', True)
        ]
        self.assertEqual(entidadesAtivas(fatos, schema), resultado)

    def test_n_tuplas_cardinalidade_many(self):
        fatos = [
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
        ]
        resultado = [
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
        ]
        self.assertEqual(entidadesAtivas(fatos, schema), resultado)

    def test_remocao_many(self):
        fatos = [
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
        ]
        resultado = [
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '91234-5555', True),
        ]
        self.assertEqual(entidadesAtivas(fatos, schema), resultado)

    def test_varias_entidades(self):
        fatos = [
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
        ]
        resultado = [
            ('joão', 'endereço', 'rua einstein, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
        ]
        self.assertEqual(entidadesAtivas(fatos, schema), resultado)



if __name__ == "__main__":
    unittest.main()
