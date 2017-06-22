
# modules 
from fabric.api import *

#host list where puppet client to be installed 

env.hosts = ['node1','node2','node3']

# Set the username
env.user   = "root"

# Set the password

env.password = "your_password"

def  install():
    #commands to be executed 
     
    run("yum update -y")
    run("yum install puppet -y ")
    run("echo server = master >> /etc/puppet/puppet.conf")
    run("echo runinterval = 1440m >> /etc/puppet/puppet.conf")
    run("service puppet start")
    result = run("service puppet status")
    result.failed
#function name will be used during script execution

def update_install():

     install()
