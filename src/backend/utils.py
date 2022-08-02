import os


OUTPUT_LIST = ['All_Day', 'Experiment']

def make_output_folder():
    for path in OUTPUT_LIST:
        if not os.path.isdir(path):
            os.mkdir(path)
        
def make_output_folder_by_sn(sn):
    sn = sn.replace('\r\n', '')
    sn_list = [f"{i}//{sn}" for i in OUTPUT_LIST]
    for path in sn_list:
        if not os.path.isdir(path):
            os.mkdir(path)
    