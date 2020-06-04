with open('./fb_64.emd') as f1:
    l1 = f1.readlines()
    for line in l1:
        arr=line.strip().split()
        #print(arr)

with open('./fb_128.emd') as f2:
    l2 = f2.readlines()
    for line in l2:
        arr=line.strip().split()
        #print(arr)

with open('./fb_256.emd') as f3:
    l3 = f3.readlines()
    for line in l3:
        arr=line.strip().split()
        #print(arr)

with open('./lastfm_64.emd') as f6:
    l6 = f6.readlines()
    for line in l6:
        arr=line.strip().split()
        #print(arr)

with open('./lastfm_128.emd') as f4:
    l4 = f4.readlines()
    for line in l4:
        arr=line.strip().split()
        #print(arr)

with open('./lastfm_256.emd') as f5:
    l5 = f5.readlines()
    for line in l5:
        arr=line.strip().split()
        #print(arr)
