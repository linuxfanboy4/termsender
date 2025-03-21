# TermSender: Advanced Terminal-Based Chat Application

## Overview

TermSender is a sophisticated terminal-based chat application designed to facilitate secure and efficient communication between multiple users. Built with Python, this application leverages socket programming and multi-threading to enable real-time messaging within chat groups. TermSender is ideal for users who require a lightweight, command-line interface for communication, offering a robust solution for both individual and group interactions.

## Key Features

- **Secure Authentication**: Utilizes SHA-256 hashing for password storage, ensuring that user credentials are securely managed.
- **Real-Time Messaging**: Enables instant message delivery within chat groups, providing a seamless communication experience.
- **Dynamic Group Management**: Allows users to join existing chat groups or create new ones, fostering flexible and scalable communication channels.
- **Multi-Threading**: Employs threading to handle multiple client connections simultaneously, ensuring optimal performance and responsiveness.
- **Rich Text Interface**: Integrates the `rich` library to deliver an enhanced terminal experience with styled text and panels.

## Installation

To install and run TermSender, follow these steps:

1. **Download the Source Code**:
   Use `wget` to download the server and client scripts directly from the repository.

   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/termsender/refs/heads/main/src/server.py
   wget https://raw.githubusercontent.com/linuxfanboy4/termsender/refs/heads/main/src/cilent.py
   ```

2. **Run the Server**:
   Start the server by executing the `server.py` script. This will initialize the chat server and listen for incoming client connections.

   ```bash
   python server.py
   ```

3. **Run the Client**:
   Launch the client by executing the `cilent.py` script. This will prompt you to authenticate and connect to the server.

   ```bash
   python cilent.py
   ```

## Usage

### Server

The server script (`server.py`) is responsible for managing client connections, handling authentication, and facilitating message broadcasting within chat groups. Upon execution, the server binds to `localhost` on port `9999` and awaits client connections.

### Client

The client script (`cilent.py`) provides the user interface for interacting with the chat server. Upon execution, the client connects to the server and prompts the user for authentication. Once authenticated, the user can join or create chat groups and begin sending and receiving messages in real-time.

### Commands

- **Join or Create a Group**: Upon successful authentication, the client will display available chat groups and prompt the user to join an existing group or create a new one.
- **Send Messages**: Enter messages in the terminal to broadcast them to all members of the current chat group.
- **Exit**: Type `exit` to leave the chat group and disconnect from the server.

## Security Considerations

TermSender employs SHA-256 hashing to securely store user passwords, mitigating the risk of credential exposure. However, it is imperative to ensure that the server environment is adequately secured, particularly when deploying in production scenarios. Additional security measures, such as SSL/TLS encryption, should be considered to safeguard data in transit.

## Performance

TermSender is optimized for performance, utilizing multi-threading to handle multiple client connections concurrently. This ensures that the application remains responsive even under high load, making it suitable for both small-scale and large-scale deployments.

## Customization

TermSender is designed with extensibility in mind. Developers can easily modify the source code to introduce new features, such as private messaging, message persistence, or enhanced security protocols. The modular architecture facilitates seamless integration of additional functionalities.

## License

TermSender is released under the MIT License. This permissive license allows for broad usage, modification, and distribution, making it an excellent choice for both personal and commercial projects.

## Support

For support, issues, or feature requests, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/termsender). The development team is committed to providing timely assistance and ensuring the continued improvement of TermSender.
