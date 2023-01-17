import sys
import os
import subprocess

input_file = sys.argv[1]

with open(input_file) as f:
    out_dict = {}
    lines = f.readlines()
    for line in lines:
        l = line.split()
        # print(l)
        p = l[6].split("/open")
        # print(p)
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


#Host and Ports as different text files (For nmap scanning)
# file_path = './for_nmap/'
# for k,v in out_dict.items():
#     if not os.path.exists(file_path):
#         os.makedirs(file_path)
#     file1 = open(file_path+f"{k}.txt", "w")
#     for value in v:
#         file1.writelines(f"{value},")
#     file1.close()

#For httprobe, we write IPs with port 80 and 443 open into a file
# file_path2 = './for_httprobe/'
# if not os.path.exists(file_path2):
#     os.makedirs(file_path2)

# file2 = open(file_path2+"for_httprobe.txt", "w")
# for k,v in out_dict.items():
#     if "80" in v or "443" in v:
#         file2.writelines(f"{k}\n")
#     else:
#         continue
# file2.close()

#Run nmap for service discovery and save results

for k,v in out_dict.items():
    s=""
    if len(v) < 2975:
        for value in v:
            s+=value+","

    command = ["nmap", "-T4", "-p"+s, "-A", k, "-oN", k+".nmap_output"]
    ext_code = subprocess.run(command)
    print(f"The nmap scan for {k} was run with exit code: {ext_code}")
        


