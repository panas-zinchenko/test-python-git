from random import randint
a = int(input("Введіть діапазон(мінімальне) = "))
b = int(input("Введіть діапазон(максимальне) ="))

l = []
y = 1

m = int(input("Скільки елементів потрібно в списку: "))
x = int(input("Введіть шукане число "))

while y <= m:
    l.append(randint(a, b))
    y += 1
print(l)


print("--------------------------------------------------------------------")

r = 0

if x in l:
    k = l.index(x)
    for i in l[:k]:
        r += i
    print("Сума чисел до ", x, "=", r)
else:
    print(0)
print("--------------------------------------------------------------------")
