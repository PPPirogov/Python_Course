class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count+=1
    def reset(self):
        self.count = 0


x = Counter()
x.inc()
print (x.count)
Counter.inc(x)
print (x.count)
Counter.reset(x)
print (x.count)
x.reset()
print (x.count)

a = []
len(a)