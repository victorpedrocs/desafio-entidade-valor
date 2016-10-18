# -*- coding: utf-8 -*-
from itertools import groupby

def elementosCardinalidadeOne(atributo, fatos):
    lista_retorno = []
    atributos_one = list( filter( lambda x: x[1] == atributo[0], fatos ) )
    for k, g in groupby( atributos_one, lambda x: x[1] ):
        lista_retorno.append( list(g)[-1] )
    return lista_retorno


def entidadesAtivas(fatos, schema):
    lista_retorno = []
    for atributo in schema:
        if atributo[2] == 'one':
            lista_retorno.extend( elementosCardinalidadeOne(atributo, fatos) )
        else:
            lista_retorno.extend( list( filter( lambda x: x[1] == atributo[0], fatos ) ) )

    return lista_retorno
