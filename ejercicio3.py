from chile_lista_aninadas import chile

#1.- Recorra la lista para monstrar las regiones de Chile

for region in chile:
    print(region[0])
    for provincia in region[1]:
        print(provincia[0])
    
    print()

# lista_juegos = ['Dota', 'COD', 'Minecraft', 'Doom DA']

# print(len(lista_juegos))
# print(lista_juegos[0])
# for juego in lista_juegos:
#     print(juego)