#!/bin/csh
#setenv PATH /root/anaconda2/bin:$PATH
mv -f *.nc /data/.Trash/
mkdir OUTPUT
mpirun python area_inlinenew.py : python point_em_inline.py : python point_inline.py
mv -f *area.nc ./hb/
cd ./hb/
python addnc_v1.py
mv -f out.nc ../OUTPUT/area.nc
mv -f *.nc ../OUTPUT/

cd ..
mv -f *.nc ./OUTPUT/

