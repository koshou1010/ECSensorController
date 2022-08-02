import os
import setting
import logging
import copy, ndjson, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


np.set_printoptions(suppress=True) # don't use scientific notation

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
        pass
    
class AnalysisSingleRound:
    '''
    Define SingleRound : same gas, same temp and same rh
    
    '''
    
    def __init__(self) -> None:
        self.sensor_enum_dict = {
            'NO2': 0,
            'SO2': 1,
            'O3': 2,
            'CO': 3,
            'Temp': 4,
            'RH': 5,
            'Flow': 6,
  
        }
        self.dirs_list = []
        self.target_machine_delta_dict = {}
        self.preprocessing()
        
    def preprocessing(self):  

        logging.info('start : preprocessing...')  
        self.target_file_list = self.seek_all_assign_date_file()
        self.target_machine_dict = self.make_target_machine_dict() #build a blank dict
        self.grouping_each_machine_each_round()
        self.ndjson2dataframe()


            
        
    def seek_all_assign_date_file(self)->list:
        target_file_list = []
        if setting.ASSIGN_DATE:
            logging.info('start : seek assign date file')
            for root, dirs, files in os.walk(setting.EXPERIMENT_PATH):
                for dir in dirs:
                    self.dirs_list.append(dir)
                for file in files:
                    if file.endswith('.ndjson'):
                        if setting.DATE in file:
                            logging.debug(os.path.join(root, file))
                            target_file_list.append(os.path.join(root, file))
        return target_file_list
    
    def make_target_machine_dict(self) -> dict:
        logging.info('start : make target machine dict')
        logging.debug("dirs : {}".format(', '.join(self.dirs_list))) 
        res_dct = {self.dirs_list[i]: [] for i in range(0, len(self.dirs_list), 1)}
        for key in res_dct.keys():
            res_dct[key] = ({"Hum_{}%".format(setting.INPUT_HUM_LIST[i]) : 
                {"Temp_{}".format(setting.INPUT_TEMP_LIST[i]) : 
                        {"{}".format(setting.INPUT_GAS_LIST[i]) : 
                        [
                        ] 
                        for i in range(0, len(setting.INPUT_GAS_LIST), 1)}
                    for i in range(0, len(setting.INPUT_TEMP_LIST), 1)}
                for i in range(0, len(setting.INPUT_HUM_LIST), 1)})
        logging.debug('blank dict : %s', res_dct)
        self.copy_dict(res_dct)
        return res_dct
    
    def grouping_each_machine_each_round(self):
        logging.info('start : grouping each machine each round')
        for i in self.target_file_list:
            filename = i.split('\\')[-1]
            sensor_board_id = filename.split('_')[0]
            input_gas = filename.split('_')[4]
            hum = "{}_{}".format(filename.split('_')[6],filename.split('_')[7])
            temp = "{}_{}".format(filename.split('_')[8],filename.split('_')[9])
            self.target_machine_dict[sensor_board_id][hum][temp][input_gas].append(i)
            
    def copy_dict(self, blank_dict:dict):
        logging.info('start : copy dict')
        self.target_machine_delta_dict = copy.deepcopy(blank_dict)
    
    def split_status(self, i:dict):
        '''
        split status 1 to status 7
        '''
        
        # status = 0, initial
        # status = 1, experient_start
        # status = 2, gas_in
        # status = 9, gas_out
        if i['name'] == 'control_status':
            if i['status_flag'] == 'experient_start':
                self.status= 1
            elif i['status_flag'] == 'gas_in':
                self.status = 2
            elif i['status_flag'] == 'gas_out':
                self.status = 9


        if self.status == 1:
            if i['name'] == 'data':
                self.basline_list.append(i['channel'])
        if self.status == 2:
            if i['name'] == 'data':
                self.gasin_list.append(i['channel'])
        if self.status == 9:
            pass
                    
    def check_modified(self, all_data:list):
        '''
        check file if modified
        '''
        
        self.status = 0
        self.basline_list = []
        self.gasin_list = []
        
        skip_index = None
        modified_flag = False  
        for index, i in enumerate(all_data):
            if index == 0:
                if i['name'] == 'modify_header':
                    modified_flag = True
                    skip_index = i['skip_to']
                else:
                    modified_flag = False
                    
            if modified_flag:
                if index >= skip_index:  
                    self.split_status(i) 
                else:
                    pass
            else:   
                self.split_status(i)
                            
    def ndjson2dataframe(self):
        logging.info('start : ndjson2dataframe')
        for machine_id in self.target_machine_dict.keys():
            # print(machine_id)
            for rh in self.target_machine_dict[machine_id]:
                # print(rh)
                for temp in self.target_machine_dict[machine_id][rh]:
                    # print(temp)
                    for gas in self.target_machine_dict[machine_id][rh][temp]:
                        # print(gas)
                        for file in self.target_machine_dict[machine_id][rh][temp][gas]:
                            total_list = []
                            status = 0
                            # if file == '../Experiment\SXT2SGXECE010004\SXT2SGXECE010004_2022_07_21_CO_15ppm_Hum_80%_Temp_29_1.ndjson':
                            # print(file)
                            concentration = float(file.split('ppm')[0].split('_')[-1])
                            total_list.append(concentration)
                            with open(file, 'r') as f:
                                all_data = ndjson.load(f)            
                                self.check_modified(all_data)
                            self.basline_list = self.basline_list[-180:] # 最後3Min
                            self.gasin_list = self.gasin_list[-120:] # 最後2Min
                            
                            baseline_ary = np.array(self.basline_list)
                            baseline_ary_avg = np.mean(baseline_ary, axis = 0)
                            gasin_ary = np.array(self.gasin_list)
                            gasin_ary_avg = np.mean(gasin_ary, axis = 0)
                            delta_ary = gasin_ary_avg - baseline_ary_avg
                            total_list.append(delta_ary)
                            self.target_machine_delta_dict[machine_id][rh][temp][gas].append(total_list)
        logging.debug('delta dict : %s', self.target_machine_delta_dict)
        
    def linear_regression_maker(self, single_round_data : list, gas : str) -> tuple:
        target_delta_list = []
        for i in single_round_data:
            target_delta_list.append(i[-1][self.sensor_enum_dict[gas]])
        df_target_delta = pd.DataFrame(target_delta_list, columns=['{}_delta'.format(gas)])
        df = pd.DataFrame(single_round_data, columns=['concentration', 'sensor_set'])
        final_df = pd.concat([df, df_target_delta], axis = 1)
        delta_current = final_df['{}_delta'.format(gas)].to_numpy()
        concentration = final_df['concentration'].to_numpy()
        concentration = concentration.astype(np.float)
        
        series_dict = {'x1':concentration, 'y1':delta_current}
        df0 = pd.DataFrame(series_dict)
        x1 = df0[['x1']]
        y1 = df0[['y1']] 
        return(x1, y1)    
       

    def plot_delta_current_and_concentration(self):
        logging.info('Start : plot delta current and concentration')
        for machine_id in self.target_machine_delta_dict.keys():
            # print(machine_id)
            for rh in self.target_machine_delta_dict[machine_id]:
                # print(rh)
                for temp in self.target_machine_delta_dict[machine_id][rh]:
                    # print(temp)
                    for gas in self.target_machine_delta_dict[machine_id][rh][temp]:
                        # print(gas)
                        legend_flag = False
                        if len(self.target_machine_delta_dict[machine_id][rh][temp][gas]) != 0:
                            filename = ('{}_{}_{}_{}_{}'.format(machine_id, setting.DATE, gas, rh, temp))
                            x1, y1 = self.linear_regression_maker(self.target_machine_delta_dict[machine_id][rh][temp][gas], gas)
                            regr=LinearRegression()
                            regr.fit(x1, y1)
                            plt.figure(figsize=(20, 12))
                            for subcontent in self.target_machine_delta_dict[machine_id][rh][temp][gas]:
                                plt.scatter(subcontent[0], subcontent[1][self.sensor_enum_dict[gas]], color = setting.COLOR_MAP[self.sensor_enum_dict[gas]], label = gas)
                                if not legend_flag:
                                    plt.legend(bbox_to_anchor=(1.2,1))
                                    plt.plot(x1, regr.predict(x1),color = setting.COLOR_MAP[self.sensor_enum_dict[gas]], linewidth=1)
                                legend_flag = True
                            plt.xlabel("concentration(ppm)")
                            plt.ylabel("delta current(nA)")
                            plt.grid()
                            plt.title(filename)
                            plt.savefig('{}\\{}\\{}'.format(setting.ANALYSIS_OUTPUT, machine_id, filename), bbox_inches='tight')
                            # plt.show()
                            plt.close()
            