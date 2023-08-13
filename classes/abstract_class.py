from datetime import datetime

import requests


class Get_Info:
    """
    Класс для получения информации через API
    """

    @classmethod
    def get_company_info(cls, company_id):
        """
        Метод для получения информации о компании
        """

        url = f'https://api.hh.ru/employers/{company_id}'
        response = requests.get(url)
        vacancies = response.json()
        info_to_column = [{
            'company_id': vacancies['id'],
            'company_name': vacancies['name'],
            'company_url': vacancies['site_url'],
            'company_area': vacancies['area']['name'],
            'company_industries': vacancies['industries'][0]['name'],
            'quantity_open_vacancies': vacancies['open_vacancies']

        }]
        return info_to_column

    @classmethod
    def get_vacancies_info(cls, company_id):
        """
        Метод для получения информации об открытых вакансиях компании по её id
        """

        url = f'https://api.hh.ru/vacancies?employer_id={company_id}'
        params = {
            "per_page": 100
        }
        response = requests.get(url, params=params)
        vacancies = response.json()
        info = vacancies['items']
        info_to_db = []
        for x in info:
            salary = x['salary']
            salary_range = salary['from'] if salary and salary[
                'from'] else 0
            date = x['published_at']
            date_str = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
            publish_time = date_str.strftime('%Y-%m-%d')
            info_to_column = {'vacancy_id': x['id'],
                              'vacancy_name': x['name'],
                              'vacancy_url': x['url'],
                              'vacancy_area': x['area']['name'],
                              'vacancy_requirement': x['snippet']['requirement'],
                              'vacancy_responsibility': x['snippet']['responsibility'],
                              'vacancy_salary': salary_range,
                              'vacancy_published_date': publish_time
                              }
            info_to_db.append(info_to_column)
        return info_to_db
