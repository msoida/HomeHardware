from decouple import config


status_topic = config('STATUS_TOPIC')
mqtt_server = config('MQTT_SERVER', default='localhost')
