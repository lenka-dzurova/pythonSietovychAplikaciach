from ClientConfig import ClientConfig
import socket
from ActionEnum import ActionEnum
from MessageModel import MessageModel
import json

def menu():
    print("******MENU******")
    print("Exit program [1]")
    print("Show users [2]")
    print("Send message [3]")


client_config = ClientConfig()



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_config.server_ip_address, client_config.server_port))

print("Wellcome")
user_name = input("Enter you nick: ")
menu()

msg = MessageModel(user_name, "", "", ActionEnum.LOGIN)
json_str = json.dumps(msg.__dict__)
client_socket.send(json_str.encode())

while(True):
    action = input ("Choose operation from menu: ")

    match action:
        case 1:
            msg = MessageModel(user_name, "", "", ActionEnum.EXIT)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())
            client_socket.close()
            quit()
        case 2:
            msg = MessageModel(user_name, "", "", ActionEnum.USER)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())
            data = client_socket.recv(1500)
            msg = json.loads(data.decode(), object_hook=MessageModel.from_json)
            print(f"User list: {msg.text}")
            continue
        case 3:
            text = input("Message: ")
            to_user = input("To user: ")
            msg = MessageModel(user_name, to_user, text, ActionEnum.USER)
            json_str = json.dumps(msg.__dict__)
            client_socket.send(json_str.encode())