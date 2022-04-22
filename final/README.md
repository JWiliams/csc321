# Final Project
All commands listed were used while python files were 
running.

## Weather
My goal with the weather broadcast was to caputure
a pcap file of wuserver.py and wuclient.py. I use 
the command "tcpdump -i 2 -w wuserver.pcap port 5555 -vvv". 
This command will have to run on the localhost interface, sniff traffic
on port 5555, and save to a file callled wuserver.pcap.

Next I did the same with the client. My command was 
"tcpdump -i 2 -w wuclient.pcap port 5555 -vvv". 

## Task
I have the same goal for the task python files. The 
first command I run is "tcpdump -i 2 -w taskvent.pcap port 5557 -vvv". Next I run "tcpdump -i 2 -w taskwork.pcap port 5557 -vvv". The sink program was running on port 5558 so the command was "tcpdump -i 2 -w tasksink.pcap port 5558 -vvv". 


