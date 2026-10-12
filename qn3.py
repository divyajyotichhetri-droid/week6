from colorama import Fore, init

init(autoreset=True)

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print(Fore.CYAN + f"Student Name: {name}")

if marks >= 40:
    print(Fore.GREEN + "PASS")
else:
    print(Fore.RED + "FAIL")
    