# Create a function that always returns True for every item in a given list. However, if an element
#  is the word 'flick', switch to always returning the opposite boolean value.



def flick_switch(lst):
    toggle = True
    result = []

    for item in lst:
        if item == 'flick':
            toggle = not toggle
        result.append(toggle)

    return result

list1 = ['codewars', 'flick', 'code', 'wars']
list2 = ['flick', 'chocolate', 'adventure', 'sunshine']
list3 = ['bicycle', 'jarmony', 'flick', 'sheep', 'flick']

flick_switch(list1)
flick_switch(list2)
flick_switch(list3)

print(flick_switch(list1))
print(flick_switch(list2))
print(flick_switch(list3))


# Essa função recebe uma lista que compara com a palavra 'flick', caso seja, adiciona 
# False na lista, até que apareça uma nova palava 'flick' novamente
