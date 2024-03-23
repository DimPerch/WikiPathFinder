# Мини-проект WikiParhFinder

## Предыстория
Существует теория, согласно которой абсолютно любая статья Википедии по цепочке ведёт к статье «Философия». Для этого нужно кликать по первой ссылке в каждой статье цепочки. Важно: ссылка должна быть не в скобках и не курсивная. Если ссылка повторяется, следует кликнуть следующую после неё, иначе вы будете ходить по кругу.
Итак: первая ссылка в статье, затем первая ссылка в следующей статье и так далее, пока не доберётесь до философии.

Мне стало интересно проверить это на собственном опыте. Открыв случайную статью, начал выполнять описанные выше действия и, о чудо, я достиг философии. Дальше проснулся спортивный интерес, чтобы автоматизировать это дело.

## О проекте
Я написал небольшой скрипт на `Python`, позволяющий находить путь от исходной статьи, до целевой, в нашем случае до философии.

В классе `WikiPathFinder` представлен метод `find`, позволяющий запустить нахождение пути.

## Использование

Перед запуском убедитесь, что у вас установлены все зависимости из `requirements.txt`. Установить из можно при помощи команды `pip install -r requirements.txt`.
Далее в файле `main.py` укажите ссылку на начальную и целевую статью в качестве аргументов в конструкторе класса `WikiPathFinder`

## Пример работы
В результате выполнения программы вы получите примерно следующий резльутат:
```
WikiPathFinder
source: https://ru.wikipedia.org/wiki/Санкт-Петербургский_государственный_электротехнический_университет
target: https://ru.wikipedia.org/wiki/Философия
Санкт-Петербургский государственный электротехнический университет
1886 год
Григорианский календарь
Солнечный календарь
Календарь
Система счисления
Символ
Традиция
Норма
Представление
Поведение
Процессы приспособления и компенсации
Патологический процесс
Декомпенсация
Орган
Цирроз печени
Печень
Железа
Кровообращение
Кровь
Соединительная ткань
Ткань
Ткацкие переплетения
Ткань
Уток
Нить
Паутина
Шёлк
Кокон
Личинка
Жизненный цикл
Жизненный цикл системы
Концепция
Стратегия
Планирование
Точка зрения
Жизненная позиция
Уникальность
Человек
Разум
Мышление
Познание
Метод
Способности
Личность
Субъект
Индивидуальность
Индивид
Социология
Сообщество
Кубанский государственный университет
Высшее учебное заведение
Общее образование
Профессиональное образование
Умение
Знание
Понимание
Психолингвистика
Психология
Гуманитарные науки
Наука
Деятельность
Сознание
Психика
Понятие
Свойство
Target link found
```
В нём будут перечисленны все статьи википедии, через которые лежит путь до конечной статьи.