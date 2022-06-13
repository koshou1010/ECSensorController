import serial
import serial.tools.list_ports
import time
import datetime
import json
import os










def SaveFile_Total(json_dump, All_filename):

  meta_data = '{"name":"file_meta","raw_dumper_ver":"raw_dumper_v1_2","project_ver":"ESRTSD_bcus_v1_2","machine_sn":"FT3WLPSW","fw_ver":"fw_sextant_1.0.0","hw_ver":"hw_sextant_1.0.0","sw_ver":"0.1.3-alpha-1","app_name":"Enosim ESRTSD","user_sn":"9366d0eb90a06ff067dfdef6c3eca8f339f72ddd4fa21cf6e376177f3ed1a547","organization":"enosim","reference_time":null,"l_date":"2021-05-19T11:44:06.076+08:00","channel_name":["_#ec_i#0","_#ec_i#0","_#ec_i#0","_#ec_i#0","_#tm_c#0","_#rh_p#0","_#fm_sccm#0"]}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.125+08:00","status_flag":"on_start","subject_flag":"user","step_flag":null}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","status_flag":"on_first_preset_voltage","subject_flag":"auto","step_flag":null}\n'+'{"name":"preset_meta","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","len_channel":7,"device_cfg":{"supply_voltage":5.0,"channel_biasing_resistance":[1,1,1,1,1,1,1],"channel_reference_c":[null,null,null,null,null,null,null],"channel_reference_voltage":[null,null,null,null,null,null,null],"preset_flow":[5],"channel_actual_gain":[1.0,1.0,1.0,1.0,1.0,1.0,1.0],"channel_preset_voltage":[1.5,1.5,1.5,1.5,1.5,1.5,1.5]},"critical":{"first_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":1800.0,"during":1.0},"second_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":10.0,"during":1.0},"round_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"baseline":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":60.0,"during":1.0},"stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":120.0,"during":1.0},"reacting":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"recovery":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":600.0,"during":1.0},"auto_stop_valve":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":4.0,"during":1.0},"slope_window_size":10,"threshold_ref_channel_indexes":[0,1]}}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:14.264+08:00","status_flag":"on_first_waiting_initial","subject_flag":"auto","valve":0,"pump":1,"step_flag":null}\n'  
  
  nowpath = os.getcwd()
  All_Floder = "All_Day"
  # print(ID.strip(), type(ID))
  # print(len(ID.strip()))
  # print(nowpath + "\\"+All_Floder+"\\"+ ID.strip() +"\\" + ID.strip() + "_"+All_filename + ".ndjson")
  # print(json_dump)
  #print(nowpath)
  global filename_allday
  filename_allday = nowpath + "\\"+All_Floder+"\\"+ ID.strip() +"\\" + ID.strip() + "_"+ All_filename + ".ndjson"
  if not os.path.isfile(filename_allday):
      f = open(filename_allday, "w")
      f.write(meta_data)
      f.close()
  try:
    with open(nowpath + "\\"+All_Floder+"\\"+ ID.strip() +"\\" + ID.strip() + "_"+ All_filename + ".ndjson", "a") as file_object:
      file_object.write("\n"+json_dump)
  except:
    print("saved error")


def SaveFile_Ex(json_dump, Ex_filename, input_gas):
  meta_data = '{"name":"file_meta","raw_dumper_ver":"raw_dumper_v1_2","project_ver":"ESRTSD_bcus_v1_2","machine_sn":"FT3WLPSW","fw_ver":"fw_sextant_1.0.0","hw_ver":"hw_sextant_1.0.0","sw_ver":"0.1.3-alpha-1","app_name":"Enosim ESRTSD","user_sn":"9366d0eb90a06ff067dfdef6c3eca8f339f72ddd4fa21cf6e376177f3ed1a547","organization":"enosim","reference_time":null,"l_date":"2021-05-19T11:44:06.076+08:00","channel_name":["_#ec_i#0","_#ec_i#0","_#ec_i#0","_#ec_i#0","_#tm_c#0","_#rh_p#0","_#fm_sccm#0"]}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.125+08:00","status_flag":"on_start","subject_flag":"user","step_flag":null}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","status_flag":"on_first_preset_voltage","subject_flag":"auto","step_flag":null}\n'+'{"name":"preset_meta","meta_index":-1,"l_date":"2021-05-19T11:44:06.140+08:00","len_channel":7,"device_cfg":{"supply_voltage":5.0,"channel_biasing_resistance":[1,1,1,1,1,1,1],"channel_reference_c":[null,null,null,null,null,null,null],"channel_reference_voltage":[null,null,null,null,null,null,null],"preset_flow":[5],"channel_actual_gain":[1.0,1.0,1.0,1.0,1.0,1.0,1.0],"channel_preset_voltage":[1.5,1.5,1.5,1.5,1.5,1.5,1.5]},"critical":{"first_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":1800.0,"during":1.0},"second_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":10.0,"during":1.0},"round_waiting_initial_stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"baseline":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":60.0,"during":1.0},"stable":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":120.0,"during":1.0},"reacting":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":30.0,"during":1.0},"recovery":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":600.0,"during":1.0},"auto_stop_valve":{"threshold_value":1.0,"threshold_rate":1.0,"timeout":4.0,"during":1.0},"slope_window_size":10,"threshold_ref_channel_indexes":[0,1]}}\n'+'{"name":"control_status","meta_index":-1,"l_date":"2021-05-19T11:44:14.264+08:00","status_flag":"on_first_waiting_initial","subject_flag":"auto","valve":0,"pump":1,"step_flag":null}\n'  
  Time = datetime.datetime.now().isoformat() + "+08:00"
  ex_start = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"experient_start"}'
  gas_in = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"gas_in"}'
  gas_out = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"gas_out"}'
  experiment_finish = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"experient_finish"}'
  #print(input_gas)
  nowpath = os.getcwd()
  Ex_Floder = "Experiment"
  #print(nowpath) 
  global filename_ex
  filename_ex = nowpath + "\\"+Ex_Floder+"\\" + ID.strip() + "\\"+ID.strip()+"_"+Ex_filename +"_"+ input_gas + ".ndjson"
  if not os.path.isfile(filename_ex):
      f = open(filename_ex, "w")
      f.write(meta_data)
      f.write(ex_start)
      f.close()

  with open(nowpath + "\\"+Ex_Floder+"\\" + ID.strip() + "\\"+ID.strip()+"_"+Ex_filename +"_"+ input_gas + ".ndjson", "a") as file_object:
    file_object.write("\n"+json_dump)
 

