import os, sys
import setting
import ana_utils
import logging
from datetime import datetime




def preprocessing():
    ana_utils.make_folder(setting.LOG_PATH)
    ana_utils.make_folder(setting.ANALYSIS_OUTPUT)
    for root, dirs, files in os.walk(setting.EXPERIMENT_PATH):
        for dir in dirs:
            ana_utils.make_folder(os.path.join(setting.ANALYSIS_OUTPUT, dir))
    
    now = datetime.now()
    current_time = now.strftime("%Y_%m_%d_%H")
    
    logging.basicConfig(level=logging.DEBUG, format=setting.FORMAT,    
        handlers=[
            logging.FileHandler('{}\\{}.log'.format(setting.LOG_PATH,current_time)),
            logging.StreamHandler(sys.stdout)
            ]
    )
    
if __name__ == '__main__':
    preprocessing()
    analyser = ana_utils.AnalysisSingleRound()
    analyser.plot_delta_current_and_concentration()