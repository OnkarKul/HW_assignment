import logging
import copy

logging.basicConfig(filename="log.log", level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

super_list=[]
def list_return():
    try:
        super_list.clear()
        my_list = eval(input('Please enter list object : '))
        if type(my_list)==list:
            logging.info('you pass correct list: %s',my_list)
            for i in my_list:
                super_list.append(i)
            return my_list
        else:
            logging.error('You need to pass list')
    except Exception as err:
        logging.exception(err)

def list_reverse():
    try:
        logging.info('list_reverse started')
        if super_list:
            logging.info('Your list: %s and reverse list : %s', super_list,super_list[::-1])
            return super_list[::-1]
        else:
            my_list = eval(input('Please enter list object : '))
            logging.info('Your list: %s and reverse list : %s', my_list,my_list[::-1])
            return my_list[::-1]
    except Exception as err:
        logging.exception(err)
    finally:
        logging.info('list_reverse end')

def list_append(my_list):
    try:
        logging.info('list_append started')
        arg=eval(input('Enter append value : '))
        my_listBK= copy.deepcopy(my_list)
    except Exception as err:
        logging.exception(err)
    else:
        my_list.append(arg)
        logging.info('Your old list is %s and updated list is %s', my_listBK, my_list)
        return my_list
    finally:
        logging.info('list_append end')

def List_sort(arg):
    logging.info('List sorting start')
    try:
        my_list_old = copy.deepcopy(arg)
        arg.sort()
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('your old list %s and sorted list is %s',my_list_old,arg)
        return arg
    finally:
        logging.info('list sorting end')


def List_insert(insert_list,insert_item):
    logging.info('List inserting start')
    try:
        index=int(input('Enter index where you want to insert value :'))
        logging.info('index= %s',index)
        my_list_old = copy.deepcopy(insert_list)
        insert_list.insert(index,insert_item)
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('your old list %s and after inserting your list is %s', my_list_old, insert_list)
        return insert_list
    finally:
        logging.info('list inserting end')

def List_extend(list1,list2):
    logging.info('List extent start')
    try:
        logging.info('Input list are %s and %s', list1, list2)
        my_list_old = copy.deepcopy(list1)
        list1.extend(list2)
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your old list are %s & %s and extended list is %s', my_list_old, list2, list1)
        return list1
    finally:
        logging.info('list extent end')


def List_count(list1):
    logging.info('List count start')
    try:
        if type(list1)==list:
            counter_var = eval(input('Enter count value '))
            logging.info('Input list are %s ', list1)
            count_var=list1.count(counter_var)
        else:
            raise  Exception ("Sorry, you suppose to pass list")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your list %s and value %s occurrences %s time in the list', list1, counter_var, count_var)
        return count_var
    finally:
        logging.info('list count end')

def List_index(list1):
    logging.info('List index start')
    try:
        if type(list1) == list:
            index_var = eval(input('Enter value which you want to find index : '))
            logging.info('Input list are %s and value is %s  ', list1 ,index_var )
            count_var = list1.index(index_var)
        else:
            raise Exception("Sorry, you suppose to pass list")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your list is %s and index of value %s  is %s ', list1, index_var, count_var)
        return count_var
    finally:
        logging.info('list index end')


def List_remove(list1):
    logging.info('List remove start')
    try:
        if type(list1) == list:
            my_list_old = copy.deepcopy(list1)
            remove_var = eval(input('Enter value which you want to remove : '))
            logging.info('Input list are %s and value is %s ', list1, remove_var)
            list1.remove(remove_var)
        else:
            raise Exception("Sorry, you suppose to pass list")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your list is %s and after removing %s  your list is  %s ', my_list_old, remove_var, list1)
        return list1
    finally:
        logging.info('list remove end')
def List_pop(list1):
    logging.info('List pop start')
    try:
        if type(list1) == list:
            my_list_old = copy.deepcopy(list1)
            pop_var = eval(input('Enter index which you want to remove : '))
            logging.info('Input list are %s and index is %s ', list1, pop_var)
            list1.pop(pop_var)
        else:
            raise Exception("Sorry, you suppose to pass list")

    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your list is %s and after removing %s th index list is %s ', my_list_old, pop_var, list1)
        return list1
    finally:
        logging.info('list pop end')