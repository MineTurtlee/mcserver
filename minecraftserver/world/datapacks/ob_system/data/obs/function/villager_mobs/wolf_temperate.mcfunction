execute store result score #temp cob.block run random value 1..2

execute if score #temp cob.block matches 1 run summon wolf ~ ~ ~ {variant:"pale"}
execute if score #temp cob.block matches 2 run summon wolf ~ ~ ~ {variant:"woods"}