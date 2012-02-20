def take_potion():
	global inventory
	global health
	life = 0
	if "potion" in inventory:
		inventory.remove("potion")
		health = health+10
	else:
		print ("You don't have any potion")
		

		
health = 10
inventory = ["potion","potion","potion"]
print ("health=",health)
print (inventory)
print ("You take a potion")
take_potion()
print ("health=",health)
print (inventory)
print ("You take a potion")
take_potion()
print ("health=",health)
print (inventory)
print ("You take a potion")
take_potion()
print ("health=",health)
print (inventory)
print ("You take a potion")
take_potion()