## Triggers when lightning strikes

execute as @e[type=minecraft:lightning_bolt] at @s as @e[type=minecraft:guardian,distance=..4] run function obs:lightning_strike/guardian

advancement revoke @s only obs:technical/lightning_strike