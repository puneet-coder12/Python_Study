username = "Puneet"
username = "Chai"


# python m har cheez obj hoti h to pehle memory m puneet ka reference store hoga fir chai ka reference store hoga to memory m 2 alag alag reference store honge
# to pehle username puneet ka refernce store hoga baad reference change hoke chai ka reference store hoga to memory m 2 alag alag reference store honge
# isliye y immutable kehte h(kyunki vo us reference ko change nahi kr sakte), python m garbage collector h to jo reference kaam m nhi aa rha h usko delete kr dega

x = 15
y = x
x = 10

# isme x aur y ki value alag hoti kyunki baad m 10 memory m store hoga aur 15 memory m store hoga to dono alag alag reference store honge isliye y immutable kehte h

# MUTABLE------------------------------------------
# list
# set
# dict
# bytearray

# UNMUTABLE------------------------------------------
# int
# float
# complex
# bool
# str
# tuple
# frozenset
# bytes
# NoneType


# jo garbage collector h vo number aur string ko immmediately delete nhi karta kyunki python ek number language h to baar baar assign aur reassign ho skte h isliye to immediately memory se uska reference delete nhi karta h