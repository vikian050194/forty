Воспроизведение:
- начал 25ого в 12+
- вызвал get 28ого в 7+

Лучшим решение будет внедрение возможности проверять корректность данных.

На данный момент корректность заключается в том, что если день рабочий, то он обязательно закрыт (есть `finish` действие).

Предпроверка частично решает эту проблему, но если вчерашний день не закрыт и попытаться закрыть его сегодня, то эта же предпроверка не даст этого сделать.

Возможные решения:
- Добавать обработку флага `--force`, которые будет означать игнорирование предпроверки. Кажется, что флаг `--output=plain` вписывается в концепцию флагов, применимых к любой или почти любой команде.
- Реализовать как `check_before`, так и `check_after` декораторы. На `status` навесить первый из них, а на `start` и `finish` - второй.

Выбрано второе решение. Хотя первое никак не противоречит второму, а скорее даже его дополняет.