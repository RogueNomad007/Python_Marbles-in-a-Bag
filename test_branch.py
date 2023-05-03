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
order_array = []
for i in range(target_number)
    order_temp = input(f"What colour is drawn #{i+1}?")
    order_temp = int(order_temp)
    order_array.append(order_temp)
replacement = input("Is there replacement (1=yes, 0=no)?")
replacement = int(replacement)
if replacement == 0:
    for i in range(target_number):
        answer = answer / total
        answer = answer * colour_list[order_array[i+1]]
        colour_change = colour_list[order_array[i+1]] - 1
        colour_list[order_array[i+1]] = colour_change
        total = total - 1
        i = i +1
else
    for i in range(target_number)
        answer = answer / total
        answer = answer * colour_list[order_array[i + 1]]
print("The answer is: " , answer, "%")