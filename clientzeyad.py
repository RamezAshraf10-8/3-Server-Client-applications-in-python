import socket
# Server details
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
# File paths
oldfilename =r"C:\Users\risky\Desktop\test2\trial.txt"
newfilename =r"C:\Users\risky\Desktop\test\trial2.txt"
try:
    with open(oldfilename, 'r', encoding='utf-8') as file:
        filedata = file.read()
except FileNotFoundError:
    print(f"Error: File {oldfilename} not found.")
    exit(1)
except UnicodeDecodeError:
    print(f"Error: Unable to decode {oldfilename}. Try checking the file's encoding.")
    exit(1)

data = f"{oldfilename}|{newfilename}|{filedata}"
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(data.encode(FORMAT), ADDR)
    print("Successfully sent the filenames and file data to the server.")
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()