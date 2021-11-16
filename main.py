import random

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    qText = StringProperty("Кто изобрел кубик Рубика?")
    qVar1 = StringProperty("Китайцы")
    qVar2 = StringProperty("Эрно Рубик")
    qVar3 = StringProperty("Какой-то студент")
    qVar4 = StringProperty("Я")
    correctAnswer = ""
    roundQuestion = {}
    curRound = NumericProperty(0)
    statusText = StringProperty()
    buttonsDisabled = BooleanProperty(False)
    maxRound = 2

    money = NumericProperty(0)
    curQuestionMoney = NumericProperty()

    roundMoney = {
        1: 100,
        2: 500,
        3: 1000
    }

    # вопросы для игры
    questions = {
        1: [{
            "text": "Кто изобрел кубик Рубика?",
            "variants": ["Юрий Гагарин", "Илон Маск", "Джет Ли", "Эрно Рубик"],
            "corAnswer": "Эрно Рубик"
        },
            {
            "text": "Кто придумал таблицу Менделеева?",
            "variants": ["Д. И. Менделеев", "Томас Эдисон", "Хымики", "Юрий Гелий"],
            "corAnswer": "Д. И. Менделеев"
        }]
        ,
        2: [{
            "text": "Какого раунда нет в Бравл Старз?",
            "variants": ["Захват кристаллов", "Броулербаскетбол", "Столкновение", "Броулербол"],
            "corAnswer": "Броулербаскетбол"
        },
            {
                "text": "Продолжите фразу: расцветали яблони и груши..",
                "variants": ["Поплыли туманы над рекой", "Поплыли галоши по реке", "Выходила на берег она", "В небе синем сокол пролетал"],
                "corAnswer": "Поплыли туманы над рекой"
            }
        ]
    }

    # функция вызовется вначале работы
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.curRound = 1

        self.playRound(0)


    def playRound(self, dt):
        print("Играем раунд " + str(self.curRound))

        self.roundQuestion = random.choice(self.questions[self.curRound])

        self.qText = self.roundQuestion["text"]

        random.shuffle(self.roundQuestion["variants"])

        self.qVar1 = self.roundQuestion["variants"][0]
        self.qVar2 = self.roundQuestion["variants"][1]
        self.qVar3 = self.roundQuestion["variants"][2]
        self.qVar4 = self.roundQuestion["variants"][3]

        self.correctAnswer = self.roundQuestion["corAnswer"]
        self.buttonsDisabled = False

        self.statusText = "Подумайте хорошенько"
    def onButtonClick(self, arg):
        print("Нажали вариант " + str(arg))

        self.buttonsDisabled = True

        if self.correctAnswer == self.roundQuestion["variants"][arg]:
            print("Верный ответ!")
            self.statusText = "И это..."
            Clock.schedule_once(self.winRound, 2)

        else:
            print("Ошибка")
            self.statusText = "И это..."
            Clock.schedule_once(self.loseRound, 2)


    def loseRound(self, dt):
        self.statusText = "Неверный ответ"
    def winRound(self, dt):
        self.statusText = "Правильный ответ"

    #    self.money = self.roundMoney[self.curRound]


        if self.curRound == self.maxRound:
            self.statusText = "Конец игры, вы победили"
        else:
            self.curRound += 1

            Clock.schedule_once(self.playRound, 2)


class QuestGame(App):
    pass

QuestGame().run()