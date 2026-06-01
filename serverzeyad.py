import socket
import os
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
print("Server is starting.")
# Start a UDP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the IP and PORT to the server
serversocket.bind(ADDR)
print(f"Server is listening on {IP}:{PORT}.")
while True:
    try:
        data, addr = serversocket.recvfrom(SIZE)
        data = data.decode(FORMAT)
        print(f"Received data from {addr}.")
        try:
            oldfilename, newfilename, filedata = data.split("|", 2) # Use maxsplit=2 to prevent errors
        except ValueError:
            print(f"Error: Received malformed data from {addr}.")
        continue
        sanitized_newfilename = os.path.basename(newfilename)
        with open(sanitized_newfilename, 'w') as file:
            file.write(filedata)
            print(f"Successfully saved file as {sanitized_newfilename} from {addr}.")
    except Exception as e:
        print(f"Error: {e}")