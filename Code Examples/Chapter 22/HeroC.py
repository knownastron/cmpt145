class Hero(object):
    def __init__(self):
        self._name = None
        self._power = None

    def say_hello(self):
        if self._name is None:
            print('The hero remains strangely silent, as if trying to think of a name.')
        else:
            print('Hello, evil-doers! My name is', self._name + '!')
            print('My super power is', self._power, 'so you better beware.')


if __name__ == '__main__':
    bruce = Hero()
    bruce.say_hello()

    bruce._name = 'Batman'
    bruce._power = 'martial arts'
    bruce.say_hello()

    print(bruce)



