# -*- coding: utf-8 -*-
from itertools import groupby

def entidadesAtivas(fatos, schema):
    lista_retorno = []
    for atributo in schema:
        if atributo[2] == 'one':
            atributos_one = list( filter( lambda x: x[1] == atributo[0], fatos ) )
            for k, g in groupby( atributos_one, lambda x: x[1] ):
                lista_retorno.append( list(g)[-1] )
        else:
            lista_retorno.extend( list( filter( lambda x: x[1] == atributo[0], fatos ) ) )

    return lista_retorno
