# entidades possuem atributos
# atributos podem ter cardinalidade 1 ou N (muitos).

# Exemplo de fatos no formato de tuplas (E, A, V, added)
# i.e. (entidade, atributo, valor, fato foi adicionado ou retraido?)

facts = [
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua einstein, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]

# Nesse schema,
# os atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), os demais 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]

# Escrever função que retorna quais são os fatos ativos/vigentes.
# Pode assumir que a lista facts está ordenada com fatos mais antigos para os mais recentes.

def recuperaFatosAtivos(fatos, schema):

    for regra in schema:
        for fato in fatos:
# O método deve retornar um mapa:
#   [
#       [
    #       ('joão', 'endereço', 'rua einstein, 88', True),
    #       ('joão', 'telefone', '91234-5555', True),
#       ],
#       [
#           ('gabriel', 'telefone', '98888-1111', True),
#           ('gabriel', 'telefone', '56789-1010', True),
#       ]
#   ]
