from classes.abstract_class import Get_Info


class Get_Companies_Info(Get_Info):
    """
    Реализация класса для полчения информации о компании
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
        Получение информации яндекс
        """
        company_id = self.id_list['yandex']
        info = self.get_company_info(company_id)
        return info

    def get_info_sb(self):
        """
        Получение информации сбер
        """
        company_id = self.id_list['sber']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_vk(self):
        """
        Получение информации вк
        """
        company_id = self.id_list['vk']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_al(self):
        """
        Получение информации альфа
        """
        company_id = self.id_list['alfa']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_tk(self):
        """
        Получение информации тинькофф
        """
        company_id = self.id_list['tinkoff']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_gz(self):
        """
        Получение информации газпром
        """
        company_id = self.id_list['gaz_prom']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_vt(self):
        """
        Получение информации втб
        """
        company_id = self.id_list['vtb']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_sr(self):
        """
        Получение информации сибур
        """
        company_id = self.id_list['sibur']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_tl(self):
        """
        Получение информации теле 2
        """
        company_id = self.id_list['tele_2']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info
    def get_info_mt(self):
        """
        Получение информации мтс
        """
        company_id = self.id_list['mts']
        yd = Get_Info()
        info = yd.get_company_info(company_id)
        return info

    def amount_info(self):
        """
        Метод для сбора общей информации о всех компаниях
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


