things = ["mozzarella", "cinderella", "salmonella"]

for i in range(len(things)):
    if "ella" in things[i]:
        things[i] = things[i].capitalize()
    if "mozzarella" in things[i]:
        things[i] = things[i].upper()

things = [item for item in things if "salmonella" not in item]

print(things)