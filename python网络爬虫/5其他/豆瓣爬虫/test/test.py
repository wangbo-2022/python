a = [1, 2, 3]

for index in range(3):
    # a[index] = str(a[index])
    a[index] = '"' + a[index] + '"'

print(a)