import sys
import paramiko
#import optparse

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]



client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
