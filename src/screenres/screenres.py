import subprocess
command = subprocess.Popen(["fbset" , "-s"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
x, err = command.communicate()
y = x.split("\n")
z = y[2].strip().split(" ")
width = int(z[1])
height = int(z[2])


