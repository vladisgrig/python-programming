"""
Класс multifilter, выполняет ту же функцию, что и стандартный класс filter, 
но использует не одну функцию, а несколько. 

Решение о допуске элемента принимается на основании того, 
сколько функций допускают этот элемент (pos), и сколько не допускают (neg).

Решающая функция – это функция, которая принимает два аргумента – количества pos и neg, 
и возвращает True, если элемент допущен, и False иначе.
"""

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        
        self.it = iterable
        self.f = funcs
        self.a = []
        self.j = judge
        for i in self.it:
            self.pos = 0
            self.neg = 0
            for func in self.f:
                if func(i) == True:
                    self.pos += 1
                else:
                    self.neg += 1
            if self.j(self.pos, self.neg) == True:
                self.a.append(i)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return iter(self.a)