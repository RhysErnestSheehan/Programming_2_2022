"""Rhys Sheehan CP1404 Prac 03 files"""

# Program 1
# name = input("What is your name?:")
# out_file = open("name.txt", 'w')
# print(name, file=out_file)
# out_file.close()

# Program 2
# in_file = open("name.txt", "r")
# name = in_file.readline()
# print("Your name is", name)
# in_file.close()

# Program 3
in_file = open("numbers.txt", "r")
line_1 = int(in_file.readline())
line_2 = int(in_file.readline())
answer = line_1 + line_2
print(answer)
in_file.close()
