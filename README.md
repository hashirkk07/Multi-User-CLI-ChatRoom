# Multi-User CLI Chat-Room
Hi, this is a simple multi-user chat room built using threading and socket programming.
---
### Usage Guidelines:
1. Run the server in one terminal using the command   
```$ python server.py```  
 
2. Run the clients in different terminal using the command   
```$ python client.py```

---
### Note:
If you want to run the client in different machine, please update the code ``` client.connect(('127.0.0.1',45454))``` in the client.py to ```client.connect(('<YOUR_SERVER_RUNNING_MACHINE_IP>',45454))```
