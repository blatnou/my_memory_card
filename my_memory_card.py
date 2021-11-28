from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 
import time

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.passed = False
        self.quan = None
class QuestionAnswer():
    def __init__(self, number, answer, isRight):
        self.number = number
        self.answer = answer
        self.isRight = isRight

class WindowKek(QWidget):
    def __init__(self):
        super().__init__()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            if btn_OK.text() == 'Ответить':
                rbtn_1.setChecked(True)
            elif btn_OK.text() == 'Начать тест':
                RBVariant1.setChecked(True)
        if e.key() == Qt.Key_2:
            if btn_OK.text() == 'Ответить':
                rbtn_2.setChecked(True)
            elif btn_OK.text() == 'Начать тест':
                RBVariant2.setChecked(True)
        if btn_OK.text() == 'Ответить':
            if e.key() == Qt.key_3:
                rbtn_3.setChecked(True)
            if e.key() == Qt.key_4:
                rbtn_4.setChecked(True)
        if e.key() == Qt.Key_Enter or e.key() == 16777220:
            if btn_OK.text() == 'Ответить':
                check_answer()
            elif btn_OK.text() == 'Следующий вопрос':
                next_question
            elif btn_OK.text() == 'Начать тест':
                start_test()
            elif btn_OK.text() == 'Заново':
                reset_all()
        print('код клавиши:',e.key())

        
questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Название нашей группы в телеге', 'Clay Boot', 'Blay Coot', 'Boo Boo', 'tooB yalC'))
questions_list.append(Question('С какой из этих стран Чехия не граничит?', 'Венгрия', 'Австрия', 'Польша', 'Германия'))
questions_list.append(Question('Какая из этих кислот является витамином?', 'Никотиновая', 'Яблочная', 'Янтарная', 'Молочная'))
questions_list.append(Question('Какую икру больше всего любил Джеймс Бонд?', 'Белужью', 'Севрюжью', 'Стерляжью', 'Осетровую'))
questions_list.append(Question('Какой химический элемент был назван в честь злого подземного гнома?', 'Кобальт', 'Гафний', 'Бериллий', 'Теллур'))
questions_list.append(Question('Какого зайца НЕ бывает?', 'Чувак', 'Тумак', 'Русак', 'Беляк'))
questions_list.append(Question('Какая планета совершает 1 оборот вокруг солнца со скоростью 47,9 км/с', 'Меркурий', 'Марс', 'Юпитер', 'Сатурн'))
questions_list.append(Question('Чему равна сумма чисел от 0 до 100 включительно?', '5050', '3525', '1000', '7550'))
questions_list.append(Question('Какой буквой физики обозначают ускорение свободного падения?', 'g', 'f', 'n', 'm')) 
 
app = QApplication([])

GBSelectTestType = QGroupBox('Выберите способ прохождения теста')
VBLSelect = QVBoxLayout()
RBVariant1 = QRadioButton('Показ ответа после вопроса')
RBVariant2 = QRadioButton('Показ статистики после теста')
RBVariant1.setChecked(True)
VBLSelect.addWidget(RBVariant1)
VBLSelect.addWidget(RBVariant2)
GBSelectTestType.setLayout(VBLSelect)

btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
 
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 

ResultGB = QGroupBox('')
resV = QVBoxLayout()
res_label_total = QLabel('Всего:')
res_label_correct = QLabel('Правильных:')
res_label_wrong = QLabel('Неправильных:')
res_label_rating = QLabel('Рейтинг:')

resV.addWidget(res_label_total, alignment=Qt.AlignLeft)
resV.addWidget(res_label_correct, alignment=Qt.AlignLeft)
resV.addWidget(res_label_wrong, alignment=Qt.AlignLeft)
resV.addWidget(res_label_rating, alignment= Qt. AlignLeft)
ResultGB.setLayout(resV)
ResultGB.hide()

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox) 
layout_line2.addWidget(ResultGB) 
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_all_results():
    window.setWindowTitle('Результаты теста')
    lb_Question.setText('Результаты')
    res_label_total.setText('Всего: ' + str(window.total))
    res_label_correct.setText('Правильных: ' +str(window.score))
    res_label_wrong.setText('Неправильных: ' +str(window.total - window.score))
    res_label_rating.setText('Рейтинг:' +str(int(window.score/window.total*100)) + '%')
    
    
    
    
    ResultGB.show()
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    btn_OK.setText('Заново')
    
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)                                                                                                                                                                                                                     
    answers[2].setText(q.wrong2)                                                                                                                                                                                                                     
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    questions_list[window.target].passed = True
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
    if window.total == len(questions_list):
        btn_OK.setText('Результаты')
            
    
 
def next_question():
    window.setWindowTitle('Memo Card - Вопрос {} из {}'.format(window.total+1, len(questions_list)))                                                                                                                                                                                            
    while True:
        rindex = randint(0, len(questions_list) - 1)
        question = questions_list[rindex]
        if not question.passed:
            break
    window.target = rindex
    window.total += 1
    ask(question)
 
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    elif btn_OK.text() == 'Результаты':
        show_all_results()
    elif btn_OK.text() == 'Заново':
        window.score = 0
        window.total = 0
        window.target = 0
        for item in questions_list:
            item.passed = False
        ResultGB.hide()
        next_question()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
 
btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит


startime = time.time()
window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()