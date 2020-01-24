import random
import names


class Health:
    def __init__(self, health, delta=10):
        self.health = health
        self.delta = delta

    def decrease(self, power):
        self.health -= power * self.delta

    def check(self):
        return True if self.health > 0 else False

    def __str__(self):
        return f"{self.health}"


class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def __str__(self):
        return self.name

    def get_kick(self, power):
        self.health.decrease(power)

    def still_alive(self):
        return self.health.check()


class Battle:
    winner = None
    winners = []
    battle_num = 1

    def __init__(self, quantity_of_warriors):
        self.quantity = quantity_of_warriors
        self.warriors = self.get_all_warriors()


    def run(self):
        Output.print_process(self.warriors)

        if len(self.warriors) > 1:
            while len(self.warriors):
                self.let_fight()
                self.battle_num += 1
            print('Winners list: ', list(map(lambda x: x.name, self.winners)))

        # if self.winners:
        #     self.warriors = self.winners
        #     print(self.warriors)
        #     self.let_fight()


    def let_fight(self):
        Output.print_battle_num(self.battle_num)
        war1, war2 = self.get_two_warriors()
        Output.print_two_participant(war1, war2)
        Output.print_health_ratio(war1, war2)

        while True:
            two_warrios = [war1, war2]
            random.shuffle(two_warrios)
            attacking_warrior, attacked_warrior = two_warrios
            self.do_attack(attacking_warrior, attacked_warrior)
            Output.print_health_ratio(war1, war2)
            if not attacked_warrior.still_alive():
                self.winner = attacking_warrior
                self.winners.append(self.winner)
                print(f"{self.winner} won!")
                break


    def get_all_warriors(self):
        warname = [names.get_full_name() for name in range(self.quantity)]
        health = [random.randint(100, 200) for i in range(self.quantity)]
        power = [round(random.uniform(0.5, 3), 1) for i in range(self.quantity)]
        return [Warrior(warname[i], Health(health[i]), power[i]) for i in range(self.quantity)]


    def get_two_warriors(self):
        war1 = self.warriors.pop(random.randrange(len(self.warriors)))
        war2 = self.warriors.pop(random.randrange(len(self.warriors)))
        return [war1, war2]

    def do_attack(self, attacking_warrior, attacked_warrior):
        attacked_warrior.get_kick(attacking_warrior.power)


class Output:
    @staticmethod
    def print_health_ratio(war1, war2):
        print(f"{war1.health} : {war2.health}")

    @staticmethod
    def print_two_participant(war1, war2):
        print('---' * 3 + f' {war1} VS {war2} ' + '---' * 3)

    @staticmethod
    def print_battle_num(battle_num):
        print('---' * 5 + f' Battle {battle_num}: ' + '---' * 5)

    @staticmethod
    def print_process(warriors):
        if warriors:
            print('***' * 4 + ' WARRIORS: ' + '***' * 4)
            for war in warriors:
                print(war.name, f'(Health-{war.health}, Power-{war.power})')
            if len(warriors) > 1:
                print('***' * 4 + ' Fight starts! ' + '***' * 4)
            else:
                print(
                    '---' * 10,
                    "\nThe battle impossible!\n"
                    f"{warriors[0]} has no any competitor!",
                )

        else:
            print(
                "The battle impossible!\n"
                "Any warrior wasn't found!"
            )



battle = Battle(4)
battle.run()
