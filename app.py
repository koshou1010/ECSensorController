import utils
import re
from flask import Flask, request, render_template
import catchdata
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def server():
    print("machine_id = ",machine_id2)
    #print("IN SERVER")
    # data = request.get_data()
    if request.method == 'POST':
      #print("IN POST")
      if request.json['btn'] == 'allday':
        #print("IN request to call F")
        catchdata.All_Out(machine_id2)
      if request.json['btn'] == 'ex':
        input_gas = request.json['input_gas']
        # catchdata.send_ex_start()
        catchdata.Ex_Out(input_gas, machine_id2)
      if request.json['btn'] == 'switch_sample':
        catchdata.SwitchSample()
      if request.json['btn'] == 'switch_purge':
        catchdata.SwitchPurge()
      if request.json['btn'] == 'ex_done':
        catchdata.add_ex_finish()
    return render_template('front.html')

if __name__ == '__main__':
    catchdata.ChooseComPort()
    machine_id = catchdata.Got_Machine_ID()
    global machine_id2
    machine_id2 = machine_id
    utils.make_output_folder()
    utils.make_output_folder_by_sn(machine_id)
    app.run(debug=False, port = 5001)
    # app.run(debug=False, port = input("please Select Port Number :　"))
    # app.run(debug= False)
