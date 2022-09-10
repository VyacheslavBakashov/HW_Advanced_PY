import csv
import datetime as dt
import os


def log_decor(path):

    def log_decor_(old_func):
        header = ['date', 'time', 'name_func', 'arguments']
        log_file_name = 'logger.csv'

        def new_func(*args, **kwargs):
            result = old_func(*args, **kwargs)
            date, time = dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S').split()
            name_func = f'{old_func.__name__}'
            arguments = f'{args} {kwargs}'
            log_dict = dict(zip(header, [date, time, name_func, arguments]))
            with open(os.path.join(path, log_file_name), 'a+', encoding='utf-8', newline='') as log_file:
                writer = csv.DictWriter(log_file, fieldnames=header)
                log_file.seek(0)
                if not log_file.readline():
                    writer.writeheader()
                writer.writerow(log_dict)
            return result

        return new_func

    return log_decor_
