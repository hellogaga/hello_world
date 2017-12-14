import subprocess

p=subprocess.Popen(['hcitool', 'name', '60:83:34:BD:3E:96'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,errors=p.communicate()
print output
