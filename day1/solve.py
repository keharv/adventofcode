input = ''
with open('input.txt', 'r') as f:
    input = f.read()

elve_calories = []
current_elf = 0
for line in input.split('\n'):
    if line == '':
        elve_calories.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)


print("Most calories: " + max(elve_calories))
total_max = max(elve_calories)
elve_calories.remove(max(elve_calories))

total_max = max(elve_calories) + total_max
elve_calories.remove(max(elve_calories))

total_max = max(elve_calories) + total_max
print("Top 3 added together: " + total_max)
