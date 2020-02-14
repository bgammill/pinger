# local.py is run on the local machine that will be sending
# heartbeat connections to remote.py
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with code: %i" % rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect('test.mosquitto.org', 1883)

while True:
    client.publish('marcel_status', 'alive')
    time.sleep(1)

client.loop_forever()
