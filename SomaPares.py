# titulo = """Soma
#     dos
#         pares"""
# print(f'{titulo:^30}')
#
#
# titulo = "Soma dos \t\033[31mpares\033[0;0m legais"
# print(f'{titulo:^30}')
#
# titulo = "Soma dos \t\033[31mpares\033[0;0m legais"
# print(f'{titulo:*^40.120}')
#
# numero = 80
# print(f'{numero:0>+5d}')
# numero = 7.5
# print(f'{numero:0>9.2f}')

titulo = "Soma dos \tpares"
print(f'{titulo:^30}')

num = int(input('Ate qual numero você gostaria de somar os pares:'))
i = 0
soma = 0
while i <= num:
    if i % 2 == 0:
        soma = soma + i
    i += 1
print(f'A soma dos numeros pares até {num:>010d} é {soma:>010d}')
