# Aaryan Sharma
# 101230220
# --------------------
# add all other functions here

def display_2Dlist(alist):      #checks a list to see if empty
    
    if not alist:
        print("List is empty")
    else:
        for i in alist:
            print(i)

def dispaly_dict(adict):         #checks a diction to see if empty
    if not adict:
        print("Dictionary is empty.")
    else:
        for key,value in adict.items():     #method of printing dictionary line by line
            print(key,':',value)

def return_list(filename):              
    with open(filename,"r") as f:
        
        firstline = next(f)
        if firstline != None:
            listedata = []
            for line in f:
                data = line.strip("\n").split(",")
                listedata.append(data)
        
        for i in listedata:
            del i[4:] 
            
            
    return listedata



def return_dict(filename):  #returns a dictionary
    with open(filename,"r") as f:
        
        dicti = {}          #dictionary for data
        firstline = next(f) 
        if firstline != None:
            listedata = []
            for line in f:  
                data = line.strip("\n").split(",")      #correctly adding the data to the list(removing parts not needed)
                listedata.append(data)
            
            for i in listedata:
                key = int(i[3])
                values = i[4:]
                dicti[key] = values     #turns key into an integer, and adds all values afterwards
    
    
    
            
    return dicti



def display_2Dlist(database):   #stores 
    
    for i in database:
        print(i)

def get_total_cases(database,x):    #returns dictionary for question e
    casees_for_id = 0   #total cases
    diction = {}    #main dictionary
    
    if x==0:    #case reported date
        for values in database[1:]:
            if values[0] in diction:
                diction[values[0]]+=1   #if subcategory exists add 1 case
                casees_for_id+=1
            else:
                diction[values[0]]=1    #creates new subcategory 
                casees_for_id+=1
    elif x==1:  #case age group
        for values in database[1:]: 
            if values[1] in diction:
                diction[values[1]]+=1   #if subcategory exists add 1 case
                casees_for_id+=1
            else:
                diction[values[1]]=1    #creates new subcategory 
                casees_for_id+=1
    elif x==2:  #case gender
        for values in database[1:]: 
            if values[2] in diction:
                diction[values[2]]+=1   #if subcategory exists add 1 case
                casees_for_id+=1
            else:
                diction[values[2]]=1    #creates new subcategory 
                casees_for_id+=1
    
    
    for key,value in diction.items():       #method of printing values in dictionary with key line by line
        print(key,":",value)

    print("Total cases : "+str(casees_for_id))  #just the total number of cases
    return diction


def display_PHU_summary(database,dicti,id):     #checks id and prints certain elements of id accordingly
    cases = 0
    
    for i in database:          #to count the number of cases for an id
        if id == int(i[3]):
            cases+=1
    
    if id in dicti:             #checks if id is in the dictionary
        print("PHU_ID:",id)     
        for i in dicti:
            
            if i == id:     #appending items to the dictionary
                
                PHU_list = dicti[i]
                newdict = {}
                newdict['PHU_NAME'] = PHU_list[0]
                newdict['PHI_CITY'] = PHU_list[1], PHU_list[2]
                newdict['PHU_WEBSITE'] = PHU_list[3]
        for key,values in newdict.items():         #prints the dictionary
            print(key,":",values) 
        print("Total cases: "+str(cases))

    else:
        print("PHU ID is invalid")  #if id not in dictionary such is printed




def get_cases_by_PHU_and_age(database,dicti):   #collects PHU ID and ages, with how many effected with the respective ID + age
    
    
    agediction = {}
    
    for i in database:
        diction_list = []
        
        if i[3] in agediction:                  #checks if the id is already in dictionary
            
            if [i[1],1] in agediction[i[3]]:    #checks if count needs to be increased
                alreadyin = agediction[i[3]]
                for j in alreadyin:             #used to increase count if age is already present
                    j[1]+=1                          

            
            else:                                #adds new age
                diction_list.append([i[1],1])
                agediction[i[3]] = agediction[i[3]] + diction_list
            
            
            

                        
        else: #if id not in the dictionary, it appends it
            
            
            diction_list.append([i[1],1])   
            

            

            agediction[i[3]]=diction_list

    

    for keys,values in agediction.items():
        print(keys,":",values)



#def get_topx_hotspots(database,dicti,y): 
    
    #cases = 0
    #casesdiction={}

    #could not figure out this function, my apologies


        




    




        

    



    



# --------------------
# the main function, call all other functions inside of this function 
def main():
    
    alist = [[1,2],[3,4],[5],[6,7]] #random list test
    display_2Dlist(alist)
    
    
    

    filename = "Assignment 3\data10.csv" #example filename
    
    return_list(filename)
    database = return_list(filename)
    display_2Dlist(database)

    return_dict(filename)
    
    dicti = return_dict(filename)
    dispaly_dict(dicti)

    x=2     #example category
    get_total_cases(database,x)

    id = 3895   #example id
    display_PHU_summary(database,dicti,id)

    
    get_cases_by_PHU_and_age(database,dicti)

    #y = 1
    #get_topx_hotspots(database,dicti,y)
    
    #the above comment states how the y would be called towards the function(just before the function)

   



    




    





# the main guard, calls the main() function only if you run this program as a stand-alone program
if __name__ == "__main__":
    main()