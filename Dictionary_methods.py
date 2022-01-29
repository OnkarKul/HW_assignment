import logging
import copy

logging.basicConfig(filename="log.log", level=logging.INFO, format= '%(asctime)s %(levelname)s %(message)s')





def dir_get_keys(dir1):
    logging.info('Dictionary get keys start')
    try:
        if type(dir1) == dict:
            get_key=dir1.keys()
            logging.info('Dir  is %s and values are %s', dir1, get_key)

        else:
            raise Exception("Sorry, you suppose to pass dir")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        return get_key
    finally:
        logging.info('Dictionary get keys end')

def dir_get_values(dir1):
    logging.info('Dictionary get values start')
    try:
        if type(dir1) == dict:
            get_values=dir1.values()
            logging.info('Dir  is %s and values are %s', dir1, get_values)

        else:
            raise Exception("Sorry, you suppose to pass dir")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        return get_values
    finally:
        logging.info('Dictionary get values end')

def dir_get_specific_item(dir1):
    logging.info('Dictionary get item start')
    try:
        if type(dir1) == dict:
            get_key=eval(input('Enter key to get its value :'))
            x = dir1.get(get_key)
            logging.info('For key =%s values is %s', get_key, x)

        else:
            raise Exception("Sorry, you suppose to pass dir")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        return x
    finally:
        logging.info('Dictionary get item end')

def dir_pop_item(dir1):
    logging.info('Dictionary pop item start')
    try:
        if type(dir1) == dict:
            get_key=eval(input('Enter key which want to remove :'))
            logging.info('dir is %s and remove key is %s', dir1, get_key)
            x = dir1.pop(get_key)

        else:
            raise Exception("Sorry, you suppose to pass dir")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('Final dir is  %s', dir1)
        return dir1
    finally:
        logging.info('Dictionary pop item end')


def dir_update(dir1):
    logging.info('Dictionary update start')
    try:
        if type(dir1) == dict:
            get_key=eval(input('Enter key :'))
            get_value = eval(input('Enter value :'))
            logging.info('dir is %s and new key and value is {%s :%s}', dir1,get_key, get_value)
            x = dir1.update({get_key:get_value})

        else:
            raise Exception("Sorry, you suppose to pass dir")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('Final dir is  %s', dir1)
        return dir1
    finally:
        logging.info('Dictionary update end')