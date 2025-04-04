
execute if entity @s[advancements={obs:technical/mob_trade/wolf={plains=true}}] run function obs:villager_mobs/wolf_temperate
execute if entity @s[advancements={obs:technical/mob_trade/wolf={swamp=true}}] run function obs:villager_mobs/wolf_temperate
execute if entity @s[advancements={obs:technical/mob_trade/wolf={taiga=true}}] run function obs:villager_mobs/wolf_cold
execute if entity @s[advancements={obs:technical/mob_trade/wolf={snowy=true}}] run summon wolf ~ ~ ~ {variant:"snowy"}
execute if entity @s[advancements={obs:technical/mob_trade/wolf={desert=true}}] run function obs:villager_mobs/wolf_warm
execute if entity @s[advancements={obs:technical/mob_trade/wolf={jungle=true}}] run summon wolf ~ ~ ~ {variant:"rusty"}
execute if entity @s[advancements={obs:technical/mob_trade/wolf={savanna=true}}] run function obs:villager_mobs/wolf_warm

playsound minecraft:entity.villager.work_butcher neutral @a[distance=..16]

advancement revoke @s only obs:technical/mob_trade/wolf
clear @a #obs:spawn_eggs
schedule function obs:mobs/destroy_egg 1t replace