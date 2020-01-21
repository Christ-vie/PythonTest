class Myclass:
    life = 3
    def attack(self):
        print('maman')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('maman na nga ')
        else:
            print(str(self.life) + 'life left ')
myclass1 = Myclass()
myclass1.attack()
myclass1.checkLife()