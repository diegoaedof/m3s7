
# productos_enumerate = [
#     (0,("manzana",1.0)),
#     (1,("pera", 1.5)),
#     (2,("naranja", 2.0))
# ]

productos = [
    ("manzana", 1.0),
    ("pera", 1.5),
    ("naranja", 2.0)
]

for tupla_enumerate in enumerate(productos):
    print(f" El producto {tupla_enumerate[1][0]}, tiene un valor de ${tupla_enumerate[1][1]}. Ambos elementos ocupan el indice {tupla_enumerate[0]}")

# lista_original = [
#     40,
#     "elemento2",
#     True
# ]
# enumerate(lista_original)

# lista_enumerate = [
#     (0, 40),
#     (1, "elemento2"),
#     (2, True)
# ]

# for i,elemento in enumerate(lista_original):
#     print(f"En el indice {i} está el elemento {elemento}")
# frutas = ["manzana","pera","naranja"]
# for i, fruta in enumerate(frutas):
#     print(f"En el índice {i} está {fruta}")

