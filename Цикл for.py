#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
b = 0
с = 0
for i in numbers:
    b = 0
    for j in range(1, i):
        a = (i % j)
        if a != 0 :
            b = b + 1
    if (i - b) <= 2:
        primes = primes + [i]
    else:
        not_primes = not_primes + [i]
print("Простые ", primes)
print("Не простые ", not_primes)



