from task2 import List
import pytest
import numpy as np

def test_initialization():
    number_list = List()
    number_list.initialize_from_database()
    assert (len(number_list.numbers) != 0)

def test_adding():
    number_list = List()
    number_list.add_number("380123456789")
    assert number_list.numbers[0] == "380123456789"

def test_find_numbers():
    number_list = List()
    number_list.add_number("380671234569")
    number_list.add_number("380681234569")
    number_list.add_number("380981234569")
        
    number_list.find_numbers("38098")
    assert number_list.found_numbers[0] == "380981234569"

    
    
     
