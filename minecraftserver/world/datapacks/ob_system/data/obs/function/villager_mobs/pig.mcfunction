
execute if entity @s[advancements={obs:technical/mob_trade/pig={plains=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={swamp=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={taiga=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={snowy=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={desert=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={jungle=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/pig={savanna=true}}] run summon pig ~ ~ ~ {IspigJockey:0b,variant:"minecraft:warm"}

playsound minecraft:entity.villager.work_butcher neutral @a[distance=..16]

advancement revoke @s only obs:technical/mob_trade/pig
clear @a #obs:spawn_eggs
schedule function obs:mobs/destroy_egg 1t replace