# A era antes do with

try:
    file = open('bananas.txt', 'w')
    file.write('Hola mundo \n')
    file.write('Fazer esse try me parece uma coisa estranha')
    ## contexto é finalizado mesmo ao existir erro

finally:
    file.close()

# Após o with

with open('bananas2.txt', 'w') as file:
    file.write('Hola mundo \n')
    file.write('A era antes do with')
