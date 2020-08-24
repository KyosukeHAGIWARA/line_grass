import csv
import re

if __name__ == '__main__':
    
    with open('./input/talk.txt', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter='\t')
        data_title = next(reader)[0] 
        saved_datetime = next(reader)[0] 
        for row in reader:
            if len(row) == 0:
                # 空行 日付ごとに1行
                continue
            elif re.match(r'\d\d\d\d/\d\d/\d\d(.)', row[0]):
                # 日付行
                print(row[0])
            elif re.match(r'\d\d:\d\d', row[0]):
                # 発言行
                continue
            # print(row)   

        print(data_title)
        print(saved_datetime)