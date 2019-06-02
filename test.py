class a:
    def __init__(self):
        self.kk = b()
    def ww(self):
        print('aaaaaa')
        self.kk.bb()
class b:
    def __init__(self):
        self.ss = a()
    def bb(self):
        print('bbbbbb')
        self.ss.ww()
