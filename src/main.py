import csv
import re
from datetime import datetime as dt
import time as tm

if __name__ == '__main__':

    talk_data = {}
    
    with open('./input/talk.txt', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter='\t')

        talk_data['data_title'] = next(reader)[0] 
        saved_date = re.match(r'[0-9]{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])', next(reader)[0][5:])
        if saved_date:
            talk_data['saved_datetime'] = dt.strptime(saved_date.group(), '%Y/%m/%d')
        else:
            print('parse Error')
            talk_data['saved_datetime'] = ''

        talk_data['talk_list'] = []
        current_datetime = dt.now()
        
        for row in reader:
            if len(row) == 0:
                # 空行 日付ごとに1行
                continue
            elif re.match(r'[0-9]{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])(.)', row[0]):
                # 日付行
                current_date = dt.strptime(re.match(r'[0-9]{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])', row[0]).group(), '%Y/%m/%d')
                # print(row[0])
            elif re.match(r'\d\d:\d\d', row[0]) and len(row) == 3:
                # 発言行
                current_datetime = dt(
                    current_date.year
                    , current_date.month
                    , current_date.day
                    , hour=int(row[0][0:2])
                    , minute=int(row[0][3:5])
                )
                talk_data['talk_list'].append([current_datetime, row[1], row[2]])
                # print(row)   
        print(talk_data['data_title'])
        print(talk_data['talk_list'])