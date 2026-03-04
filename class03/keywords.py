import keyword
print (keyword.kwlist)
print("\n")
print(keyword.iskeyword("True")) #as it is a keyword it prints True
print(keyword.iskeyword("true")) #False
print(keyword.iskeyword("name")) #Flase