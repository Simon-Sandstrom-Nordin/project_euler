class DictHash:

    def __init__(self):
        self.__dict = {}

    def store(self, key, data):
        self.__dict[key] = data

    def search(self, key):
        return self.__dict[key]

    def __contains__(self, key):
        return True if self.__dict[key] else False

    def __getitem__(self, key):
        return self.search(key)
