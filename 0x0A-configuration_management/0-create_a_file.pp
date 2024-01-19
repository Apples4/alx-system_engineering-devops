# Creates a temp file

file { '/tmp/school':
  path    => '/tmp/school',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
}
