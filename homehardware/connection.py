from atexit import register as atexit
from json import dumps as json

from paho.mqtt.client import Client, connack_string, error_string
from pytz import timezone

from .message import on_message
from .settings import mqtt_server, status_topic


tz = timezone('Europe/Warsaw')

status_error = json(dict(status='error', value=-1))
status_connected = json(dict(status='connected', value=1))
status_disconnected = json(dict(status='disconnected', value=0))


def on_connect(client, userdata, flags, rc):
    print('MQTT connect: {}'.format(connack_string(rc)))
    client.subscribe('notification/print')
    client.subscribe('test/#')
    client.publish(status_topic, status_connected, retain=True)


def on_disconnect(client, userdata, rc):
    print('MQTT disconnect: {}'.format(error_string(rc)))


client = Client()
client.will_set(status_topic, status_error, retain=True)
client.connect_async(mqtt_server)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.loop_start()


@atexit
def run_at_exit():
    client.publish(status_topic, status_disconnected, retain=True)
    client.loop_stop()
    client.disconnect()


def publish(topic, value):
    data = json(dict(value=value))
    result, mid = client.publish(topic, data, retain=True)
