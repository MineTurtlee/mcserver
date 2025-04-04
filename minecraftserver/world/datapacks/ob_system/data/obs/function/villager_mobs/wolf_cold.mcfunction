execute store result score #temp cob.block run random value 1..3

execute if score #temp cob.block matches 1 run summon wolf ~ ~ ~ {variant:"ashen"}
execute if score #temp cob.block matches 2 run summon wolf ~ ~ ~ {variant:"black"}
execute if score #temp cob.block matches 3 run summon wolf ~ ~ ~ {variant:"chestnut"}