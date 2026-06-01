import socket
import threading

# Define the UDP client class
class UDPChatClient:
    def __init__(self, host='localhost', port=12345):
        self.server_address = (host, port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.username = input("Enter your username: ")
        self.running = True

    def receive_messages(self):
        """Handle receiving messages from the server"""
        while self.running:
            try:
                message, _ = self.client_socket.recvfrom(4096)
                print(f"Received: {message.decode()}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        """Send a message to the server"""
        self.client_socket.sendto(message.encode(), self.server_address)

    def close(self):
        """Send a disconnect message and close the client socket"""
        self.running = False
        self.send_message(f"DISCONNECT:{self.username}")
        self.client_socket.close()

    def start(self):
        """Start the client to send and receive messages"""
        # Send the connection request to the server
        self.send_message(f"CONNECT:{self.username}")
        
        # Start a thread to receive messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

        while self.running:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                print("Exiting chat...")
                self.close()
            else:
                self.send_message(message)


if __name__ == "__main__":
    client = UDPChatClient()
    client.start()

