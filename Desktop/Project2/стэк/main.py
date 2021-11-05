"""Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии(стрельба начнётся с патрона, заряженного последним).

Необходимо реализовать класс Stack со следующими методами:
isEmpty - проверка стека на пустоту. Метод возвращает True или False.
push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
size - возвращает количество элементов в стеке.
"""


class Stack:

    def __init__(self):
        self.something = []

    def isEmpty(self):
        return len(self.something) == 0

    def push(self, el):
        self.something.append(el)

    def pop(self):
        return self.something.pop()

    def peek(self):
        return self.something[-1]

    def size(self):
        return len(self.something)

# Задание 2: метод для проверки сбалансированности скобок

    def check_balance(self, string:str):
        for i in string:
            if i in '({[':
                self.push(i)
            elif i in ')]}':
                if self.isEmpty() == True:
                    self.push(i)
                    break
                if i == ')' and self.peek() == '(':
                    self.pop()
                    continue
                if i == ']' and self.peek() == '[':
                    self.pop()
                    continue
                if i == '}' and self.peek() == '{':
                    self.pop()
                    continue
                else:
                    break
        if self.isEmpty() == True:
            print('Сбалансированно')
        else:
            print('Несбалансированно')

if __name__ == '__main__':
    a = Stack()
    a.check_balance('{{[(])]}}')
