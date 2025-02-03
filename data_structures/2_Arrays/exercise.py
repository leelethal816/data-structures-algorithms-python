expenses = [2200, 2350, 2600, 2130, 2190]

print("1. ------")

feb_over_jan = expenses[1] - expenses[0]
print(f"1. {feb_over_jan}")

total_fq = 0
for i in range(len(expenses) - 2):
    total_fq += expenses[i]
print(f"2. {total_fq}")

exactly_2000 = False
for i in expenses:
    if i == 2000:
        exactly_2000 = True
print(f"3. {exactly_2000}")

expenses.append(1980)
print(f"4. {expenses}")

expenses[3] -= 200
print(f"5. {expenses}")

print("------")

print("2. ------")

heros=['spider man','thor','hulk','iron man','captain america']

print(f"1. {len(heros)}")

heros.append('black panther')
print(f"2. {heros}")

heros.pop()
heros.insert(3, 'black panther')
print(f"3. {heros}")

heros[1:3] = ["doctor strange"]
print(f"4. {heros}")

heros.sort()
print(f"5. {heros}")

print("------")

print("3. ------")

max_n = int(input("Give a big odd number: "))
odd_list = []
for i in range(max_n):
    if i % 2 != 0:
        odd_list.append(i)

print(f"{odd_list}")

print("------")