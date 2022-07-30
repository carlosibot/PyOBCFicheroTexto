f = open('readme.txt', 'w')

f.write('Hola, he escrito en el archivo de texto\n')
f.close()

f = open('readme.txt', 'a')
f.write('\n')
f.write('hola de nuevo, he escrito una nueva linea')
f.close()