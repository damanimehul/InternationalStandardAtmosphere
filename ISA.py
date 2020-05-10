# International standard atmosphere
from math import e 
height=float(input('Enter height here: '))
P_0= 101325
t_0= 288.15
p_0= 1.225
g=9.80665
R=287
expo= -g/R
t=0
lapserate=[(11000,11000,-.0065),(20000,9000,0),(32000,12000,.001),(47000,15000,.0028),(51000,4000,0)]
for element in lapserate:
    if height>= element[0] and (element[2]!=0):
        tempt=t_0
        t_0= t_0 + element[2]*element[1]
        P_0= P_0 * (t_0/tempt)**(expo/element[2])
        p_0=p_0 * (t_0/tempt)**((expo/element[2])-1)
    elif height>= element[0]:
        P_0= P_0 * e**(expo*(element[1]/t_0))
        p_0= p_0 * e**(expo*(element[1]/t_0))
    elif (t<height<element[0]) :
        if element[2]!=0:
           tempt=t_0
           t_0= t_0 + element[2]*(height-t)
           P_0= P_0 * (t_0/tempt)**(expo/element[2])
           p_0=p_0 * (t_0/tempt)**((expo/element[2])-1)
           break
        else :
           tempt=t_0
           P_0= P_0 * e**(expo*((height-t)/tempt))  
           p_0= p_0 * e**(expo*((height-t)/tempt))
           break
    t =element[0]  
soundspeed=(1.4*R*t_0)**(.5)   
print('Temperature : '+ str(round(t_0,3))+' '+'Kelvin')
print('Pressure is:' +str(round(P_0,3))+' '+'Pascal')    
print('Density is:'+ str(round(p_0,4))+' ' +'Kg/m**3')        
print('Speed of sound is:'+str(round(soundspeed,3))+' '+'m/s') 
