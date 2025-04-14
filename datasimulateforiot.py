from azure.iot.device import IoTHubDeviceClient, Message
import time
import random

conn_str = "HostName=IoTHubUnique001.azure-devices.net;DeviceId=Device001;SharedAccessKey=DjEQpXqomva1wDPpepcJU7pscggTgFfPsYbnjkEoyMY="
client = IoTHubDeviceClient.create_from_connection_string(conn_str)

while True:
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 50.0)
    msg = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')
    client.send_message(msg)
    print("Message sent")
    time.sleep(5)
