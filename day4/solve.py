file_input = open('./day4/input.txt').readlines()


#part 1
field = {}
overlaps = 0
for line in file_input:
    line = line.strip()
    duty = line.split(',')
    duty1 = duty[0].split('-')
    duty2 = duty[1].split('-')
    print(duty1)
    print(duty2)
    duty1_list = list(range(int(duty1[0]), int(duty1[1]) + 1))
    duty2_list = list(range(int(duty2[0]), int(duty2[1]) + 1))
    #check if all the numbers in duty1_list are in duty2_list
    if all(elem in duty2_list for elem in duty1_list):
        overlaps += 1
    elif all(elem in duty1_list for elem in duty2_list):
        overlaps += 1

print(f"Part 1 Answer: {overlaps}")

overlaps = 0
for line in file_input:
    line = line.strip()
    duty = line.split(',')
    duty1 = duty[0].split('-')
    duty2 = duty[1].split('-')
    print(duty1)
    print(duty2)
    duty1_list = list(range(int(duty1[0]), int(duty1[1]) + 1))
    duty2_list = list(range(int(duty2[0]), int(duty2[1]) + 1))
    #check if all the numbers in duty1_list are in duty2_list
    for num in duty1_list:
        if num in duty2_list:
            overlaps += 1
            break

print(f"Part 2 Answer: {overlaps}")