class SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_points, catchphprase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_points
        self.catchphprase = catchphprase

    def show_name(self):
        print(f'name hero: {self.name}')

    def hp(self):
        self.health_point *= 2
        print(f'hp: {self.health_point}')

    def __str__(self):
        return f"{self.nickname}, {self.superpower}, probeg: {self.health_point}"

    def __len__(self):
        return len(self.catchphprase)

hero = SuperHero('maqqeen', 'molnia', 'super_skorost', 100, 'KKKKCHAAAOOO!')

hero.show_name()
hero.hp()
print(hero)
print(f'dlinna kchao: {len(hero)}')