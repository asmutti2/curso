frase = "Python é uma linguagem excelente "
print("py" in frase)
print("Py" in frase) # letra maiúscula faz diferença
print("e" in frase)
print("uma" not in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())
print(frase.split())
print(frase.split('Python'))

x = frase.split('Python') 
print(x)