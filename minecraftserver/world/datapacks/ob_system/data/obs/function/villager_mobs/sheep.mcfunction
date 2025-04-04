summon sheep

playsound minecraft:entity.villager.work_shepherd neutral @a[distance=..16]

advancement revoke @s only obs:technical/mob_trade/sheep
clear @a #obs:spawn_eggs
schedule function obs:mobs/destroy_egg 1t replace