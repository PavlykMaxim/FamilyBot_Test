BOT_TOKEN: str = ""
SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""

BOT_PREFIX = "!"

EMBED_COLOR = 0xf56114

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

COOKIE_PATH = "/config/cookies/cookies.txt"

STARTUP_MESSAGE = "Запускаем бота..."
STARTUP_COMPLETE_MESSAGE = "Запуск прошел успешно"

MEM_DOG = "░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█\n░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█\n░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█\n░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌\n░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█\n▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌\n█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█\n█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█\n▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌\n▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌\n█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█\n-------------------------MAX--------------------------"

NO_GUILD_MESSAGE = 'Ошибка: Пожалуйста, подключись к голосовому каналу или введите команду в чат'
USER_NOT_IN_VC_MESSAGE = "Ошибка: Пожалуйста, подключись к активному голосому каналу, чтобы использовать команды"
WRONG_CHANNEL_MESSAGE = "Ошибка: Please use configured command channel"
NOT_CONNECTED_MESSAGE = "Ошибка: Бот не подключен ни к одному голосовому каналу"
ALREADY_CONNECTED_MESSAGE = "Ошибка: Бот уже подключен к голосовому каналу"
CHANNEL_NOT_FOUND_MESSAGE = "Ошибка: Не могу найти голосовой канал "
DEFAULT_CHANNEL_JOIN_FAILED = "Ошибка: Не могу подключиться к стандартному голосовому каналу"
INVALID_INVITE_MESSAGE = "Ошибка: Неверная ссылка-приглашения"

ADD_MESSAGE_1 = """```Чтобы подключить бота к своему серверу, нажми на ссылку:
                ```\n<https://discordapp.com/"""
ADD_MESSAGE_2 = "&scope=bot>"

INFO_HISTORY_TITLE = "Отыгравшие песни:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

"""---- DIRECT ----"""
COMMAND_DIRECT_NAME = "direct"
COMMAND_DITECT_ALIASES = ['dm', 'd', 'ls']

SONGINFO_UPLOADER = "Автор: "
SONGINFO_DURATION = "Длительность: "
SONGINFO_SECONDS = "с"
SONGINFO_LIKES = "Лайки: "
SONGINFO_DISLIKES = "Дизлайки: "
SONGINFO_NOW_PLAYING = "Сейчас играет: "
SONGINFO_QUEUE_ADDED = "Добавлена в очередь"
SONGINFO_SONGINFO = "Информация о песне"
SONGINFO_UNKNOWN_SITE = "Неизвестный сайт :question:"
SONGINFO_PLAYLIST_QUEUED = "Треки в очереди :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Длительность неизвестна"

HELP_ADDBOT_SHORT = "Добавить бота на другой сервер"
HELP_ADDBOT_LONG = "Ссылка для добавления бота на другой сервер."
HELP_CONNECT_SHORT = "Подключить бота к голосовому каналу"
HELP_CONNECT_LONG = "Подключает бота к голосовому чату в котором ты находишься"
HELP_DISCONNECT_SHORT = "Отключить бота от голосового канала"
HELP_DISCONNECT_LONG = "Отключить бота от голосового канала и остановить проигрывание."

HELP_SETTINGS_SHORT = "Посмотреть и установить настройки бота"
HELP_SETTINGS_LONG = "Посмотреть и настроить бота на сервере. Использование: {}settings setting_name значение".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Показать историю песен"
HELP_HISTORY_LONG = "Показать " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " песен, которые уже отыграли."
HELP_PAUSE_SHORT = "Поставить на паузу"
HELP_PAUSE_LONG = "Пауза. Продолжить можно командой 'Продолжить'"
HELP_VOL_SHORT = "Поменять громкость %"
HELP_VOL_LONG = "Изменяет громкость плеера. Нужно указать число в %. Так будет установлена громкость плеера."
HELP_PREV_SHORT = "Вернуться на одну песню назад"
HELP_PREV_LONG = "Снова проигрывает предыдущую песню."
HELP_RESUME_SHORT = "Продолжить трек"
HELP_RESUME_LONG = "Продолжает работу плеера."
HELP_SKIP_SHORT = "Пропустить трек"
HELP_SKIP_LONG = "Пропускает песню, которая сейчас играет и запускает следующую из очереди"
HELP_SONGINFO_SHORT = "Информация о играющей песне"
HELP_SONGINFO_LONG = "Показывает детали песни, которая сейчас играет."
HELP_STOP_SHORT = "Остановить трек"
HELP_STOP_LONG = "Останавливает плеер и очищает очередь"
HELP_YT_SHORT = "Проигрывание трека по ссылки или по названию"
HELP_YT_LONG = ("!p [ссылка/название песни/ключевые слова/ссылка на плейлист/ссылка на youtube/]")
HELP_BOT_PING_SHORT = "Pong"
HELP_BOT_PING_LONG = "Проверяет ответ бота"
HELP_VERSION_SHORT = "Показать версию"
HELP_VERSION_LONG = "Показывает версию бота"
HELP_CLEAR_SHORT = "Очистить очередь"
HELP_CLEAR_LONG = "Очищает очередь и пропускает текущую песню."
HELP_LOOP_SHORT = "Зациклить воспроизведение песни 'on/off'."
HELP_LOOP_LONG = "Зацикливает играющую песню и блокирует очередь. напиши команду еще раз, чтобы включить/выключить функцию."
HELP_QUEUE_SHORT = "Показывает песни в очереди"
HELP_QUEUE_LONG = "Показывает до 10 песен, которые находятся в очереди."
HELP_SHUFFLE_SHORT = "Перемешать очередь"
HELP_SHUFFLE_LONG = "Рандомно сортирует песни в очереди"
HELP_CHANGECHANNEL_SHORT = "Меняет канал бота"
HELP_CHANGECHANNEL_LONG = "Меняет канал бота на тот, в котором ты находишься"

