import sys
import binascii
import os
r=sys.argv[1]
f=open(r,"rb")
f.seek(709)
ftest=f.read(3)
f.seek(708)
fftest=f.read(3)
f.seek(0)
ffftest=f.read(5000)
faxman = ffftest.find(b'\x01\x67\x64')
if ftest == b'\x01\x67\x64':
    print('file check OK. Type1')
    r9=r.replace(".h264", ".h26")
    z=open(r9,'bw')
    f.seek(709)
    data=f.read()
    header=b'\x00\x00\x00\x01\x09\x10\x00\x00\x00'
    z.write(header)
    z.write(data)
    z.close()
elif fftest == b'\x01\x67\x64':
    print('file check OK. Type2')
    r9=r.replace(".h264", ".h26")
    z=open(r9,'bw')
    f.seek(708)
    data=f.read()
    header=b'\x00\x00\x00\x01\x09\x10\x00\x00\x00'
    z.write(header)
    z.write(data)
    z.close()
elif faxman != -1 :
    faxman = ffftest.find(b'\x01\x67\x64')
    print(faxman)
    print('warning. may be invalid.')
    r9=r.replace(".h264", ".h26")
    z=open(r9,'bw')
    f.seek(faxman)
    data=f.read()
    header=b'\x00\x00\x00\x01\x09\x10\x00\x00\x00'
    z.write(header)
    z.write(data)
    z.close()
else :
    print('file check error')