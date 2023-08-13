import psycopg2

from classes.add_info_to_db import AddInfo
from classes.class_db import DBManager


def add_info_to_db():
    """
    Функция для добавления информации о компаниях и вакансиях в БД
    """
    add_info = AddInfo()
    add_info.add_companies()
    add_info.add_vacancies()
    return


def work_with_db():
    """
    Функция для получение информации из БД по заданным критериям
    """

    work_db = DBManager()
    print("Получение списка всех компаний и количество открытых вакансий у каждой компании:")
    work_db.get_companies_and_vacancies_count()
    print()
    print("Получение списка всех вакансий с указанием названия компании,"
          "названия вакансии и зарплаты и ссылки на вакансию:")
    work_db.get_all_vacancies()
    print()
    print("Получение среднюю зарплату по вакансиям:")
    work_db.get_avg_salary()
    print()
    print("Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям:")
    work_db.get_vacancies_with_higher_salary()
    print()
    print("Получение списка всех вакансий, в названии которых содержатся переданные в метод слова:")
    work_db.get_vacancies_with_keyword()


def create_table():

    with open('/home/aliaksandr_sigai/course_work_4/course_work_5/functions/sql_manual', 'r') as file:
        open_file = file.read()
        conn = psycopg2.connect(
            host="localhost",
            database="vacancies",
            user="aliaksandr",
            password='12345'
        )
        with conn:
            with conn.cursor() as cur:
                cur.execute(open_file)


def main():
    """
    Функция с основным скриптом

    """
    print("Здравствуйте, перед началом работы создайте базу данных по примеру("
          "Создание новой БД: CREATE DATABASE vacancies)")
    print("Создание таблиц  в БД vacancies: ")
    create_table()
    print("Добавление данных в БД vacancies: ")
    add_info_to_db()
    print("Получение данных из БД vacancies: ")
    work_with_db()
