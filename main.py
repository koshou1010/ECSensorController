import server, utils, catchdata, random, socket
import sys
import webview
import threading
from cefpython3 import cefpython as cef

HOST='127.0.0.1'
RANDOM_PORT = True
RANDOM_PORT_RANGE=(20000, 60000)
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
    

def run_server():
    server.app.run(debug=False, host=HOST,port=got_port())

def set_cef():
    # To pass custom settings to CEF, import and update settings dict
    from webview.platforms.cef import settings, browser_settings
    #https://github.com/cztomczak/cefpython/blob/master/api/ApplicationSettings.md#application-settings
    settings.update(
        {
        'debug': True,
        'remote_debugging_port':5000,
        'context_menu':
            {
                "enabled" :True,
                "navigation" :True,
                "print":True,
                "view_source" :True,
                "external_browser" :True,
                "devtools" :True
            }
        }
    )
    #https://github.com/cztomczak/cefpython/blob/master/api/BrowserSettings.md#browser-settings
    browser_settings.update({
        'file_access_from_file_urls_allowed':True,
        'web_security_disabled':True,
        'universal_access_from_file_urls_allowed':True,
    })

    
def run_pywebview():
    webview.create_window('EC Sensor Controller', server.app, height=600, width=1000)
    webview.start(gui='cef')
    sys.exit()



if __name__ == '__main__':
    server.preprocessing()
    t = threading.Thread(target=run_server)
    t.daemon = True
    t.start()
    set_cef()
    run_pywebview()