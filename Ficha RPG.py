#######################################
############# Ficha RPG ###############
#######################################


# ########## Basic ##############

nome_char = "Ahmrit"
player = "Mossato"
race = "Moreau - Snake"
job = "clerigo - 5"
tendencia = "neutro"
sex = "M"
age = "16"
divindade = "Thyatis"
tamanho = "2 Metros"

print(nome_char, player, sep="# #")
print(race, job, tendencia,)
print(sex, age, divindade, tamanho)

########## Atributos ########

afor = 16
ades = 12
acon = 14
aint = 12
asab = 17
acar = 14

# MOD FORÇA

print("Força", afor)

if (afor == 30) or (afor == 31):
    mod_afor = 10
elif (afor == 28) or (afor == 29):
    mod_afor = 9
elif (afor == 26) or (afor == 27):
    mod_afor = 8
elif (afor == 24) or (afor == 25):
    mod_afor = 7
elif (afor == 22) or (afor == 23):
    mod_afor = 6
elif (afor == 20) or (afor == 21):
    mod_afor = 5
elif (afor == 18) or (afor == 19):
    mod_afor = 4
elif (afor == 16) or (afor == 15):
    mod_afor = 3
elif (afor == 14) or (afor == 13):
    mod_afor = 2
elif (afor == 12) or (afor == 11):
    mod_afor = 1
else:
    mod_afor = 0

print ("modificador de força", mod_afor)

# MOD DESTREZA

print("Destreza", ades)

if (ades == 30) or (ades == 31):
    mod_ades = 10
elif (ades == 28) or (ades == 29):
    mod_ades = 9
elif (ades == 26) or (ades == 27):
    mod_ades = 8
elif (ades == 24) or (ades == 25):
    mod_ades = 7
elif (ades == 22) or (ades == 23):
    mod_ades = 6
elif (ades == 20) or (ades == 21):
    mod_ades = 5
elif (ades == 18) or (ades == 19):
    mod_ades = 4
elif (ades == 16) or (ades == 15):
    mod_ades = 3
elif (ades == 14) or (ades == 13):
    mod_ades = 2
elif (ades == 12) or (ades == 11):
    mod_ades = 1
else:
    mod_ades = 0

print ("modificador de destreza", mod_ades)

# MOD CON

print("Constituição", acon)

if (acon == 30) or (acon == 31):
    mod_acon = 10
elif (acon == 28) or (acon == 29):
    mod_acon = 9
elif (acon == 26) or (acon == 27):
    mod_acon = 8
elif (acon == 24) or (acon == 25):
    mod_acon = 7
elif (acon == 22) or (acon == 23):
    mod_acon = 6
elif (acon == 20) or (acon == 21):
    mod_acon = 5
elif (acon == 18) or (acon == 19):
    mod_acon = 4
elif (acon == 16) or (acon == 15):
    mod_acon = 3
elif (acon == 14) or (acon == 13):
    mod_acon = 2
elif (acon == 12) or (acon == 11):
    mod_acon = 1
else:
    mod_acon = 0

print ("modificador de constituição", mod_acon)

# MOD INT

print("Inteligência", aint)

if (aint == 30) or (aint == 31):
    mod_aint = 10
elif (aint == 28) or (aint == 29):
    mod_aint = 9
elif (aint == 26) or (aint == 27):
    mod_aint = 8
elif (aint == 24) or (aint == 25):
    mod_aint = 7
elif (aint == 22) or (aint == 23):
    mod_aint = 6
elif (aint == 20) or (aint == 21):
    mod_aint = 5
elif (aint == 18) or (aint == 19):
    mod_aint = 4
elif (aint == 16) or (aint == 15):
    mod_aint = 3
elif (aint == 14) or (aint == 13):
    mod_aint = 2
elif (aint == 12) or (aint == 11):
    mod_aint = 1
else:
    mod_aint = 0

print("modificador de inteligencia", mod_aint)

# MOD SAB

print("Sabedoria", asab)

if (asab == 30) or (asab == 31):
    mod_asab = 10
elif (asab == 28) or (asab == 29):
    mod_asab = 9
elif (asab == 26) or (asab == 27):
    mod_asab = 8
elif (asab == 24) or (asab == 25):
    mod_asab = 7
elif (asab == 22) or (asab == 23):
    mod_asab = 6
elif (asab == 20) or (asab == 21):
    mod_asab = 5
elif (asab == 18) or (asab == 19):
    mod_asab = 4
elif (asab == 16) or (asab == 17):
    mod_asab = 3
elif (asab == 14) or (asab == 15):
    mod_asab = 2
elif (asab == 12) or (asab == 13):
    mod_asab = 1
else:
    mod_asab = 0

print("modificador de sabedoria", mod_asab)