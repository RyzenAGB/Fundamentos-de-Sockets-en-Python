import socket

# 1. Crear socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Asociar a una IP y puerto (Bind)
servidor.bind(('127.0.0.1', 5000))

# 3. Escuchar conexiones (Listen) - permitimos 1 en la cola
servidor.listen(1)
print("Servidor TCP iniciado. Esperando conexión en el puerto 5000...")

# 4. Aceptar la conexión entrante (Accept)
# Esto detiene la ejecución hasta que un cliente se conecte
conexion, direccion = servidor.accept()
print(f"¡Conexión exitosa desde {direccion}!")

# 5. Recibir mensaje del cliente (Recv)
mensaje_recibido = conexion.recv(1024).decode('utf-8')
print(f"Mensaje del cliente: {mensaje_recibido}")

# 6. Enviar respuesta al cliente (Send)
respuesta = "Hola cliente, soy el servidor TCP. Mensaje recibido.".encode('utf-8')
conexion.send(respuesta)

# 7. Cerrar conexión (Close)
conexion.close()
servidor.close()
print("Conexión TCP cerrada.")