from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)
hw_status = 'Doing HW'
hw_status = 'Terminated'
hw_status = 'Getting HW'

script_status = 'Doing'
script_status = 'Terminated'

next_script_idx = 0


@app.route('/screen', methods=['GET', 'POST'])
def screen():
    return render_template("index.html")
    

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # return render_template("todo.html")
    return 'HI'
    

@app.route('/hpma_controller', methods=['GET', 'POST'])
def hpma_controller():
    return render_template("hpma_controller.html", status=hw_status, script_status=script_status, next_script_idx=next_script_idx)
    

# @app.route('/set_cur_hw_got', methods=['GET', 'POST'])
# def set_cur_hw_got():
    # global hw_status
    # hw_status = 'Doing HW'
    # return redirect(url_for('hpma_controller', status=hw_status, script_status=script_status))
    

# @app.route('/set_cur_hw_done', methods=['GET', 'POST'])
# def set_cur_hw_done():
    # global hw_status
    # hw_status = 'Getting HW'
    # return redirect(url_for('hpma_controller', status=hw_status, script_status=script_status))
    

# @app.route('/set_all_hw_done', methods=['GET', 'POST'])
# def set_all_hw_done():
    # global hw_status
    # hw_status = 'Terminated'
    # return redirect(url_for('hpma_controller', status=hw_status, script_status=script_status))
    

@app.route('/get_hw_status', methods=['GET', 'POST'])
def get_hw_status():
    global hw_status
    return hw_status
    
@app.route('/get_script_status', methods=['GET', 'POST'])
def get_script_status():
    global script_status
    return script_status
    
@app.route('/get_next_script_idx', methods=['GET', 'POST'])
def get_next_script_idx():
    global next_script_idx
    return str(next_script_idx)
    
@app.route('/json_handler', methods=['POST'])
def json_handler(): 
    global hw_status
    global script_status
    global next_script_idx
    
    request_json = request.get_json()
    print(request_json)
    
    try:
        hw_status = request_json['hw_status']
        print('set hw_status to', hw_status)
    except:
        'hw_status'
        
    try:
        script_status = request_json['script_status']
        print('set script_status to', script_status)
    except:
        'script_status'
        
    try:
        add_next_script_idx = int(request_json['add_next_script_idx'])
        if add_next_script_idx > 0:
            next_script_idx = next_script_idx + int(add_next_script_idx)
        else:
            next_script_idx = 0
        print('set next_script_idx to', next_script_idx)
    except:
        'next_script_idx'
    
    
    return 'OK'
    

if __name__ == '__main__':
    hw_status = 'Getting HW'
    app.run('0.0.0.0', port=5000, debug=True)
    
