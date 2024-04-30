titulo = "Numeros Pares até 600"
print(f'{titulo:^30}')

print("FOR")
for i in range (1, 601):
    if i % 2 == 0:
        print(i)

print("WHILE")
i = 0
while i < 601:
    if i % 2 == 0:
        print(i)
    i += 1
