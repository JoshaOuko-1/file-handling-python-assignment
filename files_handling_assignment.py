# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("It's all good\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    print("Contents of my_file.txt:")
    for line in file:
        print(line.strip())

# File Appending
with open("my_file.txt", "a") as file:
    file.write("My name is Joshua \n")
    file.write("I wish PLP didnt remove the 10 oclock classes\n")
    file.write("I struggle with the early morning and evening classes \n")

print("\nContent after appending:")
with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip())
