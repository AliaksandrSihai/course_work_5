import psycopg2

from classes.get_company_info import  Get_Companies_Info
from classes.get_vacancy_info import Get_Vacancies_Info

if __name__ == "__main__":
    ff = Get_Companies_Info()
    dd = Get_Vacancies_Info()


    #print(ff.get_info_yd())
    print(dd.get_info_yd())
    #print(dd.amount_info())
    #print(get_vacancies())
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="vacancies",
    #     user="aliaksandr",
    #     password='12345'
    # )
    # with conn:
    #     with conn.cursor() as cur:
    #         cur.execute("CREATE TABLE companies ")
    #         ds = cur.fetchall()
    #         print(ds)

