import sys


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
