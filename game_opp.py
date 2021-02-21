"""
-个回合制游戏，每个角色都有hp和power, hp代表血量，power代表攻击力,
定义一个fight方法: .
my_hp = hp - enemy_power
enemy_ final_ .hp = enemy. .hp - my_ .power
两个hp进行对比，血量剩余多的人获胜
"""



class Game:

    # def __init__(self):
    #     # 初始属性
    #     self.my_hp = 1000
    #     self.my_power = 200
    #     self.enemy_hp = 1000
    #     self.enemy_power = 199

    def __init__(self,my_hp,enemy_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199


    # 对打方法

    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp -= self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power
            print(f"我剩余的血量：{self.my_hp} VS 敌人的剩余血量：{self.enemy_hp}")

            # 胜负判断
            if self.my_hp <= 0 :
                print("defeat")
                break
            elif self.enemy_hp <= 0:
                print("win")
                break

    def rest(self,time_num):
        print(f"太累了，休息{time_num}分钟")

if __name__ == '__main__':
    game = Game(1000,1100)
    game.fight()
