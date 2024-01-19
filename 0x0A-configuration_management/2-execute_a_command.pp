# kills a process named killmenow

exce { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
