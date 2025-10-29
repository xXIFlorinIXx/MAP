#Scrieți un program care să afișeze suma numerelor de la 1 la 100 

# suma = 0

# for i in range(1,100,1):
#     suma += i

# print(suma)

#Scrieți un program care să determine produsul primelor 10 numere naturale

# prod = 1

# for i in range(1,10,1):
#     prod *= i

# print(prod)

#Scrieți un program care să afișeze primele 20 de numere impare

# cnt = 0
# i = 1

# while cnt < 20:
#     if(i%2 !=0):
#         print(i)
#         cnt +=1
#     i+=1

#Determinați cel mai mare divizor comun (CMMD) a două numere întregi citite de la tastatură.

# def CMMDC (a,b):
#     ca = a
#     cb = b
#     while b!=0:
#         r = a % b
#         a = b
#         b = r
#     print("CMMDC", a)

# n = int(input("Primul numar: "))
# m = int(input("Al doilea numar: "))
# CMMDC(n,m)

#Scrieți un program care să calculeze factorialul unui număr întreg citit de la tastatură.

# def factorial(n):
#     if(n <= 0):
#        return 1
#     else:
#         return n*factorial(n-1)

# n = int(input("Factorialul numarului: "))
# print(" este: ",factorial(n))

#Determinați dacă un număr întreg dat este un număr prim.

# def prim(n):
#     if n <= 1:
#         return 0
#     if n % 2 == 0:
#         return 0
#     for d in range(3,n,2):
#         if d * d > n:
#             break
#         if n % d == 0:
#             return 0
#     return 1

# n = int(input("Numarul este:"))
# if prim(n):
#     print("PRIM")
# else:
#     print("NU este prim")

#Scrieți un program care să determine ziua săptămânii pe baza unui număr de la 1 la 7, unde 1 reprezintă luni și 7 reprezintă duminică

# def zi(n):
#     match n:
#         case 1:
#             print("Luni")
#         case 2:
#             print("Marti")
#         case 3:
#             print("Miercuri")
#         case 4:
#             print("Joi")
#         case 5:
#             print("Vineri")
#         case 6:
#             print("Sambata")
#         case 7:
#             print("Duminica")
#         case _:
#             print("Zilele sapt. sunt de la 1 la 7!!!")
        

# n = int(input("Introdu un numar de la 1 la 7: "))
# zi(n)

#Determinați dacă un număr dat este un număr par sau impar

# def paritate(n):
#     if n % 2 == 0:
#         print("PAR")
#     else:
#         print("IMPAR")

# n = int(input("Numarul: "))
# paritate(n)

#Scrieți un program care să determine dacă un an citit de la tastatură este un an bisect

# def bisect(an):
#       return an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)

#Calculați suma a două numere întregi citite de la tastatură și afișați rezultatul

# def suma(a,b):
#     return a + b

# n = int(input("Primul numar: "))
# m = int(input("Al doilea numar: "))
# print(suma(n,m))

#Determinați dacă un număr întreg citit de la tastatură este pozitiv sau negativ și afișați rezultatul

# def n_sau_p(n):
#     if n < 0:
#         print("NEGATIV")
#     else:
#         print("POZITIV")

# n = int(input("Nr: "))
# n_sau_p(n)

#Scrieți un program care să afișeze numerele Fibonacci până la un anumit termen citit de la tastatură și să le afișeze
# def fib(n):
#     x = 0
#     y = 1
#     print (x)
#     print (y)
#     while True :
#         aux = x + y
#         if aux > n:
#             break
#         print(aux)
#         x = y
#         y = aux

# n = int(input("Nr:"))
# fib(n)

#Scrieți un program care să determine suma și media a unei liste de numere citite de la tastatură

# def suma_si_medie(v,n):
#     suma = 0
#     for i in range(0,n,1):
#         suma += v[i]
#     print(suma,' ',suma/n)

# n = int(input("Numarul de elemente: "))
# v = []

# for i in range(0,n,1):
#     x = int(input("Nr: "))
#     v.append(x)
# suma_si_medie(v,n)

#Determinați cel mai mic și cel mai mare număr dintr-o listă de numere citite de la tastatură

# def mic_mare(v,n):
#     min = v[1]
#     max = v[1]
#     for i in range(0,n,1):
#         if v[i] < min:
#             min = v[i]
#         if v[i] > max:
#             max = v[i]
#     print("minimul din lista este ",min)
#     print("maximul din lista este ",max)

# n = int(input("Numarul de elemente: "))
# v = []

# for i in range(0,n,1):
#     x = int(input("Nr: "))
#     v.append(x)

# mic_mare(v,n)


# def bsort(v,n):
#      ok = False
#      while ok == False:
#           ok = True
#           for i in range(0,n-1,1):
#                if(v[i]>v[i+1]):
#                     aux = v[i]
#                     v[i] = v[i+1]
#                     v[i+1] = aux
#                     ok = False
      
            

#A se rezolva ecuația de Gradul al doilea folosind un program scris in Python.
# n = int(input("Numarul de elemente: "))
# v = []

# for i in range(0,n,1):
#      x = int(input("Nr: "))
#      v.append(x)
# bsort(v,n)

# for i in range(0,n,1):
#      print(v[i])

# import math

# def rezolva_ecuatie_grad_2(a, b, c):
#     if a == 0:
#         print("Eroare: a nu poate fi 0. Nu este o ecuație de gradul al doilea.")
#         return

#     delta = b**2 - 4*a*c

#     print(f"Delta = {delta}")

#     if delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print("Două soluții reale și diferite:")
#         print(f"x1 = {x1}")
#         print(f"x2 = {x2}")
#     elif delta == 0:
#         x = -b / (2*a)
#         print("O soluție reală dublă:")
#         print(f"x = {x}")
#     else:
#         parte_reala = -b / (2*a)
#         parte_imaginara = math.sqrt(-delta) / (2*a)
#         print("Două soluții complexe:")
#         print(f"x1 = {parte_reala} + {parte_imaginara}i")
#         print(f"x2 = {parte_reala} - {parte_imaginara}i")

# # Exemplu de utilizare:
# a = float(input("Introdu a: "))
# b = float(input("Introdu b: "))
# c = float(input("Introdu c: "))

# rezolva_ecuatie_grad_2(a, b, c)

# Se citesc 3 numere de la tastatură să se afișeze dacă acestea pot reprezenta unghiurile unui triunghi.
# def este_triunghi(u1, u2, u3):
#     suma = u1 + u2 + u3
#     if u1 > 0 and u2 > 0 and u3 > 0 and suma == 180:
#         return True
#     else:
#         return False

# 
# u1 = float(input("Introdu unghiul 1: "))
# u2 = float(input("Introdu unghiul 2: "))
# u3 = float(input("Introdu unghiul 3: "))

# if este_triunghi(u1, u2, u3):
#     print("Unghiurile pot reprezenta un triunghi.")
# else:
#     print("Unghiurile NU pot reprezenta un triunghi.")
