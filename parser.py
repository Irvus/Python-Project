import re

def parser():
    arr = []

    with open("/home/irvus/Programming/hse/python_project/Space_Corrected.csv") as f:  # TODO добавить относ. путь
        for line in f.readlines():
            array = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)

            for i in range(len(array)):
                array[i] = re.sub('\n', '', array[i])
                array[i] = array[i].strip('\"').strip()

                try:
                    array[i] = int(array[i])
                except ValueError:
                    try:
                        array[i] = float(array[i])
                    except Exception:
                        pass

            arr.append(array[1:])

    return arr


print(parser())
