names = ["Devin","Izzy", "Luna", "Charles", "Peter", "Ringo"]

new_list = [n.upper() for n in names if len(n) >= 5]


print(new_list)
