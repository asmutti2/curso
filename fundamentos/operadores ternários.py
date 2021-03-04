esta_chuvendo = True
print('Minhas roupas estão' + (" secas.", " sujas")[esta_chuvendo]) #para True, puxa o mais distante, para false, o contrario



weekend_league_sub = False
print('Você ' + ("não está inscrito na Weekend League.",
                 "está inscrito na Weekend League.")[weekend_league_sub])


print('você' + ("está inscrito na Weekend League" if weekend_league_sub
                 else " não está inscrito na Weekend League."))

print("{}, {}".format("você está inscirto na weekend league", 
                         "Você não está inscrito"))
