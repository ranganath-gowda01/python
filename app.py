s="hello Good&morning"
for i in s:
    if i.isalpha()!=True and i.isspace()!=True:
        print("The address of",i,"is",id(i),"is not a alphabet" )