import socket
 
def inet_connect(serverport):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(('',serverport))
        s.listen(5)
        print("Wait...")
        (client,(ip,port))=s.accept()
        print("Connection Established with :",ip,":",port)
        return client
def rec(client):
    data=client.recv(4096)
    if data is None:
            return False
    else:
            return data.decode('ASCII')
     

def send(data,client):
    data=data.encode('ASCII')
    client.send(data)
    
    
def get_data():
    data=input('Say something:')
    return data


serverport=int(input("Enter port :")) 
client=inet_connect(serverport)
while True:
        
        data=get_data()
        if data=="":
                send(' ',client)
        elif data == "exit" or data == "logout":
                send("OK Bye Closing Connection...",client)
                client.close()
                print("Connection Is Closed")
                break
        send(data,client)
        print("You:",data )
        clientdata=rec(client)
        if clientdata:
                print("\t\t\tFriend:",clientdata)
        if clientdata=="OK Bye Closing Connection...":
                print("Connection Is Closed")
                client.close()
                break
        
        
                
              
        
        
        

