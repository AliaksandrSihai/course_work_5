from classes.abstract_class import GetInfo


class GetCompaniesInfo(GetInfo):
    """
    Реализация класса для получения информации о компании
    """

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
        info = self.get_company_info(company_id)
        return info

    def get_info_vk(self):
        """
        Получение информации вк
        """
        company_id = self.id_list['vk']
        info = self.get_company_info(company_id)
        return info

    def get_info_al(self):
        """
        Получение информации альфа
        """
        company_id = self.id_list['alfa']
        info = self.get_company_info(company_id)
        return info

    def get_info_tk(self):
        """
        Получение информации тинькофф
        """
        company_id = self.id_list['tinkoff']
        info = self.get_company_info(company_id)
        return info

    def get_info_gz(self):
        """
        Получение информации газпром
        """
        company_id = self.id_list['gaz_prom']
        info = self.get_company_info(company_id)
        return info

    def get_info_vt(self):
        """
        Получение информации втб
        """
        company_id = self.id_list['vtb']
        info = self.get_company_info(company_id)
        return info

    def get_info_sr(self):
        """
        Получение информации сибур
        """
        company_id = self.id_list['sibur']
        info = self.get_company_info(company_id)
        return info

    def get_info_tl(self):
        """
        Получение информации теле_2
        """
        company_id = self.id_list['tele_2']
        info = self.get_company_info(company_id)
        return info

    def get_info_mt(self):
        """
        Получение информации мтс
        """
        company_id = self.id_list['mts']
        info = self.get_company_info(company_id)
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
