file = open("README")
file_copy = open("README-复件", "a")

text = file.read()
file_copy.write(text)

file.close()
file_copy.close()
