import os, csv
class Setting:
    def __init__(self):
       self.token = None
       self.domain = None
       self._setting_file_path = os.path.join(os.getcwd(), 'setting.tsv')
    def get(self):
        with open(self._setting_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)
            return [row for row in reader]

