def list_ifname_ip(file):
    f = open(file)
    list1 = list()
    list2 = list()
    d = dict()
    for line in f:
        if 'nameif' in line and if 'no' not in line:
            list1.append(line[7:])
        if 'ip address' in line:
            list2.append((line[11:26],line[27:]))
    d = zip(list1,list2)
    return d
