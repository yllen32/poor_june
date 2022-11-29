from __future__ import annotations

"""Модуль содержащий класс для построения URL."""



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

        Подробную информацию как настроить поиск смотри в README

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
            if parameter != None:
                url = url.replace(f'<{parameter}>', self.__dict__[parameter])
        return url
