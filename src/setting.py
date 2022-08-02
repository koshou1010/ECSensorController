import random, socket, os

HOST='127.0.0.1'
RANDOM_PORT = True
RANDOM_PORT_RANGE=(20000, 60000)
ROOT_PATH=os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))

def tryPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind((HOST, int(port)))
        result = True
    except:
        print("Port {} is in use".format(port))
    sock.close()
    return result


def got_port() -> int:
    if RANDOM_PORT:
        while True:
            PORT=random.randint(*RANDOM_PORT_RANGE)
            if tryPort(PORT):
                return PORT
            else:
                continue
    else:
        return 5001
    

STATIC_GUI_DIR = os.path.join(ROOT_PATH, 'frontend', 'static')  
TEMPLATES_GUI_DIR = os.path.join(ROOT_PATH, 'frontend', 'templates') 