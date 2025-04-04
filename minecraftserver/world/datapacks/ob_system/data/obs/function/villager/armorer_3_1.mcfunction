
data modify entity @s Offers.Recipes[4].maxUses set value 2

# Trade 1
loot replace entity @s weapon.mainhand 2 loot obs:gameplay/trades/armorer
data modify entity @s Offers.Recipes[4].buy set from entity @s equipment.mainhand
data modify entity @s Offers.Recipes[4].sell set from entity @s equipment.offhand

item replace entity @s weapon.mainhand with air
item replace entity @s weapon.offhand with air