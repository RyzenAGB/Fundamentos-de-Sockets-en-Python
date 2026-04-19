import socket

# 1. Crear socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Asociar a una IP y puerto (Bind)
servidor.bind(('127.0.0.1', 6000))
print("Servidor UDP iniciado. Esperando mensajes en el puerto 6000...")

# 3. Recibir mensaje (Recvfrom)
# UDP devuelve los datos y la dirección exacta de quién los envió
datos, direccion_cliente = servidor.recvfrom(1024)
mensaje = datos.decode('utf-8')
print(f"Mensaje recibido de {direccion_cliente}: {mensaje}")

# 4. Responder al cliente (Sendto)
respuesta = "Hola cliente, soy el servidor UDP. Recibí tu paquete.".encode('utf-8')
servidor.sendto(respuesta, direccion_cliente)

# 5. Cerrar socket
servidor.close()