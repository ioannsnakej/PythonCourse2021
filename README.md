# Пуш в личный Azure
git remote remove origin
git remote add origin https://ioannsnakej@dev.azure.com/ioannsnakej/Python/_git/Python
git push

# Пуш в Evraz Azure
git remote remove origin
git remote add origin https://tfs.msk.evraz.com/tfs/%D0%9F%D0%BE%D1%80%D1%82%D1%84%D0%B5%D0%BB%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/%D0%A6%D0%A2_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5/_git/Ivan-Khodyrev-Homework
git push

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