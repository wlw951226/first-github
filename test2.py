import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("/+")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))



client = mqtt.Client("1226")
client.on_connect = on_connect
client.on_message = on_message
client.connect('192.168.3.3', port =1883, keepalive=600) # 600为keepalive的时间间隔
client.subscribe('python', qos=0)
client.loop_forever() # 保持连接