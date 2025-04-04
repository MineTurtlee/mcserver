execute store result score #temp cob.block run random value 1..9

execute if score #temp cob.block matches 1 run summon wolf ~ ~ ~ {variant:"pale"}
execute if score #temp cob.block matches 2 run summon wolf ~ ~ ~ {variant:"snowy"}
execute if score #temp cob.block matches 3 run summon wolf ~ ~ ~ {variant:"woods"}
execute if score #temp cob.block matches 4 run summon wolf ~ ~ ~ {variant:"black"}
execute if score #temp cob.block matches 5 run summon wolf ~ ~ ~ {variant:"ashen"}
execute if score #temp cob.block matches 6 run summon wolf ~ ~ ~ {variant:"chestnut"}
execute if score #temp cob.block matches 7 run summon wolf ~ ~ ~ {variant:"rusty"}
execute if score #temp cob.block matches 8 run summon wolf ~ ~ ~ {variant:"spotted"}
execute if score #temp cob.block matches 9 run summon wolf ~ ~ ~ {variant:"striped"}

scoreboard players remove @e[tag=cob.block] cob.wolf 1
execute if score @e[tag=cob.block,limit=1] cob.wolf matches 1.. run function obs:crate/wolf
