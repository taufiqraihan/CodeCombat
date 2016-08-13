# http://codecombat.com/play/level/testbraen
def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo(position) > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (self.isReady("bash")):
            self.bash(target)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        elif (self.isReady("attack")):
            self.attack(target)
        else:
            pass

while True:
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    else:
        enemy = self.findNearest(self.findEnemies())
        if enemy:
            attack(enemy)
            # find some enemy to attack
            # use cleave when ready
