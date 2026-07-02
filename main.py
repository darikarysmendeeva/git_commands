# git - системф контроля версий(кода)
# github/gitlab/bitbucket - хранилище/сайт для хранения (версий )кода

# repository/репозиторий - папка в которой git отслеживает изменения 

# git init - создания репозитория 

# git status - проврка статуса отслеживания

# git add <file_name> or . - добавления файла в список отслеживания (в staging area)


# git commit -m 'пишем что хотим написать' - создания/ фиксация версии кода с сообщением

# git commit -am 'some message' -добавление существующего файла в список отслеживание 
# и фиксации/создание версии кода с сооббщением

# git remote add <variable_name>( often origin) <link to repository> - связка локального репозитория с удаленным и сохранени ссылки в переменную

# git push origin <branch_name> - отправка версии кода в удаленной репозиторий 



# BRANCH/ВЕТКА - КОПИЯ КОДА НЕЗАВИСИМАЯ ОТ ОСНОВНОЙ ВЕРСИИ КОДА  ( ЧЕРНОВИК ГРУБО ГОВОРЯ)

# git branch - вывод списка веток 
# git branch <new_branch_name> - создание новой ветки
# git checkout <branch_name> - переход на указанную ветку 

# git checkout -b <new_branch_name> - создание новой ветки и переход на указанную ветку 

# git merge <branch_name> - склеивание веток. Склеивает указанную ветку к текущей(в которой мы щас находимся)

# git pull origin <branch_name> - стягивание/ добавление изменений с указанной ветки в текущей


# git clone <link_to_repository> - скачивание/клонировани указанного репозитория


# .gitignore -файл со списками диретори/файлов для игнорирования git

# 
import os

print(os.environ['PASSWORD'])
print(os.environ['USERNAME'])