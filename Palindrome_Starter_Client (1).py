import socket  # Help communicate with the server

# Define the server address and port to connect to
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

def start_client():
    #Start the client then connects to the server and provides a menu for user interaction.

    #Make a TCP socket and use it in a with
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))  # Connect to the server
        
        while True:
            # Display the menu options for the user
            print("\nMenu:")
            print("1. Simple Palindrome Check")  # Check to see if the input string is a palindrome
            print("2. Complex Palindrome Check")  # Check to see if the input string can be rearranged into a palindrome
            print("3. Exit")  # Exit
            choice = input("Enter choice (1/2/3): ").strip()  # Get user input

            if choice == '1':  # User picks simple palindrome check
                input_string = input("Enter the string to check: ")
                message = f"simple|{input_string}"  # message for the server
            elif choice == '2':  # User picks complex palindrome check
                input_string = input("Enter the string to check: ")
                message = f"complex|{input_string}"  # mesage for the server
            elif choice == '3':  # User decides to exit
                print("Exiting the client...")
                break  # Exit the loop and close the client
            else:
                print("Invalid choice. Please try again.")  # invalid input message
                continue  # Go back to the menu

            # Send messages to the server
            client_socket.send(message.encode())

            # Receive and display the server response
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")

# Run the client when the script is ran
if __name__ == "__main__":
    start_client()
