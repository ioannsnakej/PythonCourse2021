# base python

git remote add origin <br/>
git push -u origin --all
# My name is Khodyrev Ivan
Меня зовут Ходырев Иван Сергеевич<br/>
Это мой новый репозиторий, созданный лишь с одной целью - <br/>
пройти данный курс от начала до конца и освоить базовые навыки программирования на языке Python.<br/>
После чего, с полученными мной знаниями, я напишу личный ИИ. Передам ему все свои знания и буду жить вечно.

# virtual env
Создание:
python -m venv env
-m — флаг для запуска venv как исполняемого модуля.
env — название виртуального окружения (где будут храниться ваши библиотеки).

Активация:
env/Scripts/activate.ps1 - для Windows;
source env/bin/activate - для Linux и MacOS.

Деактивация: 
deactivate

# pydantic
Install: pip install pydantic

pip list - выводит список установленных пакетов

python -m pip install --upgrade pip - обновляет pip

pip freeze - выводит все установленные зависимости

pip freeze > requirements.txt - создает текстовый документ, в котором перечислены все установленные зависимости