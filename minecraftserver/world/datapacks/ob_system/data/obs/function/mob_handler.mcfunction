tag @s[type=skeleton,predicate=obs:chances/7,predicate=obs:nether] add obs.replace
tag @s[type=skeleton,predicate=obs:chances/2,predicate=obs:snowy_slopes] add obs.replace
tag @s[type=squid,predicate=obs:chances/3] add obs.replace
execute unless entity @p[distance=..10] run tag @s[type=cod,predicate=obs:chances/2] add obs.replace
execute if block ~ ~-1 ~ minecraft:soul_soil run tag @s[type=skeleton,predicate=obs:chances/2,predicate=obs:nether] add obs.replace
tag @s[type=zombified_piglin,predicate=obs:chances/8,predicate=obs:nether,predicate=obs:blaze] add obs.replace

execute as @e[type=skeleton,tag=obs.replace,predicate=obs:nether] run summon wither_skeleton
execute as @e[type=skeleton,tag=obs.replace,predicate=obs:snowy_slopes] run summon stray
execute as @e[type=zombified_piglin,tag=obs.replace] run summon blaze ~0.0625 ~ ~
execute as @e[type=zombified_piglin,tag=obs.replace] run summon blaze ~-0.0625 ~ ~
execute as @e[type=enderman,tag=obs.replace] run summon shulker
execute as @e[type=squid,tag=obs.replace] run summon guardian
execute as @e[type=cod,tag=obs.replace] run summon salmon

data merge entity @s[type=minecraft:skeleton_horse] {Tame:1b}

tp @e[tag=obs.replace] ~ -1000 ~

tag @s add obs.process