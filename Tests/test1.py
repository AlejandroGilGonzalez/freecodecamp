from random import randint as ran


with open("dics/b.txt","r",encoding="utf-8") as f:
    lista = list(f)

new_lista = [pal.replace("\n","") for pal in lista]
dictionary = {i:word for i,word in enumerate(new_lista)}

number = ran(0,len(dictionary))

s_word = dictionary[number]
s_word = {k:j for k,j in enumerate(s_word)}
print(s_word)

layout ="".join(["_" for i in range(len(s_word))])

print(layout)

x = False
count = 0
while x == False or count < 10:
    letra = input("Escoja una letra: ")
    if len(letra)>1:
        print("No puede ser más de 1 letra.")
        print(layout)
    else:
        count += 1
        if layout == s_word:
            x = True
        if letra in s_word.values():
            layout = layout[:ind]+letra+layout[ind+1:]
        print(layout) 
    


    