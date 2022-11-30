# закомментируй если не хочешь искать по даному параметру

# текст по которому производить поиск
SEARCHING_PARAMETER = 'python'

# зона в которой проводить поиск
AREA = [
    "ЦФО",
    "СЗО",
    #"Москва",
    #"Казань",
    #"Санкт-Петербург",
    #"Новосибирск",
    #"Владивосток"
]

# опыт работы
# ВНИМАНИЕ можно выбрать только один вариант
EXPIRIANCE = [
    #"Нет опыта",
    "От 1 до 3 лет",
]

# Желаемая должность
POSITIONS = [
    "Программист-разработчик",
    "Cистемный администратор"
]

SCHEDULE = [
    "Полный день",
    "Удаленная работа"
]


SEARCHING_TEMPLATES={

    'area': {
        'цфо': 'area=232',
        'сзо': 'area=231',
        'москва': 'area=1',
        'казань': 'area=88',
        'санкт-петербург': 'area=2',
        'новосибирск': 'area=4',
        'владивосток': 'area=22',
    },
    'expiriance': {  # только одна может быть в поиске
        'нет опыта': 'noExperience',
        'от 1 до 3 лет': 'between1And3',
    },
    'roles': {
        'программист-разработчик': 'professional_role=96',
        'cистемный администратор': 'professional_role=113',
    },
    'schedule': {
        'полный день': 'schedule=fullDay',
        'удаленная работа': 'schedule=remote'
    }
  }

# писать ли внутри контейнера логи для дебага
DEBUG_LOG = True
