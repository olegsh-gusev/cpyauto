import random
import string
import time
import uuid

import requests

import pywinauto
from pywinauto import application

number = {1: (150, 540),
          2: (250, 540),
          3: (370, 540),
          4: (150, 590),
          5: (250, 590),
          6: (370, 590),
          7: (150, 640),
          8: (250, 640),
          9: (370, 640),
          0: (250, 680)
          }

sex = {
    "m": (400, 202),
    "w": (400, 232)
}

names = [("Александр", "m"),
         ("Михаил", "m"),
         ("Максим", "m"),
         ("Артем", "m"),
         ("Даниил", "m"),
         ("Марк", "m"),
         ("Иван", "m"),
         ("Лев", "m"),
         ("Дмитрий", "m"),
         ("Матвей", "m"),
         ("Роман", "m"),
         ("Тимофей", "m"),
         ("Кирилл", "m"),
         ("Илья", "m"),
         ("Никита", "m"),
         ("Андрей", "m"),
         ("Федор", "m"),
         ("Егор", "m"),
         ("Алексей", "m"),
         ("Константин", "m"),
         ("Владимир", "m"),
         ("Ярослав", "m"),
         ("Мухаммад", "m"),
         ("София", "m"),
         ("Мария", "w"),
         ("Анна", "w"),
         ("Алиса", "w"),
         ("Виктория", "w"),
         ("Полина", "w"),
         ("Ева", "w"),
         ("Елизавета", "w"),
         ("Александра", "w"),
         ("Анастасия", "w"),
         ("Варвара", "w"),
         ("Дарья", "w"),
         ("Ксения", "w"),
         ("Вероника", "w"),
         ("Василиса", "w"),
         ("Арина", "w"),
         ("Екатерина", "w"),
         ("Милана", "w"),
         ("Екатерина", "w"),
         ("Кира", "w"),
         ("Валерия", "w"),
         ("Мирослава", "w"),
         ("Ульяна", "w"),
         ("Вера", "w"),
         ("Амина", "w"),
         ("Таисия", "w"),
         ]
last_names = ["Гусь", "Лось",	"Крот", "Холод", "Царь", "Князь", "Шабан", "Юсуп", "Бык"]
country_codes = [0, 0, 0, 135, 0, 2, 0, 11, 0, 115, 0, 6, 0]
# # sms_active_key = '7c27f8c57d46c48ff1726643e85Ac37b'
# sms_active_key = "28ee25c3e7d1f3d03A631fccdA0A7dbb"


def get_number(attempt=0):
    code = 0
    try:
        code = country_codes[attempt]
    except Exception as e:
        pass
    get_key = 'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getNumber&service=fb&country={}'.format(
        sms_active_key, code)
    key_info = requests.get(get_key)
    # 'ACCESS_NUMBER:325929094:77715984276'
    data_sms_active = key_info.text
    print("key")

    if data_sms_active == 'NO_BALANCE':
        raise Exception('NO_BALANCE')
    if data_sms_active == 'NO_NUMBERS':
        print("NO_NUMBERS")
        time.sleep(5)
        if attempt + 1 >= len(country_codes):
            return None, None
        else:
            return get_number(attempt + 1)

    try:
        data_split = data_sms_active.split(":")
        phone = data_split[2]
        id = data_split[1]
    except Exception:
        if attempt + 1 >= len(country_codes):
            return None, None
        else:
            return get_number(attempt + 1)
    return phone, id


def get_status(id):
    return requests.get(
        'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getStatus&id={}'.format(
            sms_active_key, id)).text


def get_pass(length):

    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def get_key(id):
    try:
        status_text = get_status(id)
        if status_text == "STATUS_WAIT_CODE":
            print(status_text)
            time.sleep(15)
            return get_key(id)
        if "STATUS_OK" in status_text:
            return status_text.split(":")[1]
    except Exception as e:
        return None


