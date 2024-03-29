my_str = '''Книга Пророка Иезекииля. Глава 25, Стих 17
**************************************************************
Путь праведника труден, ибо препятствуют ему себялюбивые и тираны из злых людей.
Блажен тот пастырь, кто во имя милосердия и доброты ведёт слабых за собой сквозь долину тьмы.
Ибо именно он и есть тот, кто воистину печётся о ближнем своём и возвращает детей заблудших.
И совершу над ними великое мщение наказаниями яростными, над теми, кто замыслит отравить и повредить братьям моим.
И узнаешь ты, что имя моё Господь, когда мщение моё падёт на тебя.'''
print(my_str)

for s in my_str.split():
    print(s)

list_of_number = []
for i in range(0, 100):
    list_of_number.append(i)
print(list_of_number)
#or
list_of_number_two = list(range(0,100))
print("alternative")
print(list_of_number_two)

quadro_list_of_number = []
for items in list_of_number:
    quadro_list_of_number.append(items*items)
print(quadro_list_of_number)
#or
print("alternative")
list_of_quadro=[items**2 for items in list_of_number_two]
print(list_of_quadro)

my_dict={}
for i in range(10):
    my_dict[i**2]=str(i**2)*3

print(my_dict)