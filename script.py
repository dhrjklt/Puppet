
from fabric.api import *

#host list where client puppet deamind to be installed 

env.hosts = [
 	  'node1',
      'node2',
      'node3',
]
# Set the username
env.user   = "root"



def  install():
    #commands to be executed 

    run("yum install puppet -y ")
    run("echo server = master >> /etc/puppet/puppet.conf")
    run("echo runinterval = 1440m >> /etc/puppet/puppet.conf")
    run("service puppet start")
   # run("puppet agent -t")


def update_install():

    # Update
    dir_update()
