# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:07:33 2020

@author: RDxR10

input1:
30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102202f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e001

input2:
30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102203602aff824a32c19825425704546145d5fbc282ee912089923e824f46867647b01

Here we notice that the "r" values are equal which means that deriving the private key would be easy
which is:
r=d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad1
(r1=r2)
We need to find out the s values from the inputs as well so just after the "r" value we get:

from input 1    
s1=2f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e0

from input 2
s2=9a5f1c75e461d7ceb1cf3cab9013eb2dc85b6d0da8c3c6e27e3a5a5b3faa5bab

Now we use the formula:
private key = (z1*s2 - z2*s1)/(r*(s1-s2))

to find the private key. This vulnerability was exploited for hacking bitcoin wallet.
We did not want to give the actual values for z(which would specify the exact hacking case)
so we have given other values(which are not actual) just for the CTF. 



"""
def inverse_mod( a, m ):
    """Inverse of a mod m."""
    if a < 0 or m <= a: a = a % m
    # From Ferguson and Schneier, roughly:
    c, d = a, m
    uc, vc, ud, vd = 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod( d, c ) + ( c, )
        uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc

    # At this point, d is the GCD, and ud*a+vd*m = d.
    # If d == 1, this means that ud is a inverse.
    assert d == 1
    if ud > 0: return ud
    else: return ud + m


p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
r = 0xd47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad1
s1= 0x2f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e0
s2= 0x3602aff824a32c19825425704546145d5fbc282ee912089923e824f46867647b
z1= 0xc0e2d0a89a348de88fda08211c70d1d7e52ccef2eb9459911bf977d587784c6e
z2= 0x17b0f41c8c337ac1e18c98759e83a8cccbc368dd9d89e5f03cb633c265fd0ddc

h1 = r*(s1-s2)  
p1 = (z1*s2) - (z2*s1)
PK = hex((p1*inverse_mod(h1, p)) % p)
print(PK[2:])
