# -*- coding: utf-8 -*-
from itertools import groupby

def removerElementos(lista):
    remocoes = list( filter( lambda x: not x[-1], lista ) )
    for remove in remocoes:
        lista = list( filter( lambda x: x[2] != remove[2], lista ) )
    return lista

def elementosCardinalidadeOne(atributo, fatos):
    lista_retorno = []
    lista_one = list( filter( lambda x: x[1] == atributo[0], fatos ) )

    lista_one = removerElementos(lista_one)

    for k, g in groupby( lista_one, lambda x: x[1] ):
        lista_retorno.append( list(g)[-1] )

    return lista_retorno

def elementosCardinalidadeMany( atributo, fatos):
    lista_many = list( filter( lambda x: x[1] == atributo[0], fatos ) )
    lista_many = removerElementos(lista_many)
    return lista_many

def entidadesAtivas(fatos, schema):
    lista_retorno = []
    fatos.sort(key=lambda x: x[0])
    for k, g in groupby( fatos, lambda x: x[0] ):
        entidades = list(g)
        for atributo in schema:
            if atributo[2] == 'one':
                lista_retorno.extend( elementosCardinalidadeOne(atributo, entidades) )
            else:
                lista_retorno.extend( elementosCardinalidadeMany(atributo, entidades) )

    return lista_retorno
