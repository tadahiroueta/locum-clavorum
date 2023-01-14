import pynput
from time import sleep

ky = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()


def click(x, y):
    ms.move(-1600, -900)
    ms.move(x, y)
    sleep(0.1)
    ms.click(pynput.mouse.Button.left)
    sleep(0.1)


def ctrl(ltt):
    ky.press(pynput.keyboard.Key.ctrl)
    ky.type(ltt)
    sleep(0.1)
    ky.release(pynput.keyboard.Key.ctrl)
    sleep(0.1)


def altab():
    ky.press(pynput.keyboard.Key.alt)
    ky.press(pynput.keyboard.Key.tab)
    sleep(0.1)
    ky.release(pynput.keyboard.Key.tab)
    ky.release(pynput.keyboard.Key.alt)
    sleep(0.2)


# finds right translation
def translate(phrase):
    lst = open("trans.txt", 'r', encoding='utf-8').readlines()

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == phrase:
            # checks for language
            if i % 2 == 0:
                return lst[i + 1]

            return lst[i - 1]


# picks from multiple choice
def pick(phrase):
    lst = open("txt.txt", 'r', encoding='utf-8').readlines()
    for i in range(len(lst)):
        if len(lst[-i]) > 2:
            if lst[-i][2:] == phrase:
                ky.type(lst[-i][0])
                return

    ky.type('1')


print("\nHow many points do you want?")
goal = int(input('>>>    '))
# opening shit
# closing pycharm
click(1420, 15)

# Type here to search
click(100, 845)
sleep(3)
ky.type('txt.txt')
sleep(1.5)
ky.type('\n')
sleep(2)

# Seid ihr das Essen? Nein, wir sind der Jäger!
lastNut = 0
count = 0
while goal > 0:
    # exit key if you will
    if ms.position[0] >= 1500 and ms.position[1] >= 800:
        print("Oh shit!")
        exit()

    trns = open("trans.txt", "a+", encoding='utf-8')

    # reads the screen
    click(200, 400)
    ctrl('a')
    ctrl('c')
    altab()
    ctrl('a')
    ctrl('v')
    ky.type('\n')
    ctrl('s')
    altab()

    # chooses
    lst = open("txt.txt", 'r', encoding='utf-8').readlines()
    for i in range(len(lst)):
        if len(lst[-i]) >= 5:
            # learns
            if lst[-i] == 'English\n':
                trns.write(lst[-i - 1] + lst[1 - i])
                break

            # multiple-chooses
            if lst[-i][: 4] == 'Pick':
                pick(translate(lst[-i - 1]))
                break

            # typing
            if lst[-i][: 4] == 'Type':
                click(600, 370)
                ky.press(pynput.keyboard.Key.backspace)
                ky.release(pynput.keyboard.Key.backspace)
                if translate(lst[-i - 1]) is None:
                    ky.type("Fuck it doesn't work with audio!")

                else:
                    ky.type(translate(lst[-i - 1])[: -1])

                break

            # scoring
            if lst[-i][: 5] == 'Total':
                divid = lst[-i].split(' ')
                if int(divid[2]) != lastNut:
                    goal -= int(divid[2])
                    lastNut = int(divid[2])
                    count = 0

                else:
                    count += 1

                break

            # doesn't ignore
            if lst[-i] == 'Ignore?\n':
                click(950, 275)
                break

            # doesn't subscribe or something else
            if lst[-i] == 'Subscribe now\n' or count >= 10:
                click(20, 40)
                sleep(10)
                count = 0
                break

            # comes back to exercises
            if lst[-1] == 'Memrise logo\n':
                click(1040, 380)
                sleep(10)
                break

            # logs in
            if lst[-1] == 'LOGIN\n':
                click(55, 50)
                sleep(10)
                break

    sleep(0.2)
    ky.type('\n')
    sleep(0.5)

ctrl('t')
sleep(0.2)
ky.type("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")
