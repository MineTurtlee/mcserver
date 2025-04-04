
execute if entity @s[advancements={obs:technical/mob_trade/chicken={plains=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={swamp=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={taiga=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={snowy=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={desert=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={jungle=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/chicken={savanna=true}}] run summon chicken ~ ~ ~ {IsChickenJockey:0b,variant:"minecraft:warm"}

playsound minecraft:entity.villager.work_butcher neutral @a[distance=..16]

advancement revoke @s only obs:technical/mob_trade/chicken
clear @a #obs:spawn_eggs
schedule function obs:mobs/destroy_egg 1t replace