def Dump2ndjson(content, CheckAllorEx, *args):
  #print(content)
  keylist = ["name", "meta_index", "l_date", "channel"]
  # print(content.split(','))
  NO2 = float(content.split(',')[0].split(':')[-1].split(' ')[0])
  SO2 = float(content.split(',')[2].split(':')[-1].split(' ')[0])
  O3 = float(content.split(',')[4].split(':')[-1].split(' ')[0])
  CO = float(content.split(',')[6].split(':')[-1].split(' ')[0])
  Temp = float(content.split(',')[9].split(' ')[0])
  RH = float(content.split(',')[11].split(' ')[0])
  Flow = float(content.split(',')[13].split(' ')[0])
  Time = datetime.datetime.now().isoformat() + "+08:00"
  channellist = [NO2, SO2, O3, CO, Temp, RH, Flow]

  # print(keylist)
  #print(Time)
  # print(channellist)
  global All_filename
  All_filename = Time.split('T')[0].replace("-", "_")
  Ex_filename = Time.split('T')[0].replace("-", "_")
  #print(Ex_filename)
  dataset = {"name": "data", "meta_index": 0,
            "l_date": Time, "channel": channellist}
  json_dump = json.dumps(dataset)

  SaveFile_Total(json_dump, All_filename)
  if CheckAllorEx == 1:
    SaveFile_Ex(json_dump, Ex_filename, args[0])
  print(json_dump)

# SENDFLAG = True
# def send_ex_start():
#   if SENDFLAG == True:
#     Time = datetime.datetime.now().isoformat() + "+08:00"
#     ex_start = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"experient_start"}'
#     nowpath = os.getcwd()
#     All_Floder = "All_Day"
#     filename = nowpath + "\\"+All_Floder+"\\"+ ID.strip() +"\\" + ID.strip() + "_"+ All_filename + ".ndjson"
#     with open(filename, "a") as file_object:
#       file_object.write("\n"+ex_start)

def add_gas_in():
  Time = datetime.datetime.now().isoformat() + "+08:00"
  gas_in = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"gas_in"}'
  with open(filename_ex, "a") as file_object:
    file_object.write("\n"+gas_in)
  with open(filename_allday, "a") as file_object:
    file_object.write("\n"+gas_in)

def add_gas_out():
  Time = datetime.datetime.now().isoformat() + "+08:00"
  gas_out = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"gas_out"}'
  with open(filename_ex, "a") as file_object:
    file_object.write("\n"+gas_out)
  with open(filename_allday, "a") as file_object:
    file_object.write("\n"+gas_out)

def add_ex_finish():
  Time = datetime.datetime.now().isoformat() + "+08:00"
  experiment_finish = '{"name": "control_status", "meta_index": -1, "l_date":"'+str(Time)+'", "status_flag":"experiment_finish"}'
  with open(filename_ex, "a") as file_object:
    file_object.write("\n"+experiment_finish)
  with open(filename_allday, "a") as file_object:
    file_object.write("\n"+experiment_finish)

