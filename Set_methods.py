import logging
import copy

logging.basicConfig(filename="log.log", level=logging.INFO, format= '%(asctime)s %(levelname)s %(message)s')


def set_add_element(set1):
    logging.info('set adding value start')
    try:
        if type(set1)==set:
            index = int(input('Enter value you want to add value :'))
            logging.info('set %s and value is %s', set1 , index)
            my_set_old = copy.deepcopy(set1)
            set1.add(index)
        else:
            raise Exception("Sorry, you suppose to pass set")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('your old set %s and after inserting your set is %s', my_set_old, set1)
        return set1
    finally:
        logging.info('list adding end')

def set_difference(set1,set2):
    logging.info('set difference start')
    try:
        if type(set1) == set and type(set2)==set:
            logging.info('sets are %s %s', set1, set2)
            updated_set1 = set1.difference(set2)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('set difference is %s', updated_set1)
        return updated_set1
    finally:
        logging.info('set difference end')
def set_difference_update(set1,set2):
    logging.info('set difference update start')
    try:
        if type(set1) == set and type(set2) == set:
            logging.info('sets are %s %s', set1, set2)
            set1.difference_update(set2)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('set difference updated is %s', set1)
        return set1
    finally:
        logging.info('set difference update end')

def set_intersection(set1,set2):
    logging.info('set intersection start')
    try:
        if type(set1) == set and type(set2) == set:
            logging.info('sets are %s %s', set1, set2)
            updated_set = set1.intersection(set2)

        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:
        logging.info('set intersection of sets is %s', updated_set)
        return updated_set
    finally:
        logging.info('set intersection end')

def set_intersection_update(set1,set2):
    logging.info('set intersection update start')
    try:
        if type(set1) == set and type(set2) == set:
            logging.info('sets are %s %s', set1, set2)
            set1.intersection_update(set2)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('set intersection updated is %s', set1)
        return set1
    finally:
        logging.info('set intersection update end')

def set_symmetric_difference(set1,set2):
    logging.info('set symmetric_difference start')
    try:
        if type(set1) == set and type(set2) == set:
            logging.info('sets are %s %s', set1, set2)
            symmetric_set = set1.symmetric_difference(set2)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('set symmetric difference is %s', symmetric_set)
        return symmetric_set
    finally:
        logging.info('set symmetric_difference end')
def set_symmetric_difference_update(set1,set2):
    logging.info('set symmetric_difference_update start')
    try:
        if type(set1) == set and type(set2) == set:
            logging.info('sets are %s %s', set1, set2)
            set1.symmetric_difference_update(set2)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('set intersection updated is %s', set1)
        return set1
    finally:
        logging.info('set symmetric_difference_update end')

def set_discard(set1):
    logging.info('set discard start')
    try:
        if type(set1) == set:

            set_val=eval(input('Enter value which you want to discard from set :'))
            logging.info('set is %s and value is %s', set1,set_val)
            set1.discard(set_val)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('your final set is %s after discarding %s', set1, set_val)
        return set1
    finally:
        logging.info('set discard end')


def set_remove(set1):
    logging.info('set remove start')
    try:
        if type(set1) == set:

            set_val = eval(input('Enter value which you want to remove from set :'))
            logging.info('set is %s and value is %s', set1, set_val)
            set1.remove(set_val)
        else:
            raise Exception("Sorry, you suppose to pass sets")
    except Exception as err:
        logging.error('Exception occurred')
        logging.exception(err)
    else:

        logging.info('your final set is %s after removing %s', set1, set_val)
        return set1
    finally:
        logging.info('set remove end')
