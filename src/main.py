import backend.server as server
import backend.utils as utils
import backend.catchdata as catchdata
import setting
import sys
import webview
import threading
from cefpython3 import cefpython as cef



def run_server():
    server.app.run(debug=False, host=setting.HOST,port=setting.got_port())

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
    # server.preprocessing()
    t = threading.Thread(target=run_server)
    t.daemon = True
    t.start()
    set_cef()
    run_pywebview()