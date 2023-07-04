from openpyxl import Workbook


class ExcelManager:

    def save_to_file(self, v_list):
        with open('table_file.xlsx', 'w', encoding='utf-8') as file:
            wb = Workbook()
            ws = wb.active

            ws.append([
                'vacancy_name', 'vacancy_url', 'salary_min',
                'salary_max', 'requirements'
            ])

            for vacancy in v_list:
                ws.append([
                    vacancy['title'], vacancy['url'], vacancy['salary_min'],
                    vacancy['salary_max'], vacancy['requirements']
                ])
            wb.save('table_file.xlsx')
            wb.close()
