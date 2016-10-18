# -*- coding: utf-8 -*-
from itertools import groupby

def elementosCardinalidadeOne(atributo, fatos):
    lista_retorno = []
    atributos_one = list( filter( lambda x: x[1] == atributo[0], fatos ) )
    for k, g in groupby( atributos_one, lambda x: x[1] ):
        lista_retorno.append( list(g)[-1] )
    return lista_retorno

def elementosCardinalidadeMany( atributo, fatos):
    lista_many = list( filter( lambda x: x[1] == atributo[0], fatos ) )
    remocoes = list( filter( lambda x: not x[-1], lista_many ) )
    for remove in remocoes:
        lista_many = list( filter( lambda x: x[2] != remove[2], lista_many ) )
    return lista_many

def entidadesAtivas(fatos, schema):
    lista_retorno = []
    for k, g in groupby( fatos, lambda x: x[0] ):
        entidades = list(g)
        for atributo in schema:
            if atributo[2] == 'one':
                lista_retorno.extend( elementosCardinalidadeOne(atributo, entidades) )
            else:
                lista_retorno.extend( elementosCardinalidadeMany(atributo, entidades) )

    return lista_retorno
