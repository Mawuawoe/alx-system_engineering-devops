#!/usr/bin/pup
# Install specific version of flask (2.1.0)
# Ensure pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Install a specific version of Werkzeug compatible with Flask 2.1.0
package { 'werkzeug':
  ensure   => '2.1.1',  # or another compatible version
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
