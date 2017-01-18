import fractal
import pghelper
import paho.mqtt.client as mqtt

repete = True

cliente = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Conexao realizada com sucesso")
    client.subscribe("paho/test/arte",qos=0)

def on_message(client, userdata, msg):
    intermediario = fractal.fractal(int(msg.payload))
    pghelper.updateImage(intermediario)
    print(msg.topic+" "+str(msg.payload))


def on_disconnect(client, userdata, rc):
    print("deauth")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
