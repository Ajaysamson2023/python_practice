# Practice while loop:
i = 1
while i <= 10:
    print(i)
    i += 1
print("------------------Continue-----------------------------")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1

print("------------------Break-----------------------------")

i = 1
while i <= 20:
    if i == 5:
        break
    print(i)
    i += 1