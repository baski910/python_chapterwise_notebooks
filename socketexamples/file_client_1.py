import socket
# Client-side
def client_program():
    host = socket.gethostname()
    port = 5074
    filename = "example.txt" # Replace with the path to your file

    client_socket = socket.socket()
    client_socket.connect((host, port))

    #client_socket.send(filename.encode())

    with open(filename, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print("File sent successfully.")
    client_socket.close()
    
if __name__ == '__main__':
    client_program()
