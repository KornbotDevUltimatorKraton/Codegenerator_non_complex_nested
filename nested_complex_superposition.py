import os 
import sys
import re  
from publish_subscriber_class import Create_node_pub,Create_node_sub # Getting the node pub and sub 
sequence_complex = {'parameter_1':{'p1':2,'p2':4,'p3':0,'if_2':{'p1':"!=p2",'command':"print('Not equally')",'if_3':{"p1+p2":"=6",'for_1':{'v_1':[0,'len(data1)'],'if_4':{'p2-p1':'=2','display':'print("data_output ",p2-p1)'}}}},'compute_1':{'p3':'math.pow(p1,p2)'}}} # Getting the complex data analysis 

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
      print(key_list)
      print(value_list)
      return key_list,value_list

#def getting_position_index():
     
      

ref_mem = {} # Getting the ref_mem of each recent parameter with dict in the list value data with the current key 
series_adder = {} # Getting the series of the parameter input
mem_dict = []
mem_array_keys  = [] 
mem_array_value = []
while True:
  for r in list(sequence_complex):
          
      if mem_dict == []: 
        
             print(sequence_complex.get(r),str(type(sequence_complex.get(r))).split(" ")[1].split(">")[0]) # Checking type and save the parameter in value and looping the extraction  
             if  str(type(sequence_complex.get(r))).split(" ")[1].split(">")[0] == "'dict'":  
                  key_list,value_list = loop_ex_check(sequence_complex.get(r))  
                  if mem_dict == []:          
                        mem_dict.append(sequence_complex.get(r))
                  if mem_dict != []:
                      if mem_dict[len(mem_dict)-1] != sequence_complex.get(r):
                              mem_dict.append(sequence_complex.get(r))
                              mem_array_keys.append([])
                              mem_array_keys[len(mem_array_keys)-1].append(str(rt))   
              
                  #print(mem_dict)
      if mem_dict !=[]:
                
                for rt in list(mem_dict[len(mem_dict)-1]): 
                           #print("Searching dict",rt,mem_dict[len(mem_dict)-1].get(rt))
                           if str(type(mem_dict[len(mem_dict)-1].get(rt))).split(" ")[1].split(">")[0] == "'dict'":
                                 #print("Found dict!")  
                                 if mem_dict[len(mem_dict)-1] != mem_dict[len(mem_dict)-1].get(rt):               
                                            mem_dict.append(mem_dict[len(mem_dict)-1].get(rt))
                                            mem_array_keys.append([])
                                            mem_array_keys[len(mem_array_keys)-1].append(str(rt))
                print("Complete dict",mem_dict)
      print("Referent_position: ",mem_array_keys)
