from flask import Flask, request, render_template, redirect, url_for
from functools import wraps
import pyautogui


app = Flask(__name__)
hw_status = 'Doing HW'
hw_status = 'Terminated'
hw_status = 'Getting HW'


@app.route('/screen', methods=['GET', 'POST'])
def screen():
    return render_template("index.html")
    

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # return render_template("todo.html")
    return 'HI'
    

@app.route('/hpma_controller', methods=['GET', 'POST'])
def hpma_controller():
    return render_template("hpma_controller.html", status=hw_status)
    

@app.route('/set_cur_hw_got', methods=['GET', 'POST'])
def set_cur_hw_got():
    global hw_status
    hw_status = 'Doing HW'
    return redirect(url_for('hpma_controller', status=hw_status))
    

@app.route('/set_cur_hw_done', methods=['GET', 'POST'])
def set_cur_hw_done():
    global hw_status
    hw_status = 'Getting HW'
    return redirect(url_for('hpma_controller', status=hw_status))
    

@app.route('/set_all_hw_done', methods=['GET', 'POST'])
def set_all_hw_done():
    global hw_status
    hw_status = 'Terminated'
    return redirect(url_for('hpma_controller', status=hw_status))
    

@app.route('/get_hw_status', methods=['GET', 'POST'])
def get_hw_status():
    global hw_status
    return hw_status
    
@app.route('/json_handler', methods=['POST'])
def json_handler(): 
    global hw_status
    request_json = request.get_json()
    print(request_json)
    hw_status = request_json['hw_status']
    
    return 'OK'
    
@app.route('/mouse_handler', methods=['POST'])
def mouse_handler(): 
    request_json = request.get_json()
    
    pyautogui.moveTo(100, 150)
    
    action = request_json['mouse_action']
    if action == 'move_mouse':
        X = request_json['posX']
        Y = request_json['posY']
        
        pyautogui.click(X, Y)
    
    return 'OK'

if __name__ == '__main__':
    hw_status = 'Getting HW'
    app.run('0.0.0.0', port=5000, debug=True)
    
