import re

def parser():
    arr = []

    months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }

    with open("/home/irvus/Programming/hse/python_project/Space_Corrected.csv") as f:  # TODO добавить относ. путь
        for line in f.readlines():
            array = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)

            for i in range(len(array)):
                array[i] = re.sub('\n', '', array[i])  # cutting quotes and \n
                array[i] = array[i].strip('\"').strip()

                try:
                    array[i] = int(array[i])  # here I change strings to integer and float
                except ValueError:
                    try:
                        array[i] = float(array[i])
                    except ValueError:
                        pass

                if i == 4 and array[4] != 'Datum':  # Here I change date format to 'yyyy.mm.dd hh.mm Dow',
                    date_arr = array[4].replace(',', '').replace(':', '.').split()  # Dow is equal to day of week

                    date = date_arr[3] + '.' + months[date_arr[1]] + '.' + date_arr[2] + ' '
                    try:
                        date += (date_arr[4] + ' ' + date_arr[0])
                    except IndexError:
                        pass

                    array[4] = date
            arr.append(array[1:])
    return arr


# print(parser())
