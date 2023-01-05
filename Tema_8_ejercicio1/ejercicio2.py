fichero = open('archvio_prueba.txt', 'w')
fichero.write('Hola este es mi primer Fichero')
fichero.close()

fichero = open('archvio_prueba.txt', 'r+')
fichero.read()
fichero.write('\nEste es mi segundo texto que escribo y soy un genio')

fichero.seek(0)
print(fichero.read())
fichero.close()