
text = "tesla"

for char in text:
    print(char)
    break

print("bye")

names = ["Dani", "Leti", "Alan", "Pablo"]

for name in names:
    print(name)
    check = True

    if name == "Alan":
        continue

    if name == "Leti":
        break

    for char in name:
        print(char)

