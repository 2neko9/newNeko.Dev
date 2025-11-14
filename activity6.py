print("\nThis is a simple python program that allows you to choose between Land, Water and Wind.")
print("Then it will dispaly a corresponding sentence.")

choice = input("Enter your choice here: ").strip().lower()
if choice == "water":
    print("Water is a Liquid that fills containers and flows.\n")
elif choice == "land":
    print("The solid portion of the Earth’s surface is called land.\n")
elif choice == "wind":
    print("Air in the atmosphere moves naturally and is called wind.\n")
else:
    print("Unknown component. Please enter wind, land, or water.\n")
