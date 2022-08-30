import csv
import re


def fix_names(data_list, header):
    if not all(data_list):
        temp = ' '.join(data_list[:3]).split()
        if len(temp) < 3:
            temp.append('')
        data_list[:3] = temp
    return dict(zip(header, data_list))


def fix_list(data_list):
    name_keys = ("lastname", "firstname")
    temp_dict = {}
    for row in data_list:
        name = f'{row.pop(name_keys[0])} {row.pop(name_keys[1])}'
        temp_dict.setdefault(name, row).update({k: row[k] for k in row if row[k]})
    return [{**dict(zip(name_keys, k.split())), **v} for k, v in temp_dict.items()]


if __name__ == '__main__':
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})' \
              r'[-\s]*(\d{2})[-\s]*(\d{2})\s*\(?(\w{3}\.)?\s*(\d{4})?\)?'
    template = r'+7(\2)\3-\4-\5 \6\7'

    with open('phonebook_raw.csv', encoding='utf-8') as file_in:
        headers = file_in.readline().strip().split(',')
        raw_data = list(csv.reader(file_in))
        data_upd = fix_list(map(fix_names, raw_data, [headers]*len(raw_data)))

    for data in data_upd:
        data['phone'] = re.sub(pattern, template, data['phone']).strip()

    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as file_out:
        writer = csv.DictWriter(file_out, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_upd)
