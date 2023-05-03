total = input("Total Marbles")
total = int(total)
colour_list = []
colour_number = input("How many different colours?")
colour_number = int(colour_number)
answer = 1
for i in range(colour_number):
    colour_temp = input(f"How many in colour #{i+1}?")
    colour_temp = int(colour_temp)
    colour_list.append(colour_temp)
i = 0
target_number = input("How many in a row")
target_number = int(target_number)
target_colour = input("which colour (1,2,etc)?")
target_colour = int(target_colour) - 1
replacement = input("Is there replacement (1=yes, 0=no)?")
replacement = int(replacement)
if replacement == 0:
    for i in range(target_number):
        answer = answer / total
        answer = answer * colour_list[target_colour]
        colour_change = colour_list[target_colour] - 1
        colour_list[target_colour] = colour_change
        total = total - 1
        i = i +1
else:
    answer = target_number / total
    answer = answer * colour_list[target_colour]
print("The answer is: " , answer, "%")