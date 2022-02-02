import random
from paho.mqtt import client as mqtt_client
from db import get_db
import app
import  requests

broker = 'localhost'
port = 1883
topic = "python/mqtt"

client_id = f'python-mqtt-{random.randint(0,100)}'
timer_set = 0

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        result = msg.payload.decode()
        global timer_set
        time_to_close = float(result)
        timer_set = max(timer_set, time_to_close)
        print(timer_set)
        if time_to_close == 0:
            pload = {'is_closed': 'True', 'time': str(timer_set)}
            r = requests.post(url='http://localhost:5000/timer/', data=pload)
            print(r.text)





    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()