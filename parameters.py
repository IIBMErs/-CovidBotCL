# Nombre bot
NOMBRE_BOT = "@coronaChile_bot"

# Path Base de datos
PATH_BASE = 'base.sqlite'

# Path a archivos .csv necesarios para obtener la información en datos
# Se optive de producto 1 Archivo "Covid-19.csv"
PATH_CASOS_INCREMENTALES = "../Datos-COVID19/output/producto1/Covid-19.csv"

# Se obtiene de producto 25 archivo "CasosActualesPorComuna"
PATH_CASOS_DIARIOS = "../Datos-COVID19/output/producto25/CasosActualesPorComuna.csv"

# Obtener lista de Comunas, se obtiene de producto 1, archivo "Covid-19.csv"
PATH_LISTA_COMUNAS = "../Datos-COVID19/output/producto1/Covid-19.csv"

# Fases de las comunas
PATH_FASES = "../Datos-COVID19/output/producto74/paso_a_paso.csv"

# Ruta al github https://github.com/MinCiencia/Datos-COVID19
PATH_COVID = "../Datos-COVID19"


# Datos 
INFO_DATOS = [
    ["Casos Incrementales","casosIncrementales",PATH_CASOS_INCREMENTALES],
    ["Casos Diarios","casosDiarios",PATH_CASOS_DIARIOS],
    ["Incidencia","incidencia","asdfasd"],
    ["Fase comuna","faseComuna","asdf"]
] 