geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

filtered_birds = list(filter(lambda bird: bird not in geese, birds))
print(filtered_birds)
