def toBinary(n):
    m=[]
    for i in n:
      m.append(int(bin(ord(i))[2:]))
    return m

text_tastatura = input("Introduceti propozitia: ")
print(toBinary(text_tastatura))