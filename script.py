import paramiko
import sys
import time


HOST = ["compute8", "compute3", "compute4"]
ITERATION = 1

def fn():
  client1=paramiko.SSHClient()
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client1.connect(HOST)
  print "SSH connection to %s established" %HOST
  stdin, stdout, stderr = client1.exec_command('yum install puppet -y')
  stdin, stdout, stderr = client1.exec_command('echo server = master >> /etc/puppet/puppet.conf ')
  stdin, stdout, stderr = client1.exec_command( 'echo runinterval = 1440m >> /etc/puppet/puppet.conf ')
  stdin, stdout, stderr = client1.exec_command( 'service puppet start ')
  stdin, stdout, stderr = client1.exec_command( 'puppet agent -t')
  client1.close()
  print "Logged out of device %s" %HOST


for x in xrange(ITERATION):
    fn()
    print "%s Iteration/s completed" %(x+1)
    print "********"
    time.sleep(5) 
