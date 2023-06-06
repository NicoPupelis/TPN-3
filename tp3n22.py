
import queue

cola = queue.Queue()

cola.put(("Tony Stark", "Iron Man", "M"))
cola.put(("Steve Rogers", "Capitán América", "M"))
cola.put(("Natasha Romanoff", "Black Widow", "F"))
cola.put(("Carol Danvers", "Capitana Marvel", "F"))
cola.put(("Scott Lang", "Ant-Man", "M"))

nombre_cm = ""
for p in list(cola.queue):
    if p[1] == "Capitana Marvel":
        nombre_cm = p[0]
print("Nombre del personaje de Capitana Marvel:", nombre_cm)

print("Superhéroes femeninos:")
for p in list(cola.queue):
    if p[2] == "F":
        print(p[1])

print("Personajes masculinos:")
for p in list(cola.queue):
    if p[2] == "M":
        print(p[0])

superheroe_sl = ""
for p in list(cola.queue):
    if p[0] == "Scott Lang":
        superheroe_sl = p[1]
print("Superhéroe del personaje Scott Lang:", superheroe_sl)

print("Datos de superhéroes/personajes cuyos nombres comienzan con S:")
for p in list(cola.queue):
    if p[0][0] == "S":
        print(p)
        
carol_danvers_en_cola = False
nombre_superheroe_carol_danvers = ""
for p in list(cola.queue):
    if p[0] == "Carol Danvers":
        carol_danvers_en_cola = True
        nombre_superheroe_carol_danvers = p[1]
if carol_danvers_en_cola:
    print("Carol Danvers se encuentra en la cola. Su nombre de superhéroe es:", nombre_superheroe_carol_danvers)
else:
    print("Carol Danvers no se encuentra en la cola.")