class FT232:
  # def CheckPort():
  #   plist = list(serial.tools.list_ports.comports())
  #   if len(plist) <= 0: 
  #     pass 
  #   else:
  #     plist_0 = list(plist[0])
  #     print(plist[0])
  #     print(plist[1])
  #     print(plist[2])
  #     print(plist[3])
  #     #Seletor_Com = input("Please Select ComPort : ")
  #     serialName = plist_0[0]
  #     serialFd = serial.Serial(serialName, 115200, timeout=1)
  #     return serialFd

  def ShowRecive(ser, Cmd, CheckAllorEx, *args):
    count_RO = 0
    count_MID = 0 # count machine id
    count_SS = 0
    count_SP = 0
    while True:
      if Cmd == 'SC RE\r':  # get machine id
        count_MID += 1
        line = ser.readline()
        try:
          if count_MID == 7:
            print("machine id get successed")
            # machine_id_list = [SXT2SPECECE010007, SXT2SPECECE010009, SXT2SPECECE010010, SXT2SPECECE010011]
            
            global machine_id
            machine_id = ("Rsponse : %s" % line.decode('utf-8')).split(':')[-1]
            break
        except:
          print('error machine id')
          pass
      if Cmd == 'SR RO\r': # return data once
        count_RO+=1
        line = ser.readline() 
        try:
          #print("Rsponse : %s" % line.decode('utf-8'))
          if count_RO ==8:
            content = ("Rsponse : %s" % line.decode('utf-8'))
            print(content)
            if args:
              Dump2ndjson(content, CheckAllorEx,  args[0])
              break
            else:
              Dump2ndjson(content, CheckAllorEx)
              break
        except:
          print('response error')
          break
      if Cmd == 'SC DO VAx 0\r': # switch to sample
        count_SS +=1
        line = ser.readline()
        try:
          #print("Rsponse : %s" % line.decode('utf-8'))
          if count_SS == 9:
            content = "Rsponse : %s" % line.decode('utf-8') 
            print(content)
            add_gas_in()
            # print("switch to sample successed")
            break
        except:
          print('response error')
          break
      if Cmd == 'SC DO VAx 1\r':  # switch to purge
        count_SP += 1
        line = ser.readline()
        try:
          #print("Rsponse : %s" % line.decode('utf-8'))
          if count_SP == 11:
            print("Rsponse : %s" % line.decode('utf-8'))
            add_gas_out()
            # print("switch to sample successed")
            break
        except:
          print('response error')
          break

  def Send_Cmd(ser, Cmd, CheckAllorEx, *args):
    print("Command: %s"%Cmd)
    ser.write(Cmd.encode('utf-8'))
    if args:
      FT232.ShowRecive(ser, Cmd, CheckAllorEx, args[0])
    else:
      FT232.ShowRecive(ser, Cmd, CheckAllorEx)


def main(command, CheckAllorEx, *args):
  ContiFlag = False # use to switch per 1 min or 1 sec
  Ex_count = 0
  try:
    ser = serialFd
    print("Available com port name is >>> ", ser.name)
    while ContiFlag:
      FT232.Send_Cmd(ser, command+'\r')
      time.sleep(1)
      Ex_count+=1
      if Ex_count == 10: # set time of wait purge
        print("----------switch to sample-----------")
        cmd_ss = "SC DO VAx 0"
        FT232.Send_Cmd(ser, cmd_ss+'\r')
        break
    if ContiFlag == False:
      if args:
        FT232.Send_Cmd(ser, command+'\r', CheckAllorEx, args[0])
      else:
        FT232.Send_Cmd(ser, command+'\r', CheckAllorEx)

  except:
    print("Connect com port is error!")  


def Valve_Switcher(command, CheckAllorEx):
  ContiFlag = True  # use to switch per 1 min or 1 sec
  try:
    ser =  serialFd
    print("Available com port name is >>> ", ser.name)
    while ContiFlag:
      FT232.Send_Cmd(ser, command+'\r', CheckAllorEx)
      break
  except:
    print("Connect com port is error!")




def All_Out(machine_id2):
  command = "SR RO"
  global ID
  ID = machine_id2 
  CheckAllorEx = 0 # allday = 0, experiment = 1
  #command = input("input command: ").strip()
  #FT232.CheckPort()
  
  main(command, CheckAllorEx)


def Ex_Out(input_gas, machine_id2):
  global SENDFLAG
  SENDFLAG = False
  command = "SR RO"
  global ID
  ID = machine_id2 
  CheckAllorEx = 1 # allday = 0, experiment = 1
  #command = input("input command: ").strip()
  #FT232.CheckPort()
  main(command, CheckAllorEx, input_gas)

def SwitchSample():
  CheckAllorEx = 1
  command = "SC DO VAx 0"
  Valve_Switcher(command, CheckAllorEx)

def SwitchPurge():
  CheckAllorEx = 1
  command = "SC DO VAx 1"
  Valve_Switcher(command, CheckAllorEx)

def Got_Machine_ID():
  command = "SC RE"
  main(command, 0)
  return machine_id

def ChooseComPort():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0: 
      pass 
    else:
      plist_0 = list(plist[0])
      for i in range(len(plist)):
        print(plist[i])
      Seletor_Com = input("Please Select ComPort : ")
      serialName = Seletor_Com
      global serialFd
      serialFd = serial.Serial(serialName, 115200, timeout=1)
      return serialFd
  




# if __name__ =='__main__':
#   command = "SC RE"
#   main(command, 0)


