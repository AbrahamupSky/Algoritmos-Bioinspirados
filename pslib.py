# 01: Crear una poblacion inicial
# 02: Evaluar cada individuo
# 03: Selecciona el mejor
# 04: Seleccionar uno de aleatoria para cruzar con otro, los hijos reemplazan a los
# padres, los hijos se mezclan aleatoriamente, operacion de cruza, se hace un nuevo arreglo
# que es la nueva poblacion
# 05: Mutacion

import random

def calculate_aptitud(individuo):
  aptitud = sum([x**2 + 2 for x in individuo])
  return aptitud

def most_apt(array1):
  apts = [calculate_aptitud(individuo) for individuo in array1]
  better_index = apts.index(max(apts))
  return array1[better_index], apts[better_index]

def cruza(padre1, padre2):
  cross_point = random.randint(1, len(padre1))
  hijo1 = padre1[:cross_point] + padre2[cross_point:]
  hijo2 = padre2[:cross_point] + padre1[cross_point:]
  return hijo1, hijo2

people = 30 #Ajustable
bits = 1
range_num = range(1, 16)

array1 = [[random.choice(range_num) for i in range(bits)] for i in range(people)]
binary_array = [[format(num, '04b') for num in individuo] for individuo in array1]
# 0 indica los 0 a la izquierda que debe tener
# 4 indica el resultado final, osea una longitud de 4 caracteres
# b indicamos el como se debe formatearse, en este caso, binario

print(binary_array)
print('\n')

parent_index1 = 0
parent_index2 = 1

parent1 = array1[parent_index1]
parent2 = array1[parent_index2]

hijo1, hijo2 = cruza(parent1, parent2)

array1[parent_index1] = hijo1
array1[parent_index2] = hijo2

for i, individuo in enumerate(array1, start = 1):
  individual_aptitud = calculate_aptitud(individuo)
  print(f'Aptitud del individuo {i}: {individual_aptitud}')

print('\n')

individuo, aptitud = most_apt(array1)
print('Aptitud del individuo con mejor aptitud: ', individuo)
print('Con una aptitud de: ', aptitud)

print('Padre 1: ', parent1)
print('Padre 2: ', parent2)
print('Hijo 1: ', hijo1)
print('Hijo 2: ', hijo2)
print('Arreglo despues de la cruza: ', array1)