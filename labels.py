# create dictionary

import os

# data_dir='/home/ajit/Desktop/master_project/YOLO_format_data/Images/'
# # print(os.listdir(data_dir))
# classes = os.listdir(data_dir)
# # list_to_remove = ['00000', '00001', '00002', '00003','00004','00005']
# # final_list = list(set(classes) - set(list_to_remove))
# # final_list.sort()
# # print(final_list)
# source_path = [f'/home/ajit/Desktop/master_project/YOLO_format_data/Images/{a}' for a in classes]
# source_path_textfiles = [f'/home/ajit/Desktop/master_project/YOLO_format_data/Textfiles/{a}' for a in classes]
# # print(source_path)
# # print(source_path_textfiles)

# global i 
# i = 0
# for s in source_path_textfiles:
#     i += len(os.listdir(s))
#     # print (len(os.listdir(s)))

# print(i)

label_map = {
    '0': '20_speed',
    '1': '30_speed',
    '2': '50_speed',
    '3': '60_speed',
    '4': '70_speed',
    '5': '80_speed',
    '6': '80_lifted',
    '7': '100_speed',
    '8': '120_speed',
    '9': 'no_overtaking_general',
    '10': 'no_overtaking_trucks',
    '11': 'right_of_way_crossing',
    '12': 'right_of_way_general',
    '13': 'give_way',
    '14': 'stop',
    '15': 'no_way_general',
    '16': 'no_way_trucks',
    '17': 'no_way_one_way',
    '18': 'attention_general',
    '19': 'attention_left_turn',
    '20': 'attention_right_turn',
    '21': 'attention_curvy',
    '22': 'attention_bumpers',
    '23': 'attention_slippery',
    '24': 'attention_bottleneck',
    '25': 'attention_construction',
    '26': 'attention_traffic_light',
    '27': 'attention_pedestrian',
    '28': 'attention_children',
    '29': 'attention_bikes',
    '30': 'attention_snowflake',
    '31': 'attention_deer',
    '32': 'lifted_general',
    '33': 'turn_right',
    '34': 'turn_left',
    '35': 'turn_straight',
    '36': 'turn_straight_right',
    '37': 'turn_straight_left',
    '38': 'turn_right_down',
    '39': 'turn_left_down',
    '40': 'turn_circle',
    '41': 'lifted_no_overtaking_general',
    '42': 'lifted_no_overtaking_trucks'
}

print(label_map.values())


