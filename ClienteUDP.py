import socket

# 1. Crear socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_servidor = ('127.0.0.1', 6000)

# 2. Enviar mensaje sin conexión previa (Sendto)
mensaje = "¡Hola servidor! Paquete rápido desde el cliente UDP.".encode('utf-8')
cliente.sendto(mensaje, direccion_servidor)
print("Mensaje UDP enviado.")

# 3. Recibir respuesta (Recvfrom)
datos_respuesta, origen = cliente.recvfrom(1024)
respuesta = datos_respuesta.decode('utf-8')

# 4. Mostrar resultado
print(f"Respuesta del servidor: {respuesta}")

# 5. Cerrar socket
cliente.close()