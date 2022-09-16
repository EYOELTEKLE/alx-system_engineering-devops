# puppet project


package {'Flask':
  ensure   => '2.1.1',
  provider => 'pip',
}
