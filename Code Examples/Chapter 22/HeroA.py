class Hero(object):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def say_hello(self):
        print('Hello, evil-doers! My name is', self._name + '!')
        print('My super power is', self._power, 'so you better beware.')


if __name__ == '__main__':
    bruce = Hero('Batman', 'martial arts')
    bruce.say_hello()

    diana = Hero('Wonder Woman', 'super strength')
    diana.say_hello()



