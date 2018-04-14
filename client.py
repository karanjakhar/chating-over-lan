import socket


def inet_connect(ip,serverport):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,serverport))
    print("Connection Established with :",ip,":",serverport)
    print("Wait...")
    return s

def get_data():
    data=input('Say something:')
    return data
    
def rec(s):
    data=s.recv(4096)
    return data.decode('ASCII')
     

def send(data,s):
    data=data.encode('ASCII')
    s.send(data)
    
serverport=int(input("Enter Port:"))
ip=input("Enter IP:")
s=inet_connect(ip,serverport)
while True:
        
        data=rec(s)
        print("\t\t\tFriend:",data)
        if data == "OK Bye Closing Connection..." :
            print("Connection Is Closed.")
            s.close()
            break
        data=get_data()
        if data=="":
            send(' ',s)
        elif data =="exit" or data =="logout":
             send("OK Bye Closing Connection...",s)
             s.close()
             break
        send(data,s)
        print("You:",data)
         
                
         
                
        
        
