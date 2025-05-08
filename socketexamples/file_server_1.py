import socket
import os

# Server-side
def server_program():
    host = socket.gethostname()
    port = 5074 # Arbitrary non-privileged port
    server_socket = socket.socket()
    print("socket created")
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    #filename = conn.recv(1024).decode()
    #print("Receiving file:", filename)

    with open("test.txt", "wb") as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received successfully.")
    conn.close()
    server_socket.close()





if __name__ == '__main__':
    import threading
    print("starting the server")
    # Run server in a separate thread so it doesn't block the client
    server_thread = threading.Thread(target=server_program)
    server_thread.start()
