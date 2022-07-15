import utils
import re
from flask import Flask, request, render_template
import catchdata
app = Flask(__name__)

def preprocessing():
    catchdata.ChooseComPort()
    machine_id = catchdata.Got_Machine_ID()
    global machine_id2
    machine_id2 = machine_id
    utils.make_output_folder()
    utils.make_output_folder_by_sn(machine_id)
    catchdata.SwitchSample()
    
@app.route("/", methods=['GET', 'POST'])
def server():
    # print("machine_id = ",machine_id2)
    if request.method == 'POST':
      if request.json['btn'] == 'allday':
        catchdata.All_Out(machine_id2)
      if request.json['btn'] == 'ex':
        input_gas = request.json['input_gas']
        catchdata.Ex_Out(input_gas, machine_id2)
      if request.json['btn'] == 'switch_sample':
        # catchdata.SwitchSample()
        catchdata.add_gas_in()
      if request.json['btn'] == 'switch_purge':
        # catchdata.SwitchPurge()
        catchdata.add_gas_out()
      if request.json['btn'] == 'ex_done':
        catchdata.add_ex_finish()
    return render_template('front.html')

  
# @app.route("/", methods=['GET', 'POST'])
# def server():
#   if request.method == 'POST':
#     pass
#   return render_template('front.html')


