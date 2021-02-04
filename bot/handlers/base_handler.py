class Handler:
    def __init__(self):
        self._keys = []
        self.description = ''

    @property
    def keys(self):
        return self._keys
    
    @keys.setter
    def keys(self, mas):
        for key in mas:
            self._keys.append(key.lower())

    def process(self, data):
        pass
