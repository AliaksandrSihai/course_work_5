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
        Получает список всех компаний и количество вакансий у каждой компании
        """

        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT company_name,COUNT(*) "
                            "FROM companies "
                            "JOIN vacancies USING(company_id) "
                            "GROUP BY company_name "
                            "ORDER BY COUNT(*) DESC")

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT company_name, vacancy_name, vacancy_salary, vacancy_url "
                            "FROM vacancies "
                            "JOIN result USING(vacancy_id) "
                            "JOIN companies USING(company_id) "
                            "GROUP BY company_name "
                            "ORDER BY company_name")

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT vacancy_name, AVG(vacancy_salary) "
                            "FROM vacancies "
                            "GROUP BY vacancy_name "
                            "ORDER BY AVG(vacancy_salary)")

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * "
                            "FROM vacancies "
                            "WHERE vacancy_salary > (SELECT AVG(vacancy_salary) FROM vacancies) "
                            "ORDER BY vacancy_salary ")

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например python
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * "
                            "FROM vacancies "
                            f"WHERE vacancy_name LIKE '%{keyword}%' "
                            "ORDER BY vacancy_salary ")
