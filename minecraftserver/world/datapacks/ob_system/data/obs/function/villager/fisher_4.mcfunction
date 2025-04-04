
# Trade 1
loot replace entity @s weapon.mainhand 2 loot obs:gameplay/trades/fisher_2
data modify entity @s Offers.Recipes[6].buy set from entity @s equipment.mainhand
data modify entity @s Offers.Recipes[6].sell set from entity @s equipment.offhand

item replace entity @s weapon.mainhand with air
item replace entity @s weapon.offhand with air
