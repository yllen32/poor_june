from datetime import date

from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hh_parser import BASE_DIR

engine = create_engine(f'sqlite:///../vacancy_storage.db', echo=True)
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
            continue #  если урл уже в бд, то пропускаем его
        description = item["description"]
        new_data.append(Vacancy(url, description))
    if new_data:
        session.add_all(new_data)
        session.commit()
        session.close()
        return new_data
    session.close()
    return None


if __name__ == '__main__':
    Base.metadata.create_all(engine) # создаем бд (sqlite) если она не существует
