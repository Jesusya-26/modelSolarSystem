import sqlite3

DATA = sqlite3.connect('solar_objects_db.db').cursor().execute("""SELECT * FROM SolarObjects""")
DATA = [list(i) for i in DATA]
SOLAR_IMAGES = ['images/sun.png', 'images/mercury.png', 'images/venerus.png', 'images/earth.png',
                'images/mars.png', 'images/jupiter.png', 'images/saturn.png', 'images/uran.png',
                'images/neptun.png','images/pluton.png']
SOLAR_OBJECTS = []


class SolarObject:

    def __init__(self, view, image, *args):
        self.view = view
        self.image = image
        self.description = args[0]
        self.name = self.description[1]

    def __str__(self):
        main_data = [i for i in self.description[2:11]]
        atmosphere, describe = [], []
        for i in range(len(self.description[11])):
            if i % 150 == 0:
                atmosphere.append(self.description[11][:i + 1])
        for i in range(len(self.description[12])):
            if i % 150 == 0:
                describe.append(self.description[12][:i + 1])
        atmosphere, describe = '\n'.join(atmosphere), '\n'.join(describe)
        return f'Тип: {main_data[0]}\nРасстояние от Солнца: {main_data[1]} а.е.\n' \
               f'Период обращения вокруг Солнца (в земных годах): {main_data[2]}\n' \
               f'Эксцентриситет: {main_data[3]}\nОрбитальная скорость: {main_data[4]} км/с\n'\
               f'Плотность: {main_data[5]}x10^3 кг/м^3\nУскорение свободного падения: {main_data[6]} м/с^2\n' \
               f'Масса (в массах Земли): {main_data[7]}\nКоличество спутников: {main_data[8]}\n' \
               f'Состав атмосферы: {atmosphere}\nОписание: {describe}'

    def animate(self):
        return


for i in range(10):
    SOLAR_OBJECTS.append(SolarObject(None, SOLAR_IMAGES[i], DATA[i]))

print(DATA)