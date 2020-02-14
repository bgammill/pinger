# remote.py is run on the remote machine that will be receiving
# heartbeat connections from local.py
import paho.mqtt.client as mqtt
import time

global last_time
last_time =  time.time()

def on_connect(client, userdata, flags, rc):
    print("Connected with code: %i" % rc)
    client.subscribe('marcel_status')

def on_message(client, userdata, message):
    print('client is still alive')
    global last_time
    last_time = time.time()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('test.mosquitto.org', 1883)

while True:
    client.loop_start()
    if time.time() - last_time > 3:
        last_time = time.time()
        print('client is probably dead')
