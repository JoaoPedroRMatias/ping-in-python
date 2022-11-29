import os

def myping(host):
    response = os.system("ping " + host)
    
    if response == 0:
        return True
    else:
        return False
        
ip = str(input('IP / URL: '))
print(myping(ip))