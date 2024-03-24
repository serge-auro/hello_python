import re
import csv
import codecs
from datetime import datetime

month_map = {
    'янв': '01',
    'фев': '02',
    'мар': '03',
    'апр': '04',
    'май': '05',
    'июн': '06',
    'июл': '07',
    'авг': '08',
    'сен': '09',
    'окт': '10',
    'ноя': '11',
    'дек': '12',
    #float
    ',0': '0',
    ',1': '1',
    ',2': '2',
    ',3': '3',
    ',4': '4',
    ',5': '5',
    ',6': '6',
    ',7': '7',
    ',8': '8',
    ',9': '9',
}

input_file = "C:/Users/SergeyIvanov/Documents/_csk/KLAD/test.csv" #--!!
output_file = "C:/Users/SergeyIvanov/Documents/_csk/KLAD/output.csv"

with codecs.open(input_file, 'r', encoding='utf-8', errors='replace') as f_in, \
     codecs.open(output_file, 'w', encoding='utf-8') as f_out:
    reader = csv.reader(f_in, delimiter=';')
    writer = csv.writer(f_out, quoting=csv.QUOTE_MINIMAL, escapechar='\\', delimiter=';')
    for row in reader:
        new_row = []
        for item in row:
            # Сначала выполняем замену по словарю
            for key, value in month_map.items():
                item = item.replace(key, value)
            # Затем обрабатываем даты
            date_match = re.search(r'\b(\d{1,2}.\d{1,2}.\d{4} \d{1,2}:\d{2})\b', item)
            if date_match:
                date_str = date_match.group(1)
                new_date = datetime.strptime(date_str, '%d.%m.%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
                item = re.sub(r'\b(\d{1,2}.\d{1,2}.\d{4} \d{1,2}:\d{2})\b', new_date, item)
            new_row.append(item)
        writer.writerow(new_row)

print(f"Output file saved to: {output_file}")