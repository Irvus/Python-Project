import re

def parser():
    arr = []

    with open("/home/irvus/Programming/hse/python_project/Space_Corrected.csv") as f:  # TODO добавить относ. путь
        for line in f.readlines():
            array = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)  # TODO remove \n, ""

            for i in range(len(array)):
                array[i] = re.sub('\n', '', array[i])
                array[i] = array[i].strip('\"')

            arr.append(array)

        print(arr)


parser()
