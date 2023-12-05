import logging
import traceback

'''
logging.DEBUG - Подробная информация, обычно представляющая интерес только 
                для разработчика, пытающегося диагностировать проблему.
traceback.format_exc() - вывод консольной ошибки 
'''


def loging(name_file_log='mylog.log', message=traceback.format_exc()):
    """
    Запись лога
    :param name_file_log: имя файла куда записывать лог
    :param message: текст который нужно записать traceback.format_exc() по умолчанию выдаёёт ошибку консоли
    """
    FORMAT = '%(asctime)s | %(module)s | %(levelname)s | %(funcName)s: %(lineno)s | %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        filename=f'file/logs/{name_file_log}',
                        format=FORMAT,
                        datefmt="%Y-%m-%d %H:%M:%S"
                        )
    d = {'message': message}
    logging.warning(d)
