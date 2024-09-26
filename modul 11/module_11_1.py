# Requests — это модуль для языка Python, который используют для упрощения работы с HTTP-запросами.
# Он удобнее и проще встроенного Urllib
# Ранее в "Лекция. Как создать и запустить поток" мы уже использовали этот модуль
# Рассмотрим основные методы этого модуля:

# OPTIONS
# Метод OPTIONS нужен, чтобы спросить сервер о том, какие методы поддерживает ресурс.
# Он редко используется напрямую, обычно вызывается браузером автоматически.
# Поддерживается не всеми сайтами/ресурсами

# GET
# GET — самый распространённый HTTP-метод. Его используют для чтения интернет-ресурса.
# Браузер отправляет метод GET, когда мы открываем какой-либо сайт

# POST
# Метод POST используют для отправки на сервер данных, которые передаются в теле запроса.
# Для этого при вызове requests.post() надо указать аргумент data,
# который принимает на вход словарь, список кортежей, байты или файл.
# Если для передачи данных используется формат JSON, вместо data можно указать json.

# HEAD
# Этот метод очень похож на GET — с той лишь разницей, что HEAD возвращает пустое тело ответа.
# Он нужен, когда нужно посмотреть только на заголовки, не загружая ответ целиком.

# PUT
# Метод PUT очень похож на POST — с той разницей,
# что несколько последовательных вызовов PUT должны приводить к одному и тому же результату.
# POST этого не гарантирует и может привести к неожиданным результатам, например к дублированию созданной сущности.

# PATCH
# PATCH аналогичен методу POST, но с двумя отличиями:
# он используется для частичных изменений ресурса и его нельзя использовать в HTML-формах.
# В теле запроса передается набор модификаций, которые надо применить.

# DELETE
# Метод используется для удаления ресурса.
# Поддерживает передачу данных, однако не требует её: тело запроса может быть пустым.
# Как и PUT, последовательный вызов DELETE должен приводить к одному и тому же результату.

# Pillow
# Библиотека обработки изображений Python добавляет возможности обработки изображений в ваш интерпретатор Python.
# Эта библиотека обеспечивает расширенную поддержку форматов файлов,
# эффективное внутреннее представление и довольно мощные возможности обработки изображений.

# Ранее мы использовали данную библиотеку в практическом задании:
# "Многопроцессное программирование. Практика", где меняли размер и цвет изображения.

# В ЦЕЛОМ, Я ПОСМОТРЕЛ И ИЗУЧИЛ ДОКУМЕНТАЦИЮ КО ВСЕМ БИБЛИОТЕКАМ В СПИСКЕ, НО МНЕ НЕ ХОЧЕТСЯ ЗАНИМАТЬСЯ
# КОПИРОВАНИЕМ И ВСТАВКОЙ ОПИСАНИЯ МЕТОДОВ И ВОЗМОЖНОСТЕЙ ДАННЫХ БИБЛИОТЕК.
# Для себя на данном этапе решил более подробно изучить NumPy,
# а такие библиотеки как pandas и matplotlib пока прочитал поверхностно,
# как будет понимание где их использовать, обязательно изучу более подробно.
# Спасибо за внимание, надеюсь на понимание.