def tambah(a,b):
    return a+b

a = tambah(1,2)

print a

def changeme(me):
    me.append(1);

    print "inside of me : ", me

one = ['1','2','3']
changeme(one)

print "out of me : ", one

def specialfn(one, two):
    print one
    print two

specialfn(two = 100, one = 111)