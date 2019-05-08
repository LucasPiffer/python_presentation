
for x in range(10):
    print(x)

for y in ['Banana', 'Leite', 'Arroz']:
    print(y)

for k in ('*' * 20).split(' '):
    print(k)

for z in ('Lucas', 'Piffer'):
    print(z)

value = 0

while value < 10:
    print(value)
    value += 1

print('Breaking')

number = 1

while(number < 10):
    if number % 5 == 0:
        break

    print(number)
    number += 1
