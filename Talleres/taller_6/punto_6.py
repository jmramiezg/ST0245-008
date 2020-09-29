futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

tomar_primero = lambda futbolistas: futbolistas[0]
futbolistasTup.sort(key=tomar_primero)
print(futbolistasTup)

inventosTup = [ (60,"robots con detreza"), (70,"Energia nuclear renovada"), (20,"Prediccion de nuños prematuros"), (30, "sonda intestinal"), (90, "vacuna contra el cancer"),
                (35, "chuleta in vitro"), (95, "purificadores de aire mundiales"), (15, "relojes medicos"), (40, "servicios sin sistema de alcantarillado"), (99,"Inteligencia artificial que habla") ]

take_first = lambda inventos: inventos[0]
inventosTup.sort(key=take_first)
print(inventosTup)