class MyList:
    def __init__(self, iterable=None):
        if iterable is None:
            self._data = []
        else:
            self._data = list(iterable)
            

    def __repr__(self):
        return f"MyList({self._data})"

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self._data + other._data)
        return MyList(self._data + list(other))

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        if isinstance(other, MyList):
            return self._data == other._data
        return False

    def append(self, item):
        self._data.append(item)

    def extend(self, iterable):
        self._data.extend(iterable)

    def insert(self, index, item):
        self._data.insert(index, item)

    def remove(self, item):
        self._data.remove(item)

    def pop(self, index=-1):
        return self._data.pop(index)

    def clear(self):
        self._data.clear()

    def index(self, item, start=0, end=None):
        if end is None:
            return self._data.index(item, start)
        return self._data.index(item, start, end)

    def count(self, item):
        return self._data.count(item)

    def sort(self, key=None, reverse=False):
        self._data.sort(key=key, reverse=reverse)

    def reverse(self):
        self._data.reverse()

    def copy(self):
        return MyList(self._data.copy())