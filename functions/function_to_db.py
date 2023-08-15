import psycopg2

from classes.add_info_to_db import AddInfo
from classes.class_db import DBManager
from config import config
from utils import path_to_sql_script


def add_info_to_db():
    """
    Функция для добавления информации о компаниях и вакансиях в БД
    """
    add_info = AddInfo()
    add_info.add_companies()
    add_info.add_vacancies()


def work_with_db():
    """
    Функция для получение информации из БД по заданным критериям
    """

    work_db = DBManager()
    print("Получение списка всех компаний и количество открытых вакансий у каждой компании:")
    work_db.get_companies_and_vacancies_count()
    print("\nПолучение списка всех вакансий с указанием названия компании,"
          "названия вакансии и зарплаты и ссылки на вакансию:")
    work_db.get_all_vacancies()
    print("\nПолучение среднюю зарплату по вакансиям:")
    work_db.get_avg_salary()
    print("\nПолучение списка всех вакансий, у которых зарплата выше средней по всем вакансиям:")
    work_db.get_vacancies_with_higher_salary()
    print("\nПолучение списка всех вакансий, в названии которых содержатся переданные в метод слова:")
    work_db.get_vacancies_with_keyword()


def create_db():
    """Создание базы данных (использовал название vacancies)"""

    params = config()

    conn = psycopg2.connect(dbname='postgres', **params)
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE vacancies ")

        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE vacancies ")

    conn.close()


def create_table():

    with open(path_to_sql_script, 'r') as file:
        open_file = file.read()
        params = config()
        conn = psycopg2.connect(dbname='vacancies', **params)
        with conn:
            with conn.cursor() as cur:
                cur.execute(open_file)

        conn.close()


def main():
    """
    Функция с основным скриптом

    """
    print("Здравствуйте, для правильной работы будет создана новая база данных vacancies ")
    create_db()
    print("\nСоздание таблиц  в БД vacancies: ")
    create_table()
    print("\nДобавление данных в БД vacancies: ")
    add_info_to_db()
    print("\nПолучение данных из БД vacancies: ")
    work_with_db()
