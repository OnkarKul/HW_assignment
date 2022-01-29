import Dictionary_methods
import Set_methods
import Tuple_methods
from List_methods import *
import List_methods

''' 
creating own functions at respective data type python module and trying to access these functions from this main.py file
problem statement:
create your own packages for list functions, tuple functions, set functions and dict functions
Also maintain logging and exception handling 
'''

################################ List Methods ##########################################

List_methods.list_return()
#List_methods.list_reverse()
append_list=[1, 2.2, 3+4j,'onkar']
#List_methods.list_append(append_list)

my_list=[9,8,7,6,5,4,3,2,1]
insert_list = my_list
insert_item= 123
#List_methods.List_sort(my_list)
#List_methods.List_insert(insert_list,insert_item)
#List_methods.List_extend([1,2,3],{4,5,6})
#List_methods.List_count(my_list)
#List_methods.List_index(my_list)
#List_methods.List_remove(my_list)
#List_methods.List_pop(my_list)


################################ tuple Methods ##########################################
my_tuple=(1,2,3,4,4,5,666,6,6,6,)
#Tuple_methods.tuple_count(my_tuple)
#Tuple_methods.Tuple_index(my_tuple)
#Tuple_methods.Tuple_size(my_tuple)


################################ set Methods ##########################################
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
#Set_methods.set_add_element(set1)
#Set_methods.set_difference(set1,set2)
#Set_methods.set_difference_update(set1,set2)
#Set_methods.set_intersection(set1,set2)
#Set_methods.set_intersection_update(set1,set2)
#Set_methods.set_symmetric_difference(set1,set2)
#Set_methods.set_symmetric_difference_update({1,2,3,4,5,6},{4,5,6,7,8,9})
#Set_methods.set_discard({1,2,3,4,5,6,7})
#Set_methods.set_remove({12,22,33,44,55,66})


################################ Dict Methods ##########################################
dir1={'name':'onkar', 'surname':'kulkarni', 'mailID':'abc@gmail.com', 'age':25}
#Dictionary_methods.dir_get_keys(dir1)
#Dictionary_methods.dir_get_values(dir1)
#Dictionary_methods.dir_get_specific_item(dir1)
#Dictionary_methods.dir_pop_item(dir1)
#Dictionary_methods.dir_update(dir1)