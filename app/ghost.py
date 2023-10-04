desc = """Цель
Приложение, которое бесконечно расширяет возможности человеческой памяти, создает реплику личности. Интересно?)

Описание
Сервис постоянно записывает аудио с вашего телефона. Все ваши диалоги и монологи записываются текстом, с метаданными о спикере, времени, эмоциях, местоположении. Далее эта информация превращается в эмбеддинги (численные представления данных), загружается в векторное хранилище - будущую долговременную память для агента gpt. Всё безопасно зашифровано, и может храниться локально. 

В формате чата можно узнать в точности, какие аргументы вы приводили в защиту нового патча в доте 3 года назад вашему другу, узнать о чем вы говорили на прошлом звонке с командой (функционал otter.ai), или попросить агента проанализировать ваши философские изыскания про смысл жизни. В недалеком будущем, с развитием ASR и LLM, качество этих функций будет заоблачным, хотя уже сейчас работает на 9/10, с кучей недоработок.

Начал вместе с android-разрабом в августе, но он к сожалению выгорел к it в целом. Сделали прототип, протестировали, всё отлично работает.

Под капотом три склееные нейронки для своего SpeechToText, который в 72 раза дешевле OpenAI Whisper. Большой объем работы по ml, backend. От среднего до любого объем работы по mobile и product. 

Стек проекта
ML - torch
Backend - прототип на питоне, mvp можно писать на любом инструменте.
Mobile - прототип на kotlin jetpack compose

Серьёзный или pet
Серьёзный, медленный. В mvp очень много фичей. Сейчас проект заморожен, так как в соло ментально тяжело тянуть такой большой проект и несколько ролей.

Посчитана unit-экономика и проведено большое количество рыночных исследований.

Оплата конечно же процентом от нуля (равноценная доля организации)

UPD: MVP
-смешное мобильное приложение, но должно удовлетворительно записывать и передавать аудио на сервер
-в приложении простейший классификатор речи + кэш на случай, если нет инета или лег сервер
-бэк (скорее девопс) сервер для формирования батчей из аудио для дальнейшей отправки на serverless gpu
-сервер для хранения и взаимодействия(гпт агенты) с векторными хранилищами
-база бэка в виде данных о юзерах, платежах, и тд.

Для кого актуально 
Только для тех, кому нравится идея. Навыки не важны."""

hm = {
    "post_name": "Ghost Ghost Ghost Ghost",
    "post_desc": desc,
    "post_upvotes": 0,
    "post_credentials": ["http://t.me/nonGilgamesh"],
    "post_hashtags": ["#backend", "#ml"],
}
