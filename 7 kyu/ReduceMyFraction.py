# Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language)
# of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

import math

def reduce_fraction(fraction):
    mdc = math.gcd(fraction[0], fraction[1])
    numerador_reduzido = fraction[0] // mdc
    denominador_reduzido = fraction[1] // mdc

    fraction_reduce = [numerador_reduzido, denominador_reduzido]
    return fraction_reduce

array1 = [45, 120]
array2 = [60, 20]
array3 = [80, 120]
array4 = [4, 2]

print(reduce_fraction(array1))
print(reduce_fraction(array2))
print(reduce_fraction(array3))
print(reduce_fraction(array4))

# funcao faz a redução de fracoes
