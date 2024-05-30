from flask import Flask
import time

app = Flask(__name__)

start_time = 0
elapsed_time = 0
running = False

@app.get("/start")
def start():
    global start_time, running

    if not running:
        start_time = time.time()

    running = True
    return str(elapsed_time)

@app.get("/stop")
def stop():
    global running, elapsed_time

    if start_time == 0:
        return "NO START"
    else:
        if running:
            running = False
            elapsed_time += time.time() - start_time

        return str(elapsed_time)

@app.get("/elapsed")
def elapsed():
    if start_time == 0:
        return "NO START"
    else:
        if running:
            curr_elapsed_time = time.time() - start_time + elapsed_time
        else:
            curr_elapsed_time = elapsed_time

        run_code = "R" if running else "S"
        return  run_code + "|" + str(curr_elapsed_time)

@app.get("/reset")
def reset():
    global start_time, elapsed_time, running

    start_time = 0
    elapsed_time = 0
    running = False
    
    return "OK"
