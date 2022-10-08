from uzivatel import uzivatel
print("Hello")

user1 = uzivatel("Lenka", "Dzurova", 20)
user2 = uzivatel("Fero", "Maly", 50)
user1 = user2
user1.print_info()