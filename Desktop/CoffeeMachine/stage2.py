cups = int(input('Write how many cups of coffee you will need:'))

WATER = 200
MILK = 50
COFFEE = 15

print(f'For {cups} cups of coffee you will need:')
print(f'{WATER * cups} ml of water')
print(f'{MILK * cups} ml of milk')
print(f'{COFFEE * cups} g of coffee beans')