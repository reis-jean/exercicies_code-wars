# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) 
# and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    
    jadenCased = ''
    togle = True
    
    for i in range(len(string)):
        if string[i] == ' ':
            togle = True
            jadenCased += string[i]
        else:
            if togle:
                jadenCased += string[i].upper()
                togle = False
            else:
                jadenCased += string[i]
                togle = False
    
    return jadenCased

string1 = 'How can mirrors be real if our eyes arent real' 
string2 = 'most trees are blue' 
string3 = 'All the rules in this world were made by someone no smarter than you. So make your own.' 
string4 = 'School is the tool to brainwash the youth.' 


print(to_jaden_case(string1))
print(to_jaden_case(string2))
print(to_jaden_case(string3))
print(to_jaden_case(string4))

# O codigo acima não esta correto mais é necessario tratar as palavras separadamente, porque quando recebe um texto muito grande
# o codigo acaba se embaralhando.

# convem usar mais esse codigo ( que faz isso)

def to_jaden_case2(string):
    
    words = string.split()  # Divide a string em uma lista de palavras
    jaden_cased = []

    for word in words:
        jaden_cased.append(word.capitalize())  # Capitaliza cada palavra

    return ' '.join(jaden_cased)  # Junta as palavras com espaços

            

input_string = "XpOlmcxF CDNiVTKOo Ocxf X K i adcyEWoG lSF yegigkECh EFk SMDCKgib aAqef tJUksGE GFIE Ps hkvGyXcg QHNPBo xVjdEHIgZ grtFLeEw JgEC KnCy SfWn aUVKWyoLN PflEfY wxQneZHgCg UoaxWtl isA JpoA qijmM ad"
result = to_jaden_case2(input_string)
print(result)

# O método capitalize() é um método de string em Python que é usado para capitalizar a primeira letra 
# de uma string e converter todas as outras letras em minúsculas. Ele não afeta o restante das letras na string, apenas a primeira letra.

# O método join() é usado para unir os elementos de uma lista em uma única string, onde cada elemento é separado por um delimitador. 
# Neste caso, o delimitador é um espaço em branco, porque você usou ' '.join(...), o que significa que você deseja separar as palavras por espaços em branco.

# Portanto, quando você faz ' '.join(jadenCased), está pegando as palavras contidas em jadenCased e as unindo em uma única string, separando-as por espaços em branco.

# Por exemplo, se jadenCased fosse uma lista de palavras ["Isso", "é", "um", "exemplo"], ' '.join(jadenCased) criaria a seguinte string: "Isso é um exemplo".
# Cada palavra da lista é separada por um espaço em branco na string resultante.