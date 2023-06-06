notificaciones = []

def eliminar_fb():
    global notificaciones
    notificaciones = [noti for noti in notificaciones if noti["app"] != "Facebook"]

def mostrar_notificaciones_twitter_python():
    global notificaciones
    for noti in notificaciones:
        if noti["app"] == "Twitter" and "Python" in noti["mensaje"]:
            print("Notificación de Twitter:", noti)

def contar_notificaciones_temp():
    global notificaciones
    contador_temporal = sum(1 for noti in notificaciones if "11:43" <= noti["hora"] <= "15:57")
    print("Cantidad de notificaciones almacenadas temporalmente:", contador_temporal)

notificaciones.append({"hora": "10:30", "app": "Facebook", "mensaje": "Hola"})
notificaciones.append({"hora": "11:50", "app": "Twitter", "mensaje": "Aprende Python"})
notificaciones.append({"hora": "13:20", "app": "Facebook", "mensaje": "Foto nueva"})
notificaciones.append({"hora": "14:30", "app": "Twitter", "mensaje": "Python es genial"})
notificaciones.append({"hora": "16:10", "app": "Facebook", "mensaje": "Evento próximo"})

eliminar_fb()
mostrar_notificaciones_twitter_python()
contar_notificaciones_temp()
