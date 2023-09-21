#!/bin/bash

# 1. Переключаемся на ветку dev
git checkout dev

# 2. Сливаем изменения из master (или другой ветки, которую вы используете как основу для prd)
git merge main

# 3. Собираем и тестируем ваше приложение

# 4. Если тестирование прошло успешно, создаем тег с номером ревизии
git tag v1.0

# 5. Переключаемся на ветку prd
git checkout prd

# 6. Сливаем изменения из dev
git merge dev

# 7. Пушим изменения в prd
git push origin prd

# 8. Пушим тег в удаленный репозиторий
git push --tags

# 10. Завершаем процесс
