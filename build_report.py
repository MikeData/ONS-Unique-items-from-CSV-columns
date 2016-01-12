# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:37:19 2016

@author: Mike
"""

import pandas as pd
import csv
import sys

dim_list = [
            "observation",
            "measure_type_eng",
            "unit_multiplier",
            "unit_of_measure_eng",
            "geographic_area",
            "time_dim_item_id",
            "time_dim_item_label_eng",
            "time_type",
            "statistical_population_id",
            "statistical_population_label_eng",
            "dim_id_1",
            "dimension_label_eng_1",
            "dim_item_id_1",
            "dimension_item_label_eng_1",
            "is_total_1",
            "is_sub_total_1",
            "dim_id_2",
            "dimension_label_eng_2",
            "dim_item_id_2",
            "dimension_item_label_eng_2",
            "is_total_2",
            "is_sub_total_2",
            ]

def scan_dims(dim, load_file):
    with open('report-' + load_file, 'ab') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=',')
    
        obs_file= pd.read_csv(load_file, dtype=object, usecols=dim)
        uniques = pd.Series(obs_file[:-1].values.ravel()).unique()
        uniques = uniques.tolist()
        uniques.append('<EOF>')
        uniques.insert(0, dim)
        unqiues = pd.Series(uniques)
        mywriter.writerow(unqiues)      
    csvfile.close()

def loop(loop_file):
    for dim in dim_list:
        scan_dims([dim], load_file)


load_file = sys.argv[1]
loop(load_file)

