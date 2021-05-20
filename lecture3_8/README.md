### 1 Задание
Потому что InActConn соединение рагирует на любое не канальное соединение.  
Вырезка из мануала  
The output of ipsvadm lists connections, either as

ActiveConn - in ESTABLISHED state  
InActConn - any other state  

Весит соединение потому что каждое вхождение весит до connection timeout. 

### 2 Задание  
```
 !Configuration File for keepalived
global_defs {
   router_id uMASTER
}

vrrp_instance VI_1 {
    state MASTER
    interface eth1
    virtual_router_id 230
    priority 101                        # PAY ATTENTION ON PRIORITY!!
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P@$$w0rd)
    }


   virtual_ipaddress {
       173.28.128.200/32 dev eth1
    }
}
! Configuration File for keepalived
global_defs {
   router_id uBACKUP
}


vrrp_instance VI_1 {
    state BACKUP
    interface eth1
    virtual_router_id 230
    priority 100                        # PAY ATTENTION ON PRIORITY!!
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P@$$w0rd)
    }

   virtual_ipaddress {
       173.28.128.200/32 dev eth1
    }
}

vrrp_script change_ip {
scripts </opt/scripts/change_ip.sh
}

/opt/scripts/change_ip.sh  
#!/bin/bashbash  
sudo ipvsadm -A -t 172.28.128.200:80 -s rr  
sudo ipvsadm -a -t 172.28.128.200:80 -r 172.28.128.10:80 -g -w 1  
sudo ipvsadm -a -t 172.28.128.200:80 -r 172.28.128.60:80 -g -w 1  
```
###3. Задание



 7 адресов. 1 по которому подключаються и по 2 пары адресов на каждый сервер. 
 На каждом сервере настраивается VIP так,  
 1 адрес из первой сети 2 из второй сети