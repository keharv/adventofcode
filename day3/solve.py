file_input = open('input.txt').readlines()

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#part 1
prio = 0
for line in file_input:
    line = line.strip()
    half = len(line) // 2
    firstCompartment = line[:half]
    secondCompartment = line[half:]
    for c in firstCompartment:
        if c in secondCompartment:
            prio += (priorities.index(c) + 1)
            break
print(f"Part 1 Answer: {prio}")

#part 2
prio = 0 
i = 0
while(i < len(file_input)):
    comp1 = file_input[i].strip()
    comp2 = file_input[i+1].strip()
    comp3 = file_input[i+2].strip()
    for char in comp1:
        if char in comp2 and char in comp3:
            prio += (priorities.index(char) + 1)
            break
    i += 3
print(f"Part 2 Answer: {prio}")