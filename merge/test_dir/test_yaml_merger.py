from pathlib import Path
import sys
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir+"/merger_pkg")
from yaml_merger import get_data
import pytest

@pytest.fixture
def cases_simple_yaml():
    # [key,value]
    keys_values=[
        ["simple_yaml_1",42],
        ["simple_yaml_2",'hello'],  
        ["simple_yaml_3",{"simple_yaml_3_1":'hello2',"simple_yaml_3_2":'ccccc'}],
        ["simple_yaml_5","eeees"]]
    # print (keys_values)
    return keys_values

@pytest.fixture
def cases_simple_yaml1():
    keys_values = [
        ["simple_yaml_3_1","hello2"],
        ["simple_yaml_3_2","ccccc"],
        ["simple_yaml_4_1",{
        "include": 
            {"output_1":['output_1_data_1','output_1_data_2','output_1_data_3','output_1_data_4','output_1_data_5']},
        "include1": {
            "simple_yaml1_1":["simple_yaml1_1_data1","simple_yaml1_1_data2","simple_yaml1_1_data3","simple_yaml1_1_data4","simple_yaml1_1_data5"],
        "simple_yaml1_2":"simple_yaml1_2_data1"}
        }],
    ]
    return keys_values

@pytest.fixture
def cases_output_yaml():
    keys_values = [
        ["include",{"output_1":
            ['output_1_data_1','output_1_data_2','output_1_data_3','output_1_data_4','output_1_data_5']
                }
        ],
        ["include1", {
            "simple_yaml1_1":["simple_yaml1_1_data1","simple_yaml1_1_data2","simple_yaml1_1_data3","simple_yaml1_1_data4","simple_yaml1_1_data5"],
        "simple_yaml1_2":"simple_yaml1_2_data1"
        }]
    ]
    return keys_values

    return keys_values
def test_simple_yaml_data(cases_simple_yaml):
    for l in cases_simple_yaml:
        assert get_data(l[0]) == l[1]

def test_simple_yaml1_data(cases_simple_yaml1):
    for l in cases_simple_yaml1:
        prev_key = "simple_yaml_" + l[0][-3]
        prev_val = get_data(prev_key)
        assert prev_val[l[0]] == l[1]    

def test_output_yaml_data(cases_output_yaml):
    for l in cases_output_yaml:
        prev_val = get_data("simple_yaml_4")["simple_yaml_4_1"]
        assert prev_val[l[0]] == l[1]