with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    contents = "Hello, this is my new string"
    file.write(contents)

with open("my_file.txt", mode="a") as file:
    contents = "Hello, this is my new string"
    file.write(contents)
