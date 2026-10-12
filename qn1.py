import pyjokes
for i in range (3):
    print(pyjokes.get_joke())
    print()

while True:
    choice = input("Want another joke? (yes/no): ").lower()

    if choice == "yes":
        print(pyjokes.get_joke())
    else:
        print("Goodbye!")
        break