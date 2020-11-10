# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_star_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects

def read_int(line):
    """Переводит запись больших чисел с символом Е в обычный вид

    Параметры:

    **line** - строка с числом
    """
    exist_E = False
    for symbol in line:
        if symbol == "E":
            exist_E = True
    if exist_E:
        return float(line[0: (line.index("E"))]) * 10 ** (int(line[line.index("E") + 1: len(line)]))
    else:
        return float(line)


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.split()
    star.R = read_int(line[1])
    star.color = line[2]
    star.m = read_int(line[3])
    star.x = read_int(line[4])
    star.y = read_int(line[5])
    star.Vx = read_int(line[6])
    star.Vy = read_int(line[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line = line.split()
    planet.R = read_int(line[1])
    planet.color = line[2]
    planet.m = read_int(line[3])
    planet.x = read_int(line[4])
    planet.y = read_int(line[5])
    planet.Vx = read_int(line[6])
    planet.Vy = read_int(line[7])



def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if isinstance(obj, Star):
                object_type = "star"
            else:
                object_type = "planet"
            out_file.write(object_type, str(obj.r), str(obj.color), str(obj.m), str(obj.x), str(obj.y), str(obj.Vx), str(obj.Vy))
if __name__ == "__main__":
    print("This module is not for direct call!")
