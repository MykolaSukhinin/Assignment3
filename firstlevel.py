
n = [9, 8, -1, 7, 9, 10, 2, 55]
m=[]
print("Сума:",sum(n))
print("Найменеше число:", min(n)) 
print("Reverse:",*n[::-1])
for i in list(n):
    if i%2 != 0:
        m.append(i)
print("Непарні числа:", *m)   
k = []
x= int(input("На скільки треба помножити?:"))
for i in list(n):
    k.append(i*x)
print("помножений:", *k)     

