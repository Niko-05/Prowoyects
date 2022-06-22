inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}




def displayInventory(inventory):
	print('Inventory:')

	totalItems = 0
	for k,v in inventory.items():
		totalItems = totalItems + v
		print(str(v) + ' ' + k)

	print('Total number of items: ' + str(totalItems))
	print('')


def addToInventory(inventory, addedItems):
	for i in range(len(addedItems)):
		item = addedItems[i]
		inventory.setdefault(item, 0)
		inventory[item] = inventory[item] + 1

	return inventory





displayInventory(inventory)

newInventory = {'furries': 2}
dragonLoot = ['gold coin', 'furries', 'gold coin', 'ruby']
newInventory = addToInventory(newInventory, dragonLoot)


displayInventory(newInventory)