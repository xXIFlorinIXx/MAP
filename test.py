# x = 10
# if x > 10 : 
#     print("x>5")
# else:
#     print("x<5")

#Do while simulat
# i = 1
# while True :
#     print("Do while simulat: ",i)
#     i = i + 1;
#     if i > 5:
#         break

# #Instructiunea While

# i = 1
# while i <= 5:
#     print("Bucla While: ",i)
#     i+=1

#Instruciunea for

#citim de la tastatura un numar
# n = int(input("Introduceti numarul: "))
# for i in range(1,n+1,2):
#     print("i = ", i)

#Citirea Valorilor din lista v

# n = int(input("Introdu numarul de elemente: "))
# v = []
# for i in range(n):
#     val = int(input("Introdu valoarea: "))
#     v.append(val)

# for i in range(n):
#     print(v[i],' ')

# nume = input("Introdu numele tau: ")
# print(nume+", e timpul sa iei o pauza")

#Sirul lui Fibonacci
#Primul element este 0
#Al doilea element este 1
#FIecare element urmator este suma celor doua elemente anterioare
#Ex 0 1 1 2 3 5 8 13 21 34

# x = 0
# y = 1
# print (x)
# print (y)
# while True :
#     print(x+y)
#     aux = x + y
#     x = y
#     y = aux
#     if aux > 1000:
#         break

#Verifica daca suma cifrelor unui numar este numar PAR

# def verifica_suma_cif(numar):
#     suma_cif = 0
#     copie = numar
#     while copie > 0 :
#         cifra = copie % 10
#         suma_cif+= cifra
#         copie = copie // 10
#     print("Suma cifrelor este: ", suma_cif)
#     if suma_cif % 2 == 0:
#         print("Suma cifrelor este para")
#     else:
#         print("Suma cifrelor este impara")

# numar = int(input("Introdu numarul: "))
# verifica_suma_cif(numar)

#Verificati daca un numar este palindrom

def palindrom(n):
    copie = n
    og = 0
    while copie != 0:
        og = og * 10 + copie % 10
        copie = copie // 10
    if og == n:
        print("Palindrom")
    else:
        print("NU este palindrom")

n = int(input("Nr pal: "))
palindrom(n)