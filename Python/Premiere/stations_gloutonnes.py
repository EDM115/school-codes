r=100
d=[23, 40, 12, 44, 21, 9, 67, 32, 51, 30, 11, 55, 24, 64, 32, 57, 12, 80]
dist=0
i=0
stations = []
'''while i<len(d):
    while i<len(d)-1 and dist+d[i]<=r:
        dist = dist + d[i]
        i=i+1
    dist=0
    stations.append(i-1)
print(stations)'''
while i<len(d):
    tmp=dist+d[i]
    dist = dist + d[i]
    i=i+1
    dist=0
    stations.append(i-1)
print(stations)
