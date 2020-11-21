import random2

hola = ["Hola", "Buenas", "Saludos", "Hola!", "Buenas!", "Saludos!"]
elhola = random2.choice(hola)

hoy = ["hoy", "esta vez", "esta ocasion", "esta oportunidad",]
elhoy = random2.choice(hoy)

tetraemos = ["te traemos", "te compartimos"]
eltetraemos = random2.choice(tetraemos)

una = ["una pelicula", "una cinta", "un filme"]
eluna = random2.choice(una)

denombre = ["de nombre", "que se llama", "llamada"]
eldenombre = random2.choice(denombre)

nombre = input("El nombre: ")

dicen = ["dicen", "comentan", "he escuchado", "he oido"]
eldicen = random2.choice(dicen)

buenisima = ["que esta buenisima", "que esta re buena", "que esta genial", "que esta bien buena"]
elbuenisima = random2.choice(buenisima)

print(f"{elhola} {elhoy} {eltetraemos} {eluna} {eldenombre} {nombre} {eldicen} {elbuenisima} ")
