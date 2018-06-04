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

    def set_name(self, name):
        self._name = name

    def set_power(self, power):
        self._power = power

    def __str__(self):
        return 'The famous super-hero ' \
               + self._name + ' has ' + self._power \
               + ' as a super-power.'

if __name__ == '__main__':
    diana = Hero()
    diana.say_hello()

    bruce = Hero()
    bruce.set_name('Batman')
    bruce.set_power('martial arts')
    bruce.say_hello()

    print(bruce)
    print(diana)



