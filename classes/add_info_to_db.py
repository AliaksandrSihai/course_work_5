import psycopg2

from classes.get_company_info import GetCompaniesInfo
from classes.get_vacancy_info import GetVacanciesInfo
from config import config


class AddInfo:
    """
    Класс для добавления информации в БД
    """
    params = config()
    conn = psycopg2.connect(dbname='vacancies', **params)

    def add_companies(self):
        """
        Добавление информации о компаниях в БД
        """
        companies = GetCompaniesInfo()
        info_to_add = companies.amount_info()
        to_db = []
        for info in info_to_add:
            for x in info:
                values = [int(value) if str(value).isdigit() else value for value in x.values()]
                to_db.append(values)
        with self.conn:
            with self.conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO companies(company_id, company_name, company_url, "
                    "company_area, company_industries, quantity_open_vacancies) "
                    "VALUES(%s, %s, %s, %s, %s, %s)", to_db)

        return to_db

    def add_vacancies(self):
        """
         Добавление информации о вакансиях компаний в БД(добавлено по 100 вакансий от каждой компании)
        """
        vacancies = GetVacanciesInfo()
        info_to_add = vacancies.amount_info()
        to_db = []
        for info in info_to_add:
            for x in info:
                values = [int(value) if str(value).isdigit() else value for value in x.values()]
                to_db.append(values)
        with self.conn:
            with self.conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO vacancies(vacancy_id, vacancy_name, vacancy_url, vacancy_area, "
                    "vacancy_requirement, vacancy_responsibility, vacancy_salary, vacancy_published_date, company_id) "
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", to_db)

        return to_db
