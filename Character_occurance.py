string = input("Enter your word ")
cha = input("Enter the specific number ")

i = 0
count = 0

while i < len(string):
    if string[i] == cha:
        count += 1
    i += 1

print("'",string, "'", " has ", count, "'", cha, "'")