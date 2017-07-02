class base {
	exec { "sudocmd":
    	path => ["/usr/bin/","/usr/sbin/","/bin"],
    	command => "yum update -y",
    	user => root,
	}
       
	package { "binutils-devel":
        ensure => present,
    }

	package { "gcc":
	ensure => present,
    }

	package {"python-devel":
	ensure => present,
    }

	package {"subversion":
	ensure => present,
    }

	package {"gcc-gfortran":
	ensure => present,
     }

	package {"gcc-c++":
	ensure => present,
     }

       service { "condor":
	ensure => running,
	enable => true,
     }
     
      service { "cvmfs_config probe":
	ensure => running,
	enable => true,
     }
     
		
}
include base 
