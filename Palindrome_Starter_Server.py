import socket  #Provides networking capabilities for server-client communication
import threading  # Helps with handling amny clients concurrently
import logging  #Logs the messages to a file
import re  #uses regular expressions for the text processing.
from collections import Counter  #helps with counting character occurrences in string

# logs the record events in 'server_log.txt'
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define server address and port to connect to
HOST = 'localhost'
PORT = 12345

def handle_client(conn, addr):
    logging.info(f"Connected: {addr}")  #Log new connection
    try:
        while True:
            data = conn.recv(1024).decode()  # Receive data from client
            if not data:  #If ther is no data received then exit tge loop
                break
            logging.info(f"Received: {data}")  # Log received data
            
            response = process_request(data)  # process the client's request
            conn.send(response.encode())  # Send response back to the client
            logging.info(f"Sent: {response}")  #Log sent response
    finally:
        conn.close()  #Close the connection when its done
        logging.info(f"Disconnected: {addr}")  # Log disconnection

def process_request(data):
    #Find the right request type and perform the right text operation
    try:
        request_type, text = data.split('|', 1)  #Expecting a 'type|string' format
    except ValueError:
        return "Error. Use: type|string format"  #Error message if given a incorrect format

    text_cleaned = sanitize_text(text)  #Remove the special characters and make it lowercase
    
    #Checks the requests type and process accordingly
    if request_type == 'simple':
        return f"Palindrome check result: {check_palindrome(text_cleaned)}"
    elif request_type == 'complex':
        possible, swaps = min_swaps_to_palindrome(text_cleaned)
        return f"Palindrome reordering possible: {possible}\nComplexity Score: {swaps}" if possible else "False"
    else:
        return "Error: Invalid request type."  #Handle unknown request

def sanitize_text(text):
    
    #Remove the non-alphanumeric characters and convert it to lowercase
    
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def check_palindrome(text):
    
    #Checks to see if the given text is a palindrome
    
    cleaned_text = sanitize_text(text)  # Clean the input text
    return cleaned_text == cleaned_text[::-1]  # Compare with the reversed version

def min_swaps_to_palindrome(s):
    
    #Check and see if a string can be rearranged into a palindrome a count needs swap. 
    
    s = sanitize_text(s)  # Clean the input string
    
    # If it cant be rearranged into a palindrome or it is to short then return false
    if not can_form_palindrome(s) or len(s) <= 1:
        return False, 0

    s = list(s)  # Convert the string to a list for swapping
    n = len(s)
    swaps = 0  # Counter for number swaps
    left = 0
    right = n - 1

    # traverse the string from both ends towards the middle
    while left < right:
        if s[left] == s[right]:  # If its the same move inwards
            left += 1
            right -= 1
            continue

        k = right
        while k > left and s[k] != s[left]:  # Find matching character
            k -= 1

        if k == left:  #if there is no match found move the unmatched character to the middle
            mid = n // 2
            for i in range(left + 1, right + 1):
                if s[i] == s[left]:
                    for j in range(i, mid):
                        s[j], s[j+1] = s[j+1], s[j]  # Swap 
                        swaps += 1
                    break
            left += 1
            right -= 1
        else:
            for i in range(k, right):  # Move its character to the right places
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1
            left += 1
            right -= 1

    return True, swaps  # Return if palindrome formation is possible and its swap count

def can_form_palindrome(s):
    
    #Check if the string can be rearranged into a palindrome
    # A string can be a palindrome if it has atkeast at most one character with an odd number.
    
    cleaned_s = sanitize_text(s)  # Clean the input string
    return sum(v % 2 for v in Counter(cleaned_s).values()) <= 1  # Count the odd occurrences

def launch_server():
    
   # THis starts the server listens for client connection and create threads to handle them
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server.bind((HOST, PORT))  
    server.listen(5)  # Allow up to max 5 clients to wait in the queue
    logging.info(f"Server active on {HOST}:{PORT}")  # Log that the server is running
    
    try:
        while True:
            conn, addr = server.accept()  # Accept a new client connection
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))  # Make new thread
            client_thread.start()  # Start thread to handel a client
    except KeyboardInterrupt:
        logging.info("Server shutting down.")  # Log server shutdown on manual stop
    finally:
        server.close()  # Close  server socket

if __name__ == '__main__':
    launch_server()  # Run the server when the script is runs
