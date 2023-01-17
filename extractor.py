import sys
import os

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
file_path = './nmap_output/'
for k,v in out_dict.items():
    # file_name = os.path.join(file_path, k)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file1 = open(file_path+f"{k}.txt", "w")
    for value in v:
        file1.writelines(f"{value},")
    file1.close()
    # with open(file_name,"w") as nfile:
    #     for value in v:
    #         nfile.writelines(f"{value},")
        


