import logging
from enum import Enum


FORMAT = '%(asctime)s %(levelname)s: %(message)s'

LOG_PATH = 'log'
ANALYSIS_OUTPUT = 'output'
EXPERIMENT_PATH = '../Experiment'
ASSIGN_DATE = True
DATE = '2022_07_21'
INPUT_GAS_LIST = ['CO', 'NO2', 'SO2']
INPUT_TEMP_LIST = ['22', '29', '35', '40']
INPUT_HUM_LIST = ['40', '50', '60', '80']
SENSOR_CHANNEL_LIST = ['NO2', 'SO2', 'O3', 'CO', 'Temp', 'RH', 'Flow']
COLOR_MAP = ['blue', 'cyan', 'red', 'orange']


class SensorEnum(Enum):
    NO2 = 0
    SO2 = 1
    O3 = 2
    CO = 3
    Temp = 4
    RH = 5
    Flow = 6