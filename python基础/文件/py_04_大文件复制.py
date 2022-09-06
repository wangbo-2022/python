file = open("README")
file_copy = open("README-复件", "a")

while True:

    text = file.readline()

    if not text:
        break

    file_copy.write(text)

file.close()
file_copy.close()