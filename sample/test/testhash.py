import md5
import base64
from datetime import *
src = 'this is a md5 test.'
m1 = md5.new()
m1.update(src)
print m1.hexdigest()

import hashlib

m2 = hashlib.md5()
m2.update(src)
test=m2.hexdigest()
print test

a='1234'
b=base64.encodestring(a)
print b

print datetime.utcnow