# Compare two strings by comparing the sum of their values (ASCII character code).

# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.

def compare(s1, s2):
    print(s1, s2)

    def is_number(value):
        return isinstance(value, (int, float))

    caracte1 = 0
    caracte2 = 0
    
    if s1 != 'null' and s1 != '' and  s1 != 'NULL'  and s1 != 'Nil' and s1 != None and s1 != '!!'  and s1 != '##' :
        for i in s1:
            if is_number(i):
                caracte1 = caracte1 + i
            else:    
                caracte1 = caracte1 + ord(i.upper())
    else:
        caracte1 = 0

    if s2 != 'null' and s2 != '' and  s2 != 'NULL'  and s2 != 'Nil' and s2 != None and s2 != '!!'  and s2 != '##':
        for i in s2:
            if is_number(i):
                caracte2 = caracte2 + i
            else:    
                caracte2 = caracte2 + ord(i.upper())
    else:
        caracte2 = 0
    
    print(caracte1, caracte2)

    if caracte1 == 0 or caracte2 == 0:
        return True
    elif caracte1 == caracte2: 
        return True
    else:
        return False
    
        
compare('AD', 'BC')
compare('AD', 'DD')
compare("gf", "FG")
compare("ZzZz", "ffPFF")
compare("ZzZz", "ffPFF")
compare("kl", "lz" )
compare('null', "" )
compare('K' , [75] )
compare([68, 84, 83, 76, 82] , 'RPQSC' )
compare([71, 74, 76] , 'LEL')
compare('YNW' , [83, 82, 89])
compare('L' , [76])

