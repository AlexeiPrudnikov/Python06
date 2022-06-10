import random
allCandies = 2021
minStep = 1
maxStep = 28
def GetStep (allCandies):
    while (True):
        step = int(input('Игрок, введите количество конфет, которое Вы берете: '))
        if (step < minStep) or (step > maxStep) or (step > allCandies):
            print(f'Ошибка ввода, можно взять от {minStep} до {maxStep} и меньше либо равно {allCandies} конфет.')
        else:
            return step
def StepBot(allCandies):
    candies = allCandies % (maxStep + 1)
    if candies == 0: return random.randint(minStep, maxStep)
    return candies
def PlayerName(first):
    if first: return 'Бот'
    else: return 'Игрок'
print('Происходит жеребьевка...')
first = random.randint(1, 2)
flag = bool(first - 1)
print('Происходит жеребьевка...')
print(f'Ходит первым {PlayerName(flag)}')
print(f'Осталось {allCandies} конфет')
while allCandies > 0:
    if flag:
        step = StepBot(allCandies)
        print(f'Бот взял {step} конфет')
    else:
        step = GetStep(allCandies)
    allCandies -= step
    print(f'Осталось {allCandies} конфет')
    if allCandies == 0:
        print(f'{PlayerName(flag)} победил!')
    flag = not flag
