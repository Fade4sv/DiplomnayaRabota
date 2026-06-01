export PATH="$PATH:/c/allure-2.42.0/bin"
export JAVA_HOME="/c/allure-2.42.0/jdk-25.0.3+9"
export PATH="$JAVA_HOME/bin:$PATH"
# Папка для сырых результатов тестов (JSON, XML файлы от pytest + allure)
results=./results

# Папка с историей предыдущих отчетов Allure (для графиков трендов)
rep_history=./final-report/history

# Папка для финального HTML отчета Allure
report=./final-report

# Удаляем папку с предыдущими результатами тестов
# 2>/dev/null перенаправляет ошибки в никуда (чтобы не было сообщений если папки нет)
rm -rf $results 2>/dev/null

# Запускаем тесты и сохраняем результаты в папку $results
# --alluredir указывает куда сохранять сырые данные для Allure
python -m pytest --alluredir=$results

# Переносим историю из старого отчета в новые результаты
# Это нужно для построения графиков трендов в Allure
# || true означает: "если команда mv завершится ошибкой, продолжаем выполнение"
# Ошибка будет если папки $rep_history не существует (первый запуск)
mv $rep_history $results 2>/dev/null || true

# Удаляем предыдущий сгенерированный HTML отчет
rm -rf $report 2>/dev/null

# Преобразуем сырые данные в красивый HTML отчет
# -o указывает выходную папку для отчета
allure generate $results -o $report

# Автоматически открываем сгенерированный отчет в браузере по умолчанию
allure open $report