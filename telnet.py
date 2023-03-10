import getpass
import telnetlib
network = "192.168.1."
for each in range(1, 255):  
    print(network+str(each)) 
    
HOST = "192.168.1.120" # here write your ip switch :)
user = input("Enter your username for device : ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST, 23) 
tn.read_until(b"Username: ")    
tn.write(user.encode('ascii') + b"\n") 
 
if password:    
    tn.read_until(b"Password: ")        
    tn.write(password.encode('ascii') + b"\n")  
    tn.write(b"enable\n")
    tn.write(b"matador\n")
    tn.write(b"conf t\n")
    tn.write(b"hostname WOW_ZOUHAIR\n")
    tn.write(b"exit\n")
    tn.write(b"exit\n")
    print("Script Completed")
    print(tn.read_all().decode('ascii')) 
