f = open("in.txt", "r")

calories = []
i = 0
for line in f:
    if len(calories) <= i:
        calories.append([])

    if line != "\n":
        calories[i].append(int(line))
    else:
        i += 1

most_values = [0, 0, 0]

for elf in calories:
    enkelt_sum = 0
    for snack in elf:
        enkelt_sum += snack

    for i in range(len(most_values)):
        if enkelt_sum > most_values[i]:
            most_values[i] = enkelt_sum
            most_values.sort()
            break

print("largest value:", most_values)
print("total top three:", sum(most_values))
    