def start():

    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    try:
        time.sleep(35)
        # pywinauto.mouse.move(coords=(640, 340))
        pywinauto.mouse.click(coords=(640, 340))
        # delete_user_from_phone()

        time.sleep(15)
        pywinauto.mouse.click(coords=(250, 320))
        time.sleep(2)
        pywinauto.mouse.click(coords=(313, 330))
        time.sleep(2)
        # Name
        name = random.choice(names)
        last_name = random.choice(last_names)
        pywinauto.keyboard.send_keys(name[0])
        time.sleep(2)
        pywinauto.mouse.click(coords=(322, 198))
        time.sleep(3)
        pywinauto.keyboard.send_keys(last_name)
        time.sleep(2)
        pywinauto.mouse.click(coords=(320, 230))
        time.sleep(5)
        # Phone
        pywinauto.mouse.click(coords=(250, 250))
        for i in range(15):
            time.sleep(0.01)
            pywinauto.keyboard.send_keys('{BACKSPACE}')

        time.sleep(0.5)
        phone_number, id = get_number(0)
        print(phone_number)
        pywinauto.keyboard.send_keys(str(phone_number))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(313, 288))
        # DOB
        # day

        time.sleep(0.5)
        first_day_n = random.randint(1, 2)
        pywinauto.mouse.click(coords=(number.get(first_day_n)[0], number.get(first_day_n)[1]))
        time.sleep(0.5)
        first_day_n = random.randint(0, 9)
        pywinauto.mouse.click(coords=(number.get(first_day_n)[0], number.get(first_day_n)[1]))

        # month
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(number.get(1)[0], number.get(1)[1]))
        time.sleep(0.5)
        first_month_n = random.randint(0, 2)
        pywinauto.mouse.click(coords=(number.get(first_month_n)[0], number.get(first_month_n)[1]))

        # year
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(number.get(1)[0], number.get(1)[1]))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(number.get(9)[0], number.get(9)[1]))
        time.sleep(0.5)
        first_year_n = random.randint(5, 9)
        pywinauto.mouse.click(coords=(number.get(first_year_n)[0], number.get(first_year_n)[1]))
        time.sleep(0.5)
        first_year_n = random.randint(0, 9)
        pywinauto.mouse.click(coords=(number.get(first_year_n)[0], number.get(first_year_n)[1]))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(303, 245))

        # sex
        time.sleep(0.5)
        user_sex = sex.get(name[1])
        pywinauto.mouse.click(coords=(user_sex[0], user_sex[1]))

        # password
        time.sleep(0.5)
        password = "EWr@213123"
        pywinauto.keyboard.send_keys(password)
        passwordn = get_pass(random.randint(3, 7))
        time.sleep(0.7)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        passwordn = str(random.randint(100, 90907))
        time.sleep(0.5)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        print(password)
        try:
            file2write = open(phone_number, 'w')
            file2write.write(password)
            file2write.close()
        except Exception:
            pass
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(283, 250))

        # reg
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(283, 250))
        time.sleep(20)

        # save data
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(180, 680))

        # get sms_code
        code = get_key(id)
        if code is None:
            pywinauto.mouse.click(coords=(180, 680))
            time.sleep(2)
            pywinauto.mouse.click(coords=(280, 400))
            delete_user_from_phone()
            time.sleep(5)
            app.kill()
        else:
            print(code)
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(220, 200))
            time.sleep(0.5)
            pywinauto.keyboard.send_keys(str(code))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(220, 235))
            time.sleep(15)

            # log settings
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(90, 480))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(385, 75))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(385, 75))
            time.sleep(10)
            pywinauto.mouse.click(coords=(190, 680))
            time.sleep(10)
            pywinauto.mouse.click(coords=(400, 70))
            time.sleep(3)
            pywinauto.mouse.press(coords=(350, 170))
            time.sleep(0.1)
            pywinauto.mouse.scroll(coords=(350, 170), wheel_dist=-1)
            time.sleep(0.1)
            pywinauto.mouse.release(coords=(350, 170))
            time.sleep(0.1)
            pywinauto.mouse.press(coords=(350, 170))
            time.sleep(0.1)
            pywinauto.mouse.scroll(coords=(350, 170), wheel_dist=-1)
            time.sleep(0.1)
            pywinauto.mouse.release(coords=(350, 170))
            pywinauto.mouse.click(coords=(150, 690))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(250, 350))
            print("ok")
            delete_user_from_phone()
            app.kill()

    except Exception:
        app.kill()


def delete_user_from_phone():
    time.sleep(1)
    pywinauto.mouse.click(coords=(400, 130))
    time.sleep(1)
    pywinauto.mouse.click(coords=(300, 250))
    time.sleep(0.5)
    pywinauto.mouse.click(coords=(300, 430))


if __name__ == '__main__':
    start()
