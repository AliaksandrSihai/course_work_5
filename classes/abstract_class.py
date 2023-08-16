from datetime import datetime

import requests


class GetInfo:
    """
    Класс для получения информации через API
    """

    id_list = {
        'yandex': 1740,
        'sber': 3529,
        'vk': 15478,
        'alfa': 80,
        'tinkoff': 78638,
        'gaz_prom': 39305,
        'vtb': 4181,
        'sibur': 3809,
        'tele_2': 4219,
        'mts': 3776
    }

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
        info_to_db = []
        page = 1
        while page < 19:
            page += 1
            params = {
                "per_page": 100,
                "page": page
            }

            response = requests.get(url, params=params)
            vacancies_raw_data = response.json()
            vacancies = vacancies_raw_data['items']
            for vacancy in vacancies:
                salary = vacancy['salary']
                salary_range = salary['from'] if salary and salary[
                    'from'] else 0
                date = vacancy['published_at']
                date_str = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
                publish_time = date_str.strftime('%Y-%m-%d')
                info_to_column = {'vacancy_id': vacancy['id'],
                                  'vacancy_name': vacancy['name'],
                                  'vacancy_url': vacancy['url'],
                                  'vacancy_area': vacancy['area']['name'],
                                  'vacancy_requirement': vacancy['snippet']['requirement'],
                                  'vacancy_responsibility': vacancy['snippet']['responsibility'],
                                  'vacancy_salary': salary_range,
                                  'vacancy_published_date': publish_time,
                                  'company_id': vacancy['employer']['id']
                                  }
                info_to_db.append(info_to_column)
        return info_to_db
