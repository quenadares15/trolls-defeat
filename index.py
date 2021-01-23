healts = 10
trolls = 0
damage = 2

while healts != 0:
    trolls += 1
    healts -= damage

    print("Bohater is defeating wrong troll, but taking damage and loosing ", damage, "health points\n")

print("Your bohater was great and defeat", trolls, "trolls.")
print("But your bohater is death now.")

input("\nPress Enter to exit\n")
