import psycopg2


class DBManager:
    """
    Класс для подключения к БД
    """
    conn = psycopg2.connect(
        host="localhost",
        database="vacancies",
        user="aliaksandr",
        password='12345'
    )

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество открытых вакансий у каждой компании
        """

        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT company_name, quantity_open_vacancies "
                            "FROM companies "
                            "GROUP BY company_name, quantity_open_vacancies "
                            "ORDER BY quantity_open_vacancies")
                result = cur.fetchall()
                print(result)
                return result

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT vacancy_name, vacancy_salary, vacancy_url, company_name "
                            "FROM vacancies "
                            "JOIN companies USING(company_id) "
                            "GROUP BY vacancy_name, vacancy_salary, vacancy_url, company_name "
                            "ORDER BY vacancy_salary")
                result = cur.fetchall()
                print(result)
                return result

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT vacancy_name, CAST(AVG(vacancy_salary) AS FLOAT) "
                            "FROM vacancies "
                            "GROUP BY vacancy_name "
                            "ORDER BY CAST(AVG(vacancy_salary) AS FLOAT)")
                result = cur.fetchall()
                print(result)
                return result

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * "
                            "FROM vacancies "
                            "WHERE vacancy_salary > (SELECT CAST(AVG(vacancy_salary) AS FLOAT)  FROM vacancies) "
                            "ORDER BY vacancy_salary ")
                result = cur.fetchall()
                print(result)
                return result

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например python
        """
        keyword = input("Введите слово ")
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * "
                            "FROM vacancies "
                            f"WHERE vacancy_name LIKE '%{keyword}%' OR vacancy_requirement LIKE '%{keyword}%' "
                            f"OR vacancy_responsibility LIKE '%{keyword}%' "
                            "ORDER BY vacancy_salary ")
                result = cur.fetchall()
                print(result)
                return result
