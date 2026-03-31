import re

def decode(phrase:str) -> str:

    # With regex we search for the characters inside parenthesis:
    
    elements_list = ""

    for i in range(phrase.count("(")):
        element = re.search(r"(\(\w+\))",phrase)
        phrase = phrase.replace(element.group(1),"")
        element = element.group(1)[::-1]
        
        print(element)
        
    
decode("(f(b(dc)e)a)")