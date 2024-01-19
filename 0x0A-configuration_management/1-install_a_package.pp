# Using Puppet, install flask from pip3

package { 'flask':
  ensure      => '2.1.0',
  description => 'installing flask from pip3',
  provider    => 'pip3'
}
