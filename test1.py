import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
def on_disconnect(client, userdata, rc):
    print("Connection returned result:"+ str(rc))

client = mqtt.Client("1995")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect= on_disconnect
client.connect('192.168.3.3', 1883, 600)
r = client.publish('python', payload='test1 test2 test3', qos=0)
print(r.mid)
client.loop_forever(timeout=50)




