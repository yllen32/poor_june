from datetime import date

from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from log import logger


engine = create_engine('sqlite:///../vacancy_storage.db', echo=False)
Base = declarative_base()


class Vacancy(Base):
    """Класс описывающий таблицу вакансий в бд."""
    __tablename__ = 'vacancys'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    description = Column(String)
    reading_date = Column(Date, default=date.today)

    def __init__(self, url, description):
        self.url = url
        self.description = description


def add_vacancys(items):
    """Функция записи прочитанных вакансий в бд.

    Функция вернет лист со свежими вакансиями, либо None если при чтении hh.ru
    новых вакансий не обнаружено."""
    session = sessionmaker(bind=engine)()
    old_data = [vac.url for vac in session.query(Vacancy)]
    new_data = []
    for item in items:
        url = item['link']
        if url in old_data:
            continue  # если урл уже в бд, то пропускаем его
        description = item["description"]
        new_data.append(Vacancy(url, description))
    if new_data:
        session.add_all(new_data)
        session.commit()
        # заберем данные из обьекта Vacancy перед закрытием сессии
        messages = [(vac.url, vac.description) for vac in new_data]
        session.close()
        return messages
    session.close()
    logger.info('Нет новых вакансий')
    return None


if __name__ == '__main__':
    # создаем бд (sqlite) если она не существует
    try:
        Base.metadata.create_all(engine)
        logger.info('База данных создана')
    except Exception as error:
        logger.critical(f'Не удалось создать баззу данных:\n{error}')
