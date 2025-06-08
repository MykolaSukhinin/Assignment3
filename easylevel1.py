# 1
n = [1, -2, 6, 7, 8 ,-22, 55, 72, 97]
x= int(input("Введіть X:"))
l1=[]
for i in list(n):
    if i > x:
        l1.append(i)
print("Числа більші за X:", *l1)



# 2 
l2= []
for i in list(n):
    if i > 0:
        l2.append(i)
print("Середнє додатних:", (sum(l2)/len(l2)))

#3 
x= int(input("Введіть X:"))
l18=[]
for i in list(n):
    if i < x:
        l18.append(i)
print("Mаксимальна кількість чисел, менших за X:", len(l18))



# 4
y = int(input("ВВедіть Y:"))
l3=[]
for i in list(n):
    if i % y == 0:
        l3.append(i) 
print("Сума чисел, які діляться на Y:", sum(l3))

# 5 
l4=[]
for i in list(n):
    l4.append(i**2)
print("Список квадратів: ", l4)

# 6
l5=[]
for i in list(n):
    if i > 0:
        l5.append(i)
print("Додатні числа :", l5)

#7 


words= ["LOL", "Kolya", "Phone", "Leonid"]



#8
N = int(input("Введіть N:"))
print ("Сума перших N чисел:", sum(n[0:N]))


#9
l7= []
for u in list(words):
    if u == u[::-1]: l7.append(u)
print( "Паліндроми:", *l7)

#10
l8= []
K = int(input("Введіть дільник:"))
for i in list(n):
    if i % K == 0:
        l8.append(f"{i} Ділиться на дільник: {K}")
    else:
        l8.append(f"{i} Не ділиться на дільник: {K}")  

print(l8)








