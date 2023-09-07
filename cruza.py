import random

def calculate_aptitude(individuo):
  aptitud = sum([x**2 + 2 for x in individuo])
  return aptitud

def most_apt(array1):
  apts = [calculate_aptitude(individuo) for individuo in array1]
  better_index = apts.index(max(apts))
  return array1[better_index]

def cruza(padre1, padre2):
  cross_point = random.randint(1, len(padre1))
  hijo1 = padre1[:cross_point] + padre2[cross_point:]
  hijo2 = padre2[:cross_point] + padre1[cross_point:]
  return hijo1, hijo2

def mutate(parent1, parent2):
  """
  Realiza la mutación de dos individuos.

  Args:
    parent1: El primer individuo.
    parent2: El segundo individuo.

  Returns:
    Los dos individuos mutados.
  """

  # Seleccionamos un bit aleatorio en cada individuo.
  index1 = random.randint(0, len(parent1) - 1)
  index2 = random.randint(0, len(parent2) - 1)

  # Mutamos un bit aleatorio en cada individuo.
  parent1[index1] = mutate_bit(parent1[index1])
  parent2[index2] = mutate_bit(parent2[index2])

  return parent1, parent2

def mutate_bit(bit):
  """
  Cambia el valor de un bit.

  Args:
    bit: El bit a cambiar.

  Returns:
    El bit cambiado.
  """

  return 1 if bit == 0 else 0

people = 30 # Ajustable
bits = 1
range_num = range(1, 16)

array1 = [[random.choice(range_num) for i in range(bits)] for i in range(people)]

print("Población inicial:")
for i, individuo in enumerate(array1, start=1):
  print(f"Individuo {i}: {individuo}")

print('\n')

# Realiza la cruza entre todos los padres
num_padres = len(array1)

for i in range(num_padres):
  for j in range(i + 1, num_padres):
    padre1 = array1[i]
    padre2 = array1[j]

    # Mutamos los padres
    padre1, padre2 = mutate(padre1, padre2)

    # Reemplazar a los padres con sus hijos en el array1
    array1[i] = padre1
    array1[j] = padre2

# Convierte el arreglo a representación binaria
binary_array = [[format(num, '04b') for num in individuo] for individuo in array1]

# Encuentra el individuo más apto después de la cruza
individuo_mas_apto = most_apt(array1)

print("Arreglo después de la cruza:")
for i, individuo in enumerate(binary_array, start=1):
  print(f"Individuo {i}: {individuo}")

print("El individuo más apto tiene un:", individuo_mas_apto)
