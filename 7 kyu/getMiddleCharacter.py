# You are going to be given a word. Your job is to return
# the middle character of the word. If the word's length is odd,
#  return the middle character. If the word's length is even, return the middle 2 characters.


def getMiddle(s):
    
    result = ''
    middle = len(s)
    
    if middle % 2 == 0:
        i = middle // 2
        result += s[i -1]
        result += s[i]
        return result
    else:
        i = middle // 2
        result += s[i]
        return result

                
print(getMiddle("test") )

print(getMiddle("testing"))

print(getMiddle("middle") )

print(getMiddle("A") )

# getMiddle recebe uma string que retorno as letras do meio, 
# se a quantidade da string for par ele retorna as duas letras do meio, se impar somente 1
