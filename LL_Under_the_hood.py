head={
       "value":11,
       "next":{
                 "value":3,
                 "next":{
                         "value":23,
                          "next":{
                                   "value":7,    #Tail
                                   "next":None  
                                }
                        }
                }
    }

print(head['next']['next']['next']['value'])

#This will only run with a linkedlist
#print(my_linked_list.head.next.next.value)
