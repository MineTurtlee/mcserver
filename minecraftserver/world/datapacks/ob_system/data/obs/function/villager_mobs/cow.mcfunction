
execute if entity @s[advancements={obs:technical/mob_trade/cow={plains=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={swamp=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:temperate"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={taiga=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={snowy=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:cold"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={desert=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={jungle=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:warm"}
execute if entity @s[advancements={obs:technical/mob_trade/cow={savanna=true}}] run summon cow ~ ~ ~ {IscowJockey:0b,variant:"minecraft:warm"}

playsound minecraft:entity.villager.work_butcher neutral @a[distance=..16]

advancement revoke @s only obs:technical/mob_trade/cow
clear @a #obs:spawn_eggs
schedule function obs:mobs/destroy_egg 1t replace