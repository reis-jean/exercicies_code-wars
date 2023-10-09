# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output 
# should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# The next words should be always capitalized.

def to_camel_case(text):
    newText = ''

    

    for i in range(len(text)): 
        

        if text[i] == '_' or text[i] == '-':
            newText += ' '
            newText += text[i+1].upper()
        if text[i].islower():
            newText += text[i]    
       
    print(newText)
    return newText

string1 = "the-stealth-warrior"
string2 = "The_Stealth_Warrior"
string3 = "the-stealth-warrior"

to_camel_case(string1)
to_camel_case(string2)
to_camel_case(string3)