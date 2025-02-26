# # HW - 3 - Inhertiance - Medium to Hard - Our Dictionary

class MyDict(dict):   
    def __setitem__(self, key, value):
        print(f'Update {key} : {value}')
        if type(key) is float:
            print(f'Do Convergence to  {int(key)}',end='')
            key = int(key)
        print()
        super().__setitem__(key, value)

    def update(self, iterable = None, **kwargs):
        if iterable:
            kwargs.update(iterable)
        for key, val in kwargs.items:
            self[key] = val

    def set_default(self, key, val=None):
        if key in self:
            return self[key]
        self[key] = val
        return val


dct = MyDict()
dct[10.5] = 20
dct[(4, 5)] = 'Mostafa'
print(10.5 in dct)
print(dct)

