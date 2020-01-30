class Myclass:
    life = 3
    def attack(self):
        print('ouch')
        self.life --1
    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life)+ "life left")
myclass1 = Myclass()
myclass1.attack()
myclass1.checkLife()