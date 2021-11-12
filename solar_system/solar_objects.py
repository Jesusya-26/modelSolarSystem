import sqlite3

DATA = sqlite3.connect('solar_objects_db.db').cursor().execute("""SELECT * FROM SolarObjects""")
DATA = [list(i) for i in DATA]
SOLAR_IMAGES = ['images/sun.png', 'images/mercury.png', 'images/venerus.png', 'images/earth.png',
                'images/mars.png', 'images/jupiter.png', 'images/saturn.png', 'images/uran.png',
                'images/neptun.png','images/pluton.png']
SOLAR_OBJECTS = []
PLANET = None


class SolarObject:

    def __init__(self, objName, view, image, *args):
        self.objName = objName
        self.view = view
        self.image = image
        self.description = args[0]
        self.name = self.description[1]

    def __str__(self):
        main_data = [i for i in self.description[2:11]]
        atmosphere, describe = [], []
        for i in range(len(self.description[11])):
            if len(self.description[11][i + 1:]) < 151 and i == 0:
                atmosphere.append(self.description[11])
                break
            if i % 151 == 0 and i != 0:
                atmosphere.append(self.description[11][:i + 1])
                if len(self.description[11][i + 1:]) < 151:
                    atmosphere.append(self.description[11][i + 1:])
                    break
        for i in range(len(self.description[12])):
            if len(self.description[12][i + 1:]) < 151 and i == 0:
                describe.append(self.description[12])
                break
            if i % 151 == 0 and i != 0:
                describe.append(self.description[12][:i + 1])
                if len(self.description[12][i + 1:]) < 151:
                    describe.append(self.description[12][i + 1:])
                    break
        atmosphere, describe = '\n'.join(atmosphere), '\n'.join(describe)
        return f'Тип: {main_data[0]}\nРасстояние от Солнца: {main_data[1]} а.е.\n' \
               f'Период обращения (в земных годах): {main_data[2]}\nЭксцентриситет: {main_data[3]}\n' \
               f'Орбитальная скорость: {main_data[4]} км/с\nПлотность: {main_data[5]}x10^3 кг/м^3\n' \
               f'Ускорение свободного падения: {main_data[6]} м/с^2\nМасса (в массах Земли): {main_data[7]}\n' \
               f'Количество спутников: {main_data[8]}\nСостав атмосферы:\n{atmosphere}\nОписание:\n{describe}'

    def animate(self):
        return


for i in range(10):
    SOLAR_OBJECTS.append(SolarObject(None, None, SOLAR_IMAGES[i], DATA[i]))
