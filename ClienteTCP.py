import socket

# 1. Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Conectarse al servidor (Connect)
cliente.connect(('127.0.0.1', 5000))
print("Conectado al servidor TCP.")

# 3. Enviar mensaje (Send)
mensaje = "¡Hola servidor! Soy un cliente TCP.".encode('utf-8')
cliente.send(mensaje)

# 4. Recibir respuesta (Recv)
respuesta_servidor = cliente.recv(1024).decode('utf-8')

# 5. Mostrar resultado
print(f"Respuesta del servidor: {respuesta_servidor}")

# 6. Cerrar conexión
cliente.close()