import socket;
import time;
import random;
import datetime
from token import STAR;

def app_banner():
    print("""
$$$$$$$\\             $$$$$$\\                      $$\\                  $$\\                         
$$  __$$\\           $$  __$$\\                     $$ |                 $$ |                        
$$ |  $$ |$$\\   $$\\ $$ /  \\__| $$$$$$\\   $$$$$$$\\ $$ |  $$\\  $$$$$$\\ $$$$$$\\    $$$$$$\\   $$$$$$\\  
$$$$$$$  |$$ |  $$ |\\$$$$$$\\  $$  __$$\\ $$  _____|$$ | $$  |$$  __$$\\\\_$$  _|  $$  __$$\\ $$  __$$\\ 
$$  ____/ $$ |  $$ | \\____$$\\ $$ /  $$ |$$ /      $$$$$$  / $$$$$$$$ | $$ |    $$$$$$$$ |$$ |  \\__|
$$ |      $$ |  $$ |$$\\   $$ |$$ |  $$ |$$ |      $$  _$$<  $$   ____| $$ |$$\\ $$   ____|$$ |      
$$ |      \\$$$$$$$ |\\$$$$$$  |\\$$$$$$  |\\$$$$$$$\\ $$ | \\$$\\ \\$$$$$$$\\  \\$$$$  |\\$$$$$$$\\ $$ |      
\\__|       \\____$$ | \\______/  \\______/  \\_______|\\__|  \\__| \\_______|  \\____/  \\_______|\\__|      
          $$\\   $$ |                                                                               
          \\$$$$$$  |                                                                               
           \\______/                                                                                
""");

def process_request(request):
    # Hence the operation took x second
    random_number = random.randint(1, 10);

    return f"The request {request} was processed in {random_number} second(s)";

if __name__ == "__main__":
    SOCKET_PORT = 55717;
    app_banner();
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("localhost", SOCKET_PORT));
        server_socket.listen();
        print(f"Server listening on localhost:{SOCKET_PORT}");

        while True:
            client_socket, address = server_socket.accept();
            start_timer = time.time();            

            current_time = "["+ time.strftime("%Y-%m-%d %H:%M:%S") +"]";            

            print(f"{current_time} Connection from {address}");

            # Handle incoming requests
            request = client_socket.recv(1024).decode();
            response = process_request(request);
            
            # Sens response back to client
            client_socket.sendall(response.encode());
            client_socket.close();

            timer = time.time() - start_timer;            
            print(f"i -> {request} The process was actually ran at {timer} second(s)");
