from csv import excel_tab
import os
from posixpath import lexists 
import sys
import json 
import subprocess # Getting the subprocess to running the local function 
import threading # Multi threading library from the multi core parallel programming 
import requests # Getting the request rest api function 
from itertools import count
from publish_subscriber_class import Create_node_pub,Create_node_sub 

sequence_condition = {'parameters_1':{'p1':2,'p2':4},'if_1':{"p1+p2":"==6"},"for_1_nested":{"v_1":[0,3]},"command_1_nested":{"display":"print('Good bye and go!')"},"for_2_nested":{'v_2':[0,2]},"command_3_nested":{"display":"print('Hey do something !')"},'if_2_nested':{"p1+p2":"!=4"},"command_4_nested":{"display":"print('Oh, god!')"},'parameters_2_nested':{'p3':5,'p4':6}}
tab_backend_ref = [] #Getting the reference for tapping and enter down count to adding the number of parameter
tab_count = [] # Getting the tab count data in here to calculate the tab number on each state of condition automatically

count_nested = 0 
list_condition = ['if','elseif','for','while']
def checking_before_code(value_input):

                  
                   key_sequence = list(sequence_condition.keys()) 
                   value_sequence = list(sequence_condition.values()) 
                   position = key_sequence.index(value_input)
                   try:
                      print(position-1)
                      print("Before condition statement:",key_sequence[position-1].split("_")[0],"Current statement:",value_input.split("_")[0])
                      return key_sequence[position-1].split("_")[0] # Getting the key value statement before the current statement
                   except:
                       print("Out of range")
def Sequence_loader():
    for r in list(sequence_condition): 
         try:
           if r.split("_")[0] == 'parameters': 
                
                 for t in list(sequence_condition.get(r)):
                    try: 
                      if len(r.split("_"))  == 2: 
                          data_condition = "\n"+len(tab_count)*"\t"+"global "+str(t)+";"+str(t)+" = "+str(sequence_condition.get(r).get(t))
                          tab_backend_ref.append(data_condition)
                    except:
                        pass 
                    
                    try:
                       if r.split("_")[2] == 'nested':
                          
                              data_condition = "\n"+len(tab_count)*"\t"+"global "+str(t)+";"+str(t)+" = "+str(sequence_condition.get(r).get(t))
                              tab_backend_ref.append(data_condition)    
                    except:
                        pass 
         except:
             print("Not found the parameters input")

         try:
            if 'if' in r.split("_") and len(r.split("_")) >=2:
                    try:
                      if len(r.split("_")) ==2:
                        for d in list(sequence_condition.get(r)): 
                           data_condition = str(r.split("_")[0])+" "+str(d)+str(sequence_condition.get(r).get(d)) +":"
                           tab_backend_ref.append("\n"+data_condition)
                    except:
                        pass 
                    try:         
                      if r.split("_")[2] == 'nested':
                          print("Found nested function in if",len(tab_backend_ref),len(tab_count))
                          #tab_count.append(r.split("_")[2])
                          for d in list(sequence_condition.get(r)):
                             if checking_before_code(r) in list_condition:
                              
                                 data_condition = "\n"+len(tab_count)*"\t"+str(r.split("_")[0])+" "+str(d)+str(sequence_condition.get(r).get(d)) +":"
                                 tab_backend_ref.append(len(tab_backend_ref)*"\n"+data_condition)
                    except: 
                        pass 
                    try:
                       if r.split("_")[2] == 'nested':
                           print("Found nested function in if",len(tab_backend_ref),len(tab_count))
                           tab_count.append(r.split("_")[2])
                           for d in list(sequence_condition.get(r)):
                                if checking_before_code(r) not in list_condition:
                                     data_condition = "\n"+(len(tab_count)-1)*"\t"+str(r.split("_")[0])+" "+str(d)+str(sequence_condition.get(r).get(d)) +":"
                                     tab_backend_ref.append(data_condition)
                    except:
                         pass    
         except:
             print("Not found if conditioner input")
         try: 
        
            if "for" in r.split("_") and len(r.split("_")) >= 2: 
                       
                       
                        for er in list(sequence_condition.get(r)):
                            if checking_before_code not in list_condition:  
                                 tab_count.append(str(r.split("_")[1]))
                        
                            if er.split("_")[0] == 'v':
                                  
                                    print("Found for loop nested")
                                    try:
                                      if r.split("_")[2] == 'nested':
                                              if checking_before_code(r) in list_condition:
                                                   # Getting the index to check the parameter before the statement to check tab number parameter 
                                                   data_condition = "\n"+len(tab_count)*"\t"+str(r).split("_")[0] +" "+str(er)+" "+"in range("+str(sequence_condition.get(r).get(er)[0])+","+str(sequence_condition.get(r).get(er)[1])+"):"
                                                   tab_backend_ref.append(data_condition)
                                    except:
                                         pass                  
                                    
                            if er.split("_")[0] == 'v':
                                try:
                                    if len(r.split("_")) == 2:
                                                 
                                                 data_condition = "\n"+len(tab_count)*"\t"+str(r).split("_")[0] +" "+str(er)+" "+"in range("+str(sequence_condition.get(r).get(er)[0])+","+str(sequence_condition.get(r).get(er)[1])+"):"
                                                 tab_backend_ref.append(data_condition)
                                except:
                                     pass 
                            if er.split("_")[0] == 'v':
                                try:
                                    if r.split("_")[2] == 'nested':
                                       if checking_before_code(r) not in list_condition:
                                                 data_condition = "\n"+(len(tab_count)-1)*"\t"+str(r).split("_")[0] +" "+str(er)+" "+"in range("+str(sequence_condition.get(r).get(er)[0])+","+str(sequence_condition.get(r).get(er)[1])+"):"
                                                 tab_backend_ref.append(data_condition)
                                except:
                                     pass 
         except:  
             print("Running nested command in the list")  
         try: 
             if "command" in r.split("_") and len(r.split("_")) >= 2: 
                        print("In command condition")
                        try:
                          if r.split("_")[2] == 'nested':   
                                
                                tab_count.append(r)
                                for er in list(sequence_condition.get(r)):
                                           
                                           data_condition= "\n"+len(tab_count)*"\t"+str(sequence_condition.get(r).get(er)) 
                                           tab_backend_ref.append(data_condition)
                        except:
                             pass
                        if len(r.split("_")) == 2:   
                                print("Non nested case")
                                #tab_count.append(r)
                                for er in list(sequence_condition.get(r)):
                                           
                                           data_condition= "\n"+len(tab_count)*"\t"+str(sequence_condition.get(r).get(er)) 
                                           tab_backend_ref.append(data_condition)
         except: 
             print("Not found if conditioner")       
Sequence_loader()
print("Code list",tab_backend_ref)
print("Generated code")
print(' '.join(tab_backend_ref)) # This part can be convert and rewrite to another language 
exec(' '.join(tab_backend_ref)) # Execute in python language 

