
data merge entity @s {DeathTime:200s,Silent:1b}

data remove entity @s DeathLootTable

tp @s ~ -1000 ~

summon minecraft:elder_guardian ~ ~ ~ {Tags:["ob.transformed"]}