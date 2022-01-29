import logging
import copy

logging.basicConfig(filename="log.log", level=logging.INFO, format= '%(asctime)s %(levelname)s %(message)s')

def tuple_count(tuple1):
     logging.info('tuple count start')
     try:
         if type(tuple1) == tuple:
             counter_var = eval(input('Enter count value '))
             logging.info('Input tuple is %s and value is %s ', tuple1, counter_var)
             count_var = tuple1.count(counter_var)
         else:
             raise Exception("Sorry, you suppose to pass tuple")

     except Exception as err:
         logging.error('Exception occurred')
         logging.exception(err)
     else:
         logging.info('your tuple s %s and value %s occurrences %s time in the list', tuple1, counter_var, count_var)
         return count_var
     finally:
         logging.info('tuple count end')

def Tuple_index(tuple1):
    logging.info('tuple index start')
    try:
        if type(tuple1) == tuple:
            index_var = eval(input('Enter value which you want to find index : '))
            logging.info('Input tuple is %s and value is %s  ', tuple1 ,index_var )
            count_var = tuple1.index(index_var)
        else:
            raise Exception("Sorry, you suppose to pass tuple")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your tuple is %s and index of value %s  is %s ', tuple1, index_var, count_var)
        return count_var
    finally:
        logging.info('tuple index end')


def Tuple_size(tuple1):
    count=0
    logging.info('tuple count start')
    try:
        if type(tuple1) == tuple:
            logging.info('Input tuple is %s',tuple1 )
            for i in tuple1:
                count +=1
        else:
            raise Exception("Sorry, you suppose to pass tuple")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('size of tuple %s is %s ', tuple1, count)
        return count
    finally:
        logging.info('tuple count end')

