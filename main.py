
name = input('Введите ваше имя - ')
age = int(input('Введите ваш возраст - '))
#print('Вас зовут - ', name)
#print('Ваш возраст -', age)
if age < 18:
    print(name,', доступ запрещен. Ты слишком молод. Увидимся когда тебе стукнет 18')
else:
    print(name,', добро пожаловать, заходи, разувайся)')


check_point = input('Идем дальше? Введи "Да" или "Нет" ')
if check_point == 'Да':
    print("Погнали дальше")
else:
    print('Пока-пока', name)
    exit()


time_value = int(input('Введи время в секундах '))
second_value = time_value
hour_value = time_value // 3600
minute_value_per = time_value % 3600
minute_value = minute_value_per // 60
second_value_per = minute_value % 60
second_value = second_value_per // 60

print('Its time:', hour_value,':',minute_value,':',second_value)


check_point = input('Идем дальше? Введите "Да" или "Нет"')
if check_point == 'Да':
    print("Погнали дальше")
else:
    print('Пока-пока', name)
    exit()


summary_n = input('Укажите число ')
summary_n_n = "".join([summary_n, summary_n])
summary_n_n_n = "".join([summary_n_n, summary_n])
unit1 = int(summary_n)
unit2 = int(summary_n_n)
unit3 = int(summary_n_n_n)
summary_total = unit1 + unit2 + unit3
print(summary_total)


check_point = input('Идем дальше? Введите "Да" или "Нет"')
if check_point == 'Да':
    print("Погнали дальше")
else:
    print('Пока-пока', name)
    exit()
    

any_num = int(input('Укажите случайное число '))
any_num_string = str(any_num)
any_list = list(map(int, any_num_string))
r = max(any_list)
print(r)

check_point = input('Идем дальше? Введите "Да" или "Нет"')
if check_point == 'Да':
    print("Погнали дальше")
else:
    print('Пока-пока', name)
    exit()


revenue = int(input('Укажите выручку вашей компании '))
costs = int(input('Укажите суммарные издержки '))
total = revenue - costs
if total > 0:
    print('Вы заработали ', total)
else:
    print('Вы потеряли ', abs(total))
if total > 0:
    opp = total / revenue * 100
    print('Рентабельность выручки составляет', int(opp), '%')
else:
    print('Shit happens')
employees = int(input('Укажите количество сотрудников '))
total_on_each_employee = total / employees
print('Прибыль на сотрудника = ', total_on_each_employee)


check_point = input('Идем дальше? Введите "Да" или "Нет"')
if check_point == 'Да':
    print("Погнали дальше")
else:
    print('Пока-пока', name)
    exit()


goal = int(input('Укажите цель на тренировку - '))
train = int(input('Сколько пробежал в первй день - '))
train_counter = 1
while train < goal:
    print('Продолжай тренировки', train)
    train_counter += 1
    train = train * 110 / 100
    train_result = train
    train_result = float('{:.1f}'.format(train))
print('Ура! Вы достигли цель в', goal, 'км за тренировку, вы пробежали', train_result,'км')
print('Вы достигли цели на', train_counter, 'день')
print(name, 'Спасибо за крутые задачки, я кайфанул))')

