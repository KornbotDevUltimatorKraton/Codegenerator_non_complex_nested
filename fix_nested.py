import os 
import sys
import re  
from publish_subscriber_class import Create_node_pub,Create_node_sub # Getting the node pub and sub 
import time 
sequence_complex = {'parameter_1':{'p1':2,'p2':4,'p3':0,'if_2':{'p1':"!=p2",'command':"print('Not equally')",'if_3':{"p1+p2":"=6",'for_1':{'v_1':[0,'len(data1)'],'if_4':{'p2-p1':'=2','display':'print("data_output ",p2-p1)'}}}}},'compute_1':{'p3':'math.pow(p1,p2)'}} # Getting the complex data analysis 

def validations(sequence_complex):
       print(sequence_complex.items())

validations(sequence_complex)

def extract_sequence(): 
          
         for r in list(sequence_complex):  
                  print(r)
extract_sequence()
def loop_ex_check(input_dict): 
      key_list = list(input_dict.keys()) 
      value_list = list(input_dict.values()) 
      position  = key_list.index(input_dict)
      print(key_list)
      print(value_list)
      return key_list,value_list

#def getting_position_index():
     
      

ref_mem = {} # Getting the ref_mem of each recent parameter with dict in the list value data with the current key 
series_adder = {} # Getting the series of the parameter input
mem_dict = []
mem_array_keys  = [] 
mem_array_main = []
for r in list(sequence_complex):
      mem_array_main.append([]) 


for r in range(0,len(list(sequence_complex))):
            if mem_array_main[r] == []:
                    if  str(type(sequence_complex.get(list(sequence_complex)[r]))).split(" ")[1].split(">")[0] == "'dict'": 
                           if mem_array_main[r] ==[]:
                                   mem_array_main[r].append(sequence_complex.get(list(sequence_complex)[r]))
                           if mem_array_main[r] != []: 
                                  if mem_array_main[r][len(mem_array_main[r])-1] != sequence_complex.get(list(sequence_complex)[r]):
                                                 mem_array_main[r].append(sequence_complex.get(list(sequence_complex)[r]))
                                                 mem_array_keys.append([])
     
            if mem_array_main[r] !=[]:
                    for rt in list(mem_array_main[r][len(mem_array_main[r])-1]):
                            if mem_array_main[r][len(mem_array_main[r])-1]:
                                if  str(type(sequence_complex.get(list(sequence_complex)[r]))).split(" ")[1].split(">")[0] == "'dict'": 
                                             #print("Now get inside the nested")
                                             if mem_array_main[r][len(mem_array_main[r])-1] != mem_array_main[r][len(mem_array_main[r])-1].get(rt):
                                                       mem_array_main.append(mem_array_main[r][len(mem_array_main[r])-1].get(rt))       
                                                       mem_array_keys.append([])
                                                       mem_array_keys[len(mem_array_keys)-1].append(str(rt))
            #time.sleep(2)
            
            print(mem_array_main)                                                    
            print(mem_array_keys)
            # Nest is running the mem loop of the mem_array_keys to detect the dictionnary inside the nested loop to convert into the single list json dictionary 
            
            