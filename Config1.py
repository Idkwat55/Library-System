
import  Config



def save1(host_,user_,password_,database_,table_):
    fileName = "Config.py"
    
    with    open(fileName,'a+') as write:
        write.write("\nkey_%s ={'HOST' :'%s','USER':'%s','PASSWORD':'%s', 'DATABASE':'%s' , 'TABLE':'%s'}\n    "%(Config.keys_stored,host_,user_,password_,database_,table_))
        
        Config.key_list.append('key_{}'.format(Config.keys_stored))
        Config.keys_stored = Config.keys_stored+1 
        print(Config.key_list)
        ke_lst = Config.key_list.copy()
        ke_lst = str(ke_lst)
        ke_lst = ke_lst.replace("'","")
        
        with open(fileName, 'r', encoding='utf-8') as file:
            data = file.readlines()
            data[0] = "keys_stored = {}\n".format(Config.keys_stored)
 
        with open(fileName, 'w', encoding='utf-8') as file:
            file.writelines(data[:-1])
            
    #with open(fileName, 'r', encoding='utf-8') as file1:
        #data1 = file1.readlines()
        
    with open(fileName, 'a', encoding='utf-8') as file1:
        file1.write( "\nkey_list ={}\n".format(ke_lst))
 

            
            
 
   
        print('Credentials saved')
    write.close()
    file.close()
    

