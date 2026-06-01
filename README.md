First application (FTP - UDP):
This application is working on transferring files from path to path and changing also the name of the files. The application consists of server code and client code; The server code listens for incoming data, and the client code sends the data to the server. In this case, the data is the content of a file being transferred from one location to another on the same computer.
First, importing the socket and the os libraries, setting the local IP address using gethostbyname() or from the command prompt: config/all and get the ipv4 of the device, port number, and socket address of the server, creating a UDP socket using the socket module, binding the IP address and port number to the socket.
Second, starting an infinite loop to continuously receive data from the client, within the loop, receive the data and the address of the client that sent the data, decoding the received data and splitting it into the old filename, new filename, and file data, renaming the file and save it into another path on the server. Finally, printing a confirmation message that the file has been renamed and saved, repeating the loop until the server is stopped.
For the client:
First, import the socket and the os libraries, setting the IP address, port number, and socket address of the server, creating a UDP socket using the socket module.
Second, opening and reading the content of the file that will be transferred from one location to another, combining the old filename, new filename, and file data into a single string, encoding the data string into bytes and sending it to the server.
Finally, close the connection to the server and print a confirmation message that the file data has been sent to the server.
In conclusion, this application allows the server to receive a file from the client, rename the file, and save it in another location on the server. The server listens to incoming data from the client and processes it accordingly. The client sends the file data to the server for processing. Both the server and client are implemented using Python and the socket module. The client and server communicate over a UDP socket. This application can be useful in scenarios where you need to transfer a file between different locations on the same computer. The server code consists of a few primary steps.

----------------------------------------------------
Second application (SMTP - TCP):
This Python script allows sending emails from a user-specified sender's email address to a recipient's email address. The script uses the smtplib library to establish a connection with Gmail's SMTP server, which facilitates email sending. The user inputs the sender and receiver email addresses, the subject, and the message content, and the script sends the email accordingly.
Key Components:
1.User Inputs:
oThe script prompts the user to enter:
▪Sender's email
▪Receiver's email
▪Subject of email
▪The body message of the email
<img width="843" height="109" alt="image" src="https://github.com/user-attachments/assets/68686c47-da5e-48f8-a1c8-f87a0a4ca3fe" />
2.Email Content:
o The input subject and message are combined to form the email body, with the subject appearing at the top.
3.SMTP Server Connection:
o The script establishes a connection to Gmail’s SMTP server using the server’s address (smtp.gmail.com) and port (587).
o The connection is secured using TLS (server.starttls()), ensuring that the communication between the client and the server is encrypted.
4.Authentication:
o The script logs into the Gmail account using the sender’s email and an application-specific password (provided in the code as a placeholder: "minb gnnj qcmz cjwz").
5.Sending the Email:
o The script uses the sendmail method from the smtplib library to send the email, which takes the sender's email, the recipient's email, and the email content (subject and message).
6.Confirmation:
o After successfully sending the email, a confirmation message is printed to the console indicating that the email has been sent.

-------------------------------------------------------------

Third Application (Chat - UDP)
UDP Chat Client: A Python Implementation
This report outlines a Python-based chat client built on the UDP (User Datagram Protocol). Designed for lightweight and real-time communication, the application uses socket programming and multithreading to enable seamless interaction between users and the server.
Key Functionalities
1.Connection Setup:
oThe client initializes with a server address (default: localhost and port 12345) and creates a UDP socket.
oThe user is prompted to enter a username, which is used for identification in the chat.
2.Message Sending:
o Messages are sent to the server using the send message method, which encodes the message and sends it via the UDP socket.
o Special commands like CONNECT and DISCONNECT signal the server about client connection status.
3.Message Receiving:
o A separate thread runs the receive messages method, listening for incoming messages from the server and displaying them to the user.
4. Graceful Exit:
o Users can type exit to leave the chat. This sends a disconnect message to the server and stops the client.
5.Multithreading:
o The use of a separate thread for receiving messages ensures the program remains responsive while handling both sending and receiving tasks.
Example Interaction
• The user starts the client and provides a username.
• The client sends a CONNECT message to the server.
• The user sends messages to the server, which are broadcast to other connected clients.
• Messages from other users are displayed on the client’s terminal.
• Typing exit disconnects the client from the server.
