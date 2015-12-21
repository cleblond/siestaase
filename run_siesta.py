import os

#serial on penrose
#siesta = '/home/cleblond/siestaase/siesta_serial'
#exitcode = os.system('%s < %s.fdf > %s.txt' % (siesta, label, label))

#parallel 
siesta = '/home/cleblond/siestaase/siesta_qrsh_wrap'
exitcode = os.system('%s %s.fdf > %s.txt' % (siesta, label, label))
