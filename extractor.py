import sys
import os
import subprocess
import numpy as np
from math import ceil

input_file = sys.argv[1]

print("The program will extract IP and the ports open in them and will store it but you can run extra options. Choose the options as below.")
print("-"*90)
print("0: Just extract IP and their open ports and save them.")
print("1: Put hosts and open ports as different text files named after hosts.")
print("2: Write hosts to a file which have port 80 and 443 open (for httprobe).")
print("3: Run nmap for service discovery and save results under the text file named after the hosts.")
inp = int(input("Choice: "))

with open(input_file) as f:
    out_dict = {}
    lines = f.readlines()
    for line in lines:
        l = line.split()
        p = l[6].split("/open")
        # print(f"{l[3]}:{p[0]}")
    #     try:
        if l[3] in out_dict.keys():
            out_dict[f'{l[3]}'].append(p[0])
        else:
            out_dict[f'{l[3]}'] = [p[0]]
    #     except:
    #         out_dict[f'{l[3]}'] = [p[0]]
    with open("out.log","w") as o:
        for k,v in out_dict.items():
            o.writelines(f"{k}:{v}\n")

#Just extract IP and ports
if(inp == 0):
    sys.exit()

#Host and Ports as different text files (Like for nmap scanning)
if (inp == 1):
    file_path = './for_manual_scan/'
    for k,v in out_dict.items():
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file1 = open(file_path+f"{k}.txt", "w")
        for value in v:
            file1.writelines(f"{value},")
        file1.close()

#For httprobe, we write IPs with port 80 and 443 open into a file
elif (inp == 2):
    file_path2 = './for_httprobe/'
    if not os.path.exists(file_path2):
        os.makedirs(file_path2)

    file2 = open(file_path2+"for_httprobe.txt", "w")
    for k,v in out_dict.items():
        if "80" in v or "443" in v:
            file2.writelines(f"{k}\n")
        else:
            continue
    file2.close()

#Run nmap for service discovery and save results
elif (inp == 3):
    for k,v in out_dict.items():
        s=""
        if len(v) < 2975:
            for value in v:
                s+=value+","
            command = ["nmap", "-T4", "-p"+s, "-A", k, "-oN", k+".nmap_output","-Pn"]
            ext_code = subprocess.run(command)
            print(f"The nmap scan for {k} was run with exit code: {ext_code}")

        elif len(v) > 2975:
            splitted_ports = np.array_split(v, ceil((len(v))/2900))
            count = 0
            for port_group in splitted_ports:
                for port in port_group:
                    s+=port+","
                    command = ["nmap", "-T4", "-p"+s, "-A", k, "-oN", k+"_"+str(count)+".nmap_output","-Pn"]
                # command = ["nmap", "-T4", "-p"+v[0]+"-"+v[-1], "-A", k, "-oN", k+".nmap_output","-Pn"]
                print(command)
                ext_code = subprocess.run(command)
                print(f"The nmap scan for {k} was run with exit code: {ext_code}")
                count+=1
                s=""
        
else:
    print("Your Choice is incorrect. Exiting program")
    print("-"*120)
    sys.exit()

