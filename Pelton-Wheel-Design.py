from prettytable import PrettyTable

import math

z = float(input("Elevation, zr = "))
d0 = float(input("Pipe diameter = "))
f = float(input("Friction factor, f = "))
l = float(input("Length, L = "))
m = int(input("No of elements = "))
delta = d0/m
d1 = 0

table = PrettyTable(['Diameter', 'Area', 'Velocity', 'Power'])
dtable = []
atable = []
vtable = []
ptable = []

for i in range(1, m+1):
    vi = (((2 * 9.81 * z)/(1 + 0.04 * (d1 / d0) ** 4 + f * (l / d0) * (d1 / d0) ** 4)) ** 0.5)
    poweri = (9810 * math.pi * 0.25 * (d1 ** 2) * ((vi ** 3) / (2 * 9.81)))
    areai = (math.pi * 0.25 * (d1 ** 2))
    
    dtable.append(d1)
    atable.append(areai)
    vtable.append(vi)
    ptable.append(poweri)
    
    d1 += delta

for j in range(0, m):
    table.add_row([dtable[j], atable[j], vtable[j], ptable[j]])
n = ptable.index(max(ptable))
vopt = vtable[n]
dopt = dtable[n]

print(table)
print 'Maximum Power at d =',dopt,'; P =',max(ptable)

plt.figure(figsize=(10,5))
aa = plt.figure(1)
plt.plot(dtable, ptable)
plt.title("Power vs Jet Diameter")
plt.xlabel("Jet Diameter")
plt.ylabel("Power")

######################## multiple jets ########################

n= int(input('Max no. of jets = '))
plt.figure(figsize=(10,5))
cc = plt.figure(2)
nn=1
for i in range(1,n+1):
    dtable2 = []
    for j in range(0,m):
        di2 = (atable[j]/(nn*math.pi*0.25))**0.5
        dtable2.append(di2)
    plt.plot(dtable2,ptable)
    plt.legend([i for i in range(1,n+1)])
    nn += 1
plt.title("Power vs Jet Diameter")
plt.xlabel("Jet Diameter")
plt.ylabel("Power")

ww = [50, 75, 100, 125, 150]
plt.figure(figsize=(10,5))
bb = plt.figure(3)
vpipe = ((dopt/d0)**2)*vopt
HE = z - (f*l/d0)*vpipe**2/19.62

for j in range(len(ww)):
    table2=PrettyTable(['No. of Jets','Runner Efficiency'])
    w = ww[j]
    nrtable = []
    njtable = [i for i in range(1,31)]
    for x in range(1,31): #x is no. of jets
	    v = (.2133*w*d0)/((HE*x)**.5)
	    nr = 2*v*(1-v)*(1-.85*math.cos(165*math.pi/180)) #k = .85, Beta = 165
	    nrtable.append(nr)
    for i in range(len(njtable)):
            table2.add_row([njtable[i],nrtable[i]])
    print 'w =',w
    print(table2) 
    plt.plot(njtable,nrtable)
    plt.legend(["50 RPM", "75 RPM", "100 RPM", "125 RPM", "150 RPM"])

plt.title("Runner Efficiency vs No. of Jets")
plt.xlabel("No. of Jets")
plt.ylabel("Runner Efficiency")
plt.show()
