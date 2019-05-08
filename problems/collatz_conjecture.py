# https://pt.wikipedia.org/wiki/Conjectura_de_Collatz

start_at = 2
number_with_max_iterations = {"number": start_at, "count": 1}

for i in range(start_at, 100):
    number = i
    total = 1

    while number > 1:
        total += 1

        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    else:
        number_with_max_iterations["number"] = i
        number_with_max_iterations["count"] = total

print(number_with_max_iterations)