HELP_CMD_SHORT = "Вывести команды"
HELP_CMD_LONG = "Показывает все доступные комманды. Использование: {}cmd".format(BOT_PREFIX)
HELP_CL_SHORT = "Очистка"
HELP_CL_LONG = "Очищает чат от сообщений. Использование:{}cl чтобы очистить все или".format(BOT_PREFIX) + " {}cl *количество_сообщений*, чтобы удалить несколько сообщений".format(BOT_PREFIX)
HELP_SUCK_SHORT = "Посылает человека"
HELP_SUCK_LONG = "Пошли человека, который тебе не нравится(совершенно анонимно :japanese_goblin:)"
HELP_HELLO_SHORT = "Поприветствуй человека от своего имени"
HELP_HELLO_LONG = "Пришли человеку приветствие от своего имени"
HELP_PING_SHORT = "Проверить пинг"
HELP_PING_LONG = "Проверить свой пинг на сервере"
HELP_ROLEINFO_SHORT = "Прочитать описание ролей"
HELP_ROLEINFO_LONG = "Прочитай описание всех ролей использующихся на сервере"
HELP_FLIP_SHORT = " Кинуть жребий "
HELP_FLIP_LONG = " Подкидывает монетку и получаешь *Орел* или *Решка* "
HELP_ROLL_SHORT = " Выводит рандомное число "
HELP_ROLL_LONG = " Выдает рандомное число. Использование: {}roll - выводит рандомное число от 0 до 100".format(BOT_PREFIX) + " {}roll N. Выводит рандомное число от 0 до N [N - любое число]".format(BOT_PREFIX)
HELP_DIRECT_SHORT = " Написать сообщение в директ "
HELP_DIRECT_LONG = " Отправляет сообщение в ЛС человеку. Использование: {}dm @nickname".format(BOT_PREFIX)
HELP_HELP_SHORT = " Выводит доступные комманды"
HELP_HELP_LONG = " Показывает все доступные команды. Так же можно посмотреть точную информацию о нужной команде введя {}help command_name".format(BOT_PREFIX)
HELP_BL_SHORT = "Делает буквы большими!"
HELP_BL_LONG = "Переводит **ЛАТИНСКИЙ** текст в большие буквы!"
HELP_KISS_LONG = "Поцелуй кого-нибудь"
HELP_KISS_SHORT = "Поцелуй кого-нибудь"



"""
""" """---- CMD ----""" """
COMMAND_CMD_NAME = "cmd"
COMMNAND_CMD_ALIASES = ['']

""" """---- HELLO ----""" """
COMMAND_HELLO_NAME = 'hello'
COMMAND_HELLO_ALIASES = ['hi', 'привет']

""" """---- CL ----""" """
COMMAND_CL_NAME = "cl"
COMMAND_CL_ALIASES = ['']

""" """---- SUCK ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']



""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']

""" """---- CMD ----""" """
COMMAND__NAME = ""
COMMAND__ALIASES = ['']
"""

""" @commands.command(name='cl', description=config.HELP_CLEAR_LONG, help=config.HELP_CLEAR_SHORT) #Очистка канала .cl [количество сообщений] (очистить нужное кол-во сообщений)// !clear (чистит 100 последних сообщений).
    async def _clear(self, ctx, amount = 100):
        await ctx.channel.purge(limit = amount + 1)"""


"""
async def _cmd(self, ctx):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(colour=0xf57114, title='Комманды')
        emb.add_field(name='!cmd', value=config.HELP_CMD_SHORT)
        emb.add_field(name='!suck', value='Пошли кого-то! [!suck @{nickname}]')
        emb.add_field(name='!hello', value='Поздоровайся с собеседником! !hello @nickname')
        emb.add_field(name='!ping', value='Проверить пинг')
        emb.add_field(name='!clear', value='Очистить чат [!clear {количество_сообщений} или !clear]')
        emb.add_field(name='!roleinfo', value='Выводит информацию о роли [!roleinfo название_роли]')
        emb.add_field(name='!flip', value='Кидает монетку (Орел или Решка)')
        emb.add_field(name='!roll', value='Выдает рандомное число [!roll (0-100), !roll {число} (0-число)]')
        emb.add_field(name='!dm', value='Написать человеку в ЛС [!dm @nickname {текст сообщения}')
        await ctx.send(embed=emb)
"""


BOT_VERISON = '' #do not modify
ABSOLUTE_PATH = '' #do not modify