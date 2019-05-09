# https://pt.wikipedia.org/wiki/Conjectura_de_Collatz

start_at = 2
number_with_max_iterations = {"number": start_at, "count": 1}

for i in range(start_at, 1000000):
    number = i
    total = 0

    while number > 1:
        total += 1

        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    else:
        if total > number_with_max_iterations["count"]:
            number_with_max_iterations["number"] = i
            number_with_max_iterations["count"] = total

print(number_with_max_iterations)
