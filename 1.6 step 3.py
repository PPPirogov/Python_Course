class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list,EvenLengthMixin):
    pass
print(MyList.mro())
x= MyList([1,2,3])
print(x.even_length())
x.append(4)
print(x.even_length())