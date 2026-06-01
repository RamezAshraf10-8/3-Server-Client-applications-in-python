import socket

# Define the UDP server class
class UDPChatServer:
    def __init__(self, host='localhost', port=12345):
        self.server_address = (host, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(self.server_address)
        self.clients = {}  # Store clients with their usernames

    def start(self):
        print(f"Server started. Listening on {self.server_address}...")
        while True:
            # Receive messages from clients
            message, client_address = self.server_socket.recvfrom(4096)
            decoded_message = message.decode()

            if decoded_message.startswith("CONNECT:"):
                username = decoded_message.split(":")[1].strip()
                self.clients[client_address] = username
                print(f"New client connected: {username} ({client_address})")
                # Send a welcome message back to the new client
                welcome_message = f"Welcome {username}! You are connected to the chat."
                self.server_socket.sendto(welcome_message.encode(), client_address)
                
            elif decoded_message.startswith("DISCONNECT:"):
                username = self.clients.pop(client_address, None)
                if username:
                    print(f"Client {username} ({client_address}) disconnected.")
                    disconnect_message = f"{username} has left the chat."
                    # Notify all other clients about the disconnect
                    for client in self.clients:
                        self.server_socket.sendto(disconnect_message.encode(), client)
            
            else:
                # Forward the received message to all other clients
                for client, username in self.clients.items():
                    if client != client_address:
                        self.server_socket.sendto(f"{self.clients[client_address]}: {decoded_message}".encode(), client)
                    print(f"Forwarded message from {client_address} to {client}: {decoded_message}")


if __name__ == "__main__":
    server = UDPChatServer()
    server.start()