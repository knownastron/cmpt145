class Hero(object):
    def __init__(self, name, power, sid):
        self._name = name
        self._power = power
        self.__secret = sid

    def say_hello(self):
        print('Hello, evil-doers! My name is', self._name + '!')
        print('My super power is', self._power, 'so you better beware.')

    def divulge(self):
        print('Do you want to know my secret identity?', self.__secret)


if __name__ == '__main__':
    bruce = Hero('Batman', 'martial arts', 'Bruce Wayne')
    bruce.say_hello()

    print(bruce._name)
    print(bruce.__secret)

    bruce.divulge()
    bruce._power = 'rich'
    bruce.say_hello()
    bruce.__secret = "likes bats"
    bruce.divulge()
    print(bruce.__secret)

