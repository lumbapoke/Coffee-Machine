print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need : ")
no_of_coffee = int(input())
a = int(min(water // 200, milk // 50, beans // 15))
if no_of_coffee == a:
    print("Yes, I can make that amount of coffee")
elif no_of_coffee > a:
    print("No, I can make only", a, "cups of coffee")
elif no_of_coffee < a:
    print("Yes, I can make that amount of coffee (and even ", a - no_of_coffee, "more than that)")