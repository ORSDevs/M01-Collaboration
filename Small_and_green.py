small = input("Is the plant small? Answer True or False: ").lower() == "true"
green = input("Is the plant green? Answer True or False: ").lower() == "true"

if small and green:
    print("The plant is a Pea!")
elif small and not green:
    print("The plant is a Cherry!")
elif not small and green:
    print("The plant is a Watermelon!")
else:
    print("The plant is a Pumpkin!")
    