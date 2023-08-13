
from classes.abstract_class import Get_Info


class GetVacanciesInfo(Get_Info):
    """
    Реализация класса для получения информации о вакансиях
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

    def get_info_yd(self):
        """
        Вакансии яндекса
        """
        company_id = self.id_list['yandex']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_sb(self):
        """
        Вакансии сбера
        """
        company_id = self.id_list['sber']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_vk(self):
        """
        Вакансии вк
        """
        company_id = self.id_list['vk']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_al(self):
        """
        Вакансии альфы
        """
        company_id = self.id_list['alfa']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_tk(self):
        """
        Вакансии тинькофф
        """
        company_id = self.id_list['tinkoff']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_gz(self):
        """
        Вакансии газпрома
        """
        company_id = self.id_list['gaz_prom']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_vt(self):
        """
        Вакансии втб
        """
        company_id = self.id_list['vtb']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_sr(self):
        """
        Вакансии сибур
        """
        company_id = self.id_list['sibur']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_tl(self):
        """
        Вакансии теле_2
        """
        company_id = self.id_list['tele_2']
        info = self.get_vacancies_info(company_id)
        return info

    def get_info_mt(self):
        """
        Вакансии мтс
        """
        company_id = self.id_list['mts']
        info = self.get_vacancies_info(company_id)
        return info

    def amount_info(self):
        """
        Метод для сбора общей информации о вакансиях
        """
        yd = self.get_info_yd()
        sb = self.get_info_sb()
        vk = self.get_info_vk()
        al = self.get_info_al()
        tk = self.get_info_tk()
        gz = self.get_info_gz()
        vt = self.get_info_vt()
        sr = self.get_info_sr()
        tl = self.get_info_tl()
        mt = self.get_info_mt()
        amount = yd, sb, vk, al, tk, gz, vt, sr, tl, mt
        return amount
