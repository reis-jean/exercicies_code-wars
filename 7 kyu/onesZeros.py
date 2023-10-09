# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):

    aux = 1
    
    result = 0

    for i in reversed(arr):
        i = aux * i
        # print(i)
        aux = aux * 2
        result += i

    return  result


array1 = [0, 0, 0, 1] 
array2 = [0, 0, 1, 0] 
array3 = [0, 1, 0, 1]
array4 = [1, 0, 0, 1] 
array5 = [0, 0, 1, 0] 
array6 = [0, 1, 1, 0]
array7 = [1, 1, 1, 1]
array8 = [1, 0, 1, 1] 


print(binary_array_to_number(array1))
print(binary_array_to_number(array2))
print(binary_array_to_number(array3))
print(binary_array_to_number(array4))
print(binary_array_to_number(array5))
print(binary_array_to_number(array6))
print(binary_array_to_number(array7))
print(binary_array_to_number(array8))

# funcao recebe numero binario e retorna um decimal