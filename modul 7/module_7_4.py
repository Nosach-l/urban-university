team1_name = 'Мастера кода'
team1_num = 5
score_1 = 40
team1_time = 1552.512

team2_name = 'Волшебники данных'
team2_num = 6
score_2 = 42
team2_time = 2153.31451
tasks_total = score_1 + score_2

print('В команде "%s" участников: %d!' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда "{name}" решила задач: {score} !'.format(name=team1_name, score=score_1))
print('{} решили задачи за {} с !'.format(team1_name, team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team1_name}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды {team2_name}!')
else:
    print('Ничья!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {(team1_time+team2_time)/tasks_total} секунды на задачу!')
