import socket
import threading
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def listen_for_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                console.print(Panel(Text(message, style="bold blue")))
        except:
            break

def send_message(sock):
    while True:
        message = input("Enter message: ")
        sock.send(message.encode())

def authenticate(sock):
    username = input("Enter username: ")
    sock.send(username.encode())
    password = input("Enter password: ")
    sock.send(password.encode())

    auth_response = sock.recv(1024).decode()
    console.print(Panel(Text(auth_response, style="bold green")))

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    authenticate(client_socket)

    listen_thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
    listen_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

client()
