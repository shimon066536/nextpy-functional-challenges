class BigThing:
    def __init__(self, env):
        self._env = env

    def size(self):
        return self._env if isinstance(self._env, int) else len(self._env)

class BigCat(BigThing):
    def __init__(self, env, weight):
        super().__init__(env)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        return self._weight

cutie = BigCat("mitzy", 3)
print(cutie.size())
