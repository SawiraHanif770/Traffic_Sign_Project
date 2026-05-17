import threading

def run_prediction():
    print("Prediction running...")

thread = threading.Thread(target=run_prediction)
thread.start()
thread.join()

print("Thread completed")