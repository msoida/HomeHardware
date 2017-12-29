from json import loads as unjson, JSONDecodeError


def on_message(client, userdata, message):
    try:
        data = unjson(message.payload)
    except JSONDecodeError:
        return

    if message.topic == 'test/clock':
        userdata['clock_text'](data.get('text'))

    elif message.topic == 'test/display':
        userdata['display_text'](data.get('text'))
