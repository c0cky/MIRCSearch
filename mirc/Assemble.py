#The magic number for this 13 because I said so
from Circle import Circle
width = 0
MAGIC = 13
class Assemble:

    def __init__(self, ls, w, h):
        width = 0
        self.lst = ls
        self.width = w-(w/8)
        self.height = h-(h/8)
        self.complete = []

    def do_the_work(self):
        #initialize the cirlces
        c0 = Circle(1, 0,0, self.width/2, self.height/2)
        c1 = Circle(4, self.width/4, self.height/4, self.width/2, self.height/2)
        c2 = Circle(8, self.width/2, self.height/2, self.width/2, self.height/2)

        if len(self.lst) > MAGIC: #yes magic number 13
            self.lst = self.lst[0:MAGIC]
        #puts all the individual items into their 'circle'
        for i in range(0, len(self.lst)):
            self.lst[i]['id'] = i
            if c0.is_full() == False:
                c0.add_entry(self.lst[i])
            elif c1.is_full() == False:
                c1.add_entry(self.lst[i])
            elif c2.is_full() == False:
                c2.add_entry(self.lst[i])

        c0.compute()
        c1.compute()
        c2.compute()

        self.complete = c0.to_list()
        self.complete = self.complete + (c1.to_list())
        self.complete = self.complete + (c2.to_list())


    def to_list(self):
        return self.complete


