import socket
import threading
import hashlib
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

clients = []
usernames = {}
groups = {}

console = Console()

def handle_client(client_socket, addr):
    client_socket.send("Enter your username: ".encode())
    username = client_socket.recv(1024).decode().strip()
    client_socket.send("Enter your password: ".encode())
    password = client_socket.recv(1024).decode().strip()

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if username in usernames and usernames[username] != password_hash:
        client_socket.send("Authentication failed.\n".encode())
        client_socket.close()
        return

    usernames[username] = password_hash
    client_socket.send("Authentication successful!\n".encode())

    while True:
        client_socket.send("Available groups:\n".encode())
        group_list = "\n".join(groups.keys()) if groups else "No groups available."
        client_socket.send(f"{group_list}\n".encode())
        client_socket.send("Enter a group name to join or type 'create' to make a new group: ".encode())
        choice = client_socket.recv(1024).decode().strip()

        if choice.lower() == "create":
            client_socket.send("Enter the group name: ".encode())
            group_name = client_socket.recv(1024).decode().strip()
            if group_name not in groups:
                groups[group_name] = []
                client_socket.send(f"Group '{group_name}' created successfully.\n".encode())
            else:
                client_socket.send(f"Group '{group_name}' already exists.\n".encode())
        elif choice in groups:
            groups[choice].append(client_socket)
            client_socket.send(f"You joined the group: {choice}\n".encode())
            break
        else:
            client_socket.send("Invalid group choice. Try again.\n".encode())

    try:
        while True:
            msg = client_socket.recv(1024).decode()
            if msg == 'exit':
                break
            for group_member in groups[choice]:
                if group_member != client_socket:
                    group_member.send(f"{username}: {msg}\n".encode())
    except:
        groups[choice].remove(client_socket)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(5)
    console.print(Panel("Server Started", title="Real-time Chat Server", style="bold green"))
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

start_server()
