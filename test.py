import random
import string
import time
import uuid

import requests

import pywinauto
from pywinauto import application

number = {1: (450, 540),
          2: (550, 540),
          3: (670, 540),
          4: (450, 590),
          5: (550, 590),
          6: (670, 590),
          7: (450, 640),
          8: (550, 640),
          9: (670, 640),
          0: (550, 680)
          }

sex = {
    "m": (700, 202),
    "w": (700, 232)
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
last_names = ["Гусь", "Лось", "Крот", "Холод", "Царь", "Князь", "Шабан", "Юсуп", "Бык"]
country_codes = [0, 0, 0, 135, 0, 2, 0, 11, 0, 115, 0, 6, 0]


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
    password = ''.join(random.choice(string.ascii_uppercase) for i in range(int(length / 2)))
    return password.join(random.choice(string.ascii_lowercase) for i in range(int(length / 2)))


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


def restart():
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\MultiPlayerManager.exe")
    time.sleep(35)
    pywinauto.mouse.click(coords=(1060, 240))
    time.sleep(2)
    pywinauto.mouse.click(coords=(760, 430))
    time.sleep(2)
    app.kill()
    time.sleep(10)

    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    time.sleep(60)
    app.kill()
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    time.sleep(60)
    pywinauto.mouse.click(coords=(410, 250))
    time.sleep(10)
    pywinauto.mouse.click(coords=(270, 350))
    time.sleep(10)
    app.kill()


def start():
    pywinauto.mouse.move(coords=(640, 340))
    # restart()
    print("start")
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")

    try:
        time.sleep(35)
        # pywinauto.mouse.move(coords=(640, 340))
        pywinauto.mouse.click(coords=(940, 240))
        # delete_user_from_phone()

        time.sleep(15)
        pywinauto.mouse.click(coords=(550, 320))
        time.sleep(2)
        pywinauto.mouse.click(coords=(613, 330))
        time.sleep(2)
        # Name
        name = random.choice(names)
        last_name = random.choice(last_names)
        pywinauto.keyboard.send_keys(name[0])
        time.sleep(2)
        pywinauto.mouse.click(coords=(622, 198))
        time.sleep(3)
        pywinauto.keyboard.send_keys(last_name)
        time.sleep(2)
        pywinauto.mouse.click(coords=(620, 230))
        time.sleep(5)
        # Phone
        pywinauto.mouse.click(coords=(550, 250))
        for i in range(15):
            time.sleep(0.01)
            pywinauto.keyboard.send_keys('{BACKSPACE}')

        time.sleep(0.5)
        phone_number, id = get_number(0)
        if phone_number is None:
            time.sleep(5)
            app.kill()
            time.sleep(5)
            return False
        print(phone_number)
        pywinauto.keyboard.send_keys(str(phone_number))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(513, 288))
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
        pywinauto.mouse.click(coords=(603, 245))

        # sex
        time.sleep(0.5)
        user_sex = sex.get(name[1])
        pywinauto.mouse.click(coords=(user_sex[0], user_sex[1]))

        # password
        time.sleep(0.5)
        password = get_pass(random.randint(3, 7))
        pywinauto.keyboard.send_keys(password)
        passwordn = get_pass(random.randint(3, 7))
        time.sleep(0.7)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        passwordn = str(random.randint(400, 90907))
        time.sleep(0.5)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        print(password)

        time.sleep(0.5)
        pywinauto.mouse.click(coords=(583, 250))

        # reg
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(583, 250))
        time.sleep(20)

        # save data
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(480, 680))

        # get sms_code
        code = get_key(id)
        if code is None:
            pywinauto.mouse.click(coords=(480, 680))
            time.sleep(2)
            pywinauto.mouse.click(coords=(580, 400))
            delete_user_from_phone()
            time.sleep(5)
            app.kill()
            time.sleep(5)
            return False
        else:
            try:
                file2write = open(phone_number, 'w')
                file2write.write(phone_number + " " + password)
                file2write.close()
            except Exception:
                pass
            print(code)
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(520, 200))
            time.sleep(0.5)
            pywinauto.keyboard.send_keys(str(code))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(520, 235))
            time.sleep(15)

            # log settings
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(390, 480))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(685, 75))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(685, 75))
            time.sleep(10)
            pywinauto.mouse.click(coords=(490, 680))
            time.sleep(10)
            pywinauto.mouse.click(coords=(695, 100))
            time.sleep(3)
            pywinauto.mouse.press(coords=(650, 170))
            time.sleep(0.1)
            pywinauto.mouse.scroll(coords=(650, 170), wheel_dist=-1)
            time.sleep(0.1)
            pywinauto.mouse.release(coords=(650, 170))
            time.sleep(0.1)
            pywinauto.mouse.press(coords=(650, 170))
            time.sleep(0.1)
            pywinauto.mouse.scroll(coords=(650, 170), wheel_dist=-1)
            time.sleep(0.1)
            pywinauto.mouse.release(coords=(650, 170))
            pywinauto.mouse.click(coords=(450, 690))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(550, 350))
            print("ok")
            delete_user_from_phone()
            app.kill()
        return True
    except Exception:
        app.kill()
        return False


def delete_user_from_phone():
    time.sleep(1)
    pywinauto.mouse.click(coords=(700, 130))
    time.sleep(1)
    pywinauto.mouse.click(coords=(600, 250))
    time.sleep(0.5)
    pywinauto.mouse.click(coords=(600, 430))


if __name__ == '__main__':
    start()
    iterator = 0
    mistake = 0
    while True:
        if not start():
            mistake += 1
        time.sleep(30)
        iterator += 1
        if iterator >= 10 or mistake > 10:
            iterator = 0
            mistake = 0
            restart()
            