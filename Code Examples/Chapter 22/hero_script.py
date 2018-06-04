import HeroD as Hero

bruce = Hero.Hero("Batman", "super smart", "Bruce Wayne")

bruce.say_hello()

print(bruce._name)
print(bruce._power)

bruce._power = "martial arts"

bruce.say_hello()


