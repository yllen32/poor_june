from __future__ import annotations

"""Модуль содержащий класс для построения URL."""

import settings as set


class JuneURL():
    """Класс описывающий эндпоинт сайта hh.ru для поиска работы.

        Обьект данного класа содержит свойста:
            area: регион поиска (по умолчанию ЦФО и СЗО)
            exp: опыт работы (по умолчанию от 1 до 3 лет)
            role: специализации (по умолчанию программист/разработчик и
        системный администратор)
            schedule: график работы (удаленная работа по умолчанию)
            search_fields: поиск по ключевым словам (по умолчанию везде)
            searching_text: текст поиска (по умолчанию "python")
    """

    HH_URL = "https://russia.hh.ru/search/vacancy?<area>&\
experience=<exp>&<roles>&schedule=<schedule>&<search_fields>&\
text=<searching_text>&clusters=true&enable_snippets=true&\
ored_clusters=true&order_by=publication_time&hhtmFrom=vacancy_search_list.\
    "

    def __init__(
        self,
        area="area=232&area=231",
        exp="between1And3",
        roles="professional_role=96&professional_role=113",
        schedule="remote",
        search_fields=
        ("search_field=name&search_field=company_name&search_field=description"),
        searching_text="python"
    ):
        self.area = area
        self.exp = exp
        self.roles = roles
        self.schedule = schedule
        self.search_fields = search_fields
        self.searching_text = searching_text

    def __setattr__(self, name, value) -> None:
        if value is False:
            self.__dict__[name] = ''
        else:
            self.__dict__[name] = value

    @property
    def text_url(self):
        """Метод получения url из обьекта JuneUrl.

            Возвращает строку url составленную из свойств заданых обьекту 
        JuneURL при создании.
        """
        url = self.HH_URL
        for parameter in self.__dict__:
            if parameter is not None:
                url = url.replace(f'<{parameter}>', self.__dict__[parameter])
        return url

def create_params_from_settings():
    """Функция создание параметров для url собирает значения из settings, и 
    преобразует данные из человекопонятных в параметры поиска сайта hh.
        например  зона поиска ЦФО: area=232
    """
    temps = set.SEARCHING_TEMPLATES
    areas =  _full_fill_param(set.AREA, temps['area'])
    if len(set.EXPIRIANCE)>1:
        exp = temps['expiriance']['нет опыта']
    else:
        exp = temps['expiriance'][set.EXPIRIANCE[0].lower()]
    roles = _full_fill_param(set.POSITIONS, temps['roles'])
    schedule = _full_fill_param(set.SCHEDULE, temps['schedule'])
    return areas, exp, roles, schedule


def _full_fill_param(set, temps):
    """
    Функция соединеня параметров для поиска, добавляет & между параметрами.
    """
    param = ''
    for item in set:
        param += temps[item.lower()]
        if item != set[-1]:
            param += '&'
    return param
