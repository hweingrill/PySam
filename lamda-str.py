                    # Python3 code to demonstrate working of
                    # Converting None to empty string
                    # Using lambda or second part using "str"

test_list = ["Geeks",None,"CS",None,None]
print ("The original list is : " + str(test_list))

                    # using lambda: Converting 'None' to empty string
conv = lambda i : i or ''
res = [conv(i) for i in test_list ]
print("The list after conversion of None values : " + str(res))

#------------------------> second Part <-----------------------

test_list = ["Geeks",None,"CS",None,None]
print ("The original list is : " + str(test_list))
                   
                    # using str() Converting 'None' to empty string
res = [str(i or '') for i in test_list]
print("The list after conversion of None values : " + str(res))

#----------------------------> create DICT <--------------------------
                      # Python code to demonstrate
                      # converting list into dictionary with none values
                      # using zip() and dictionary
                      # initializing list

ini_list = [1,2,3,4,5]
print ("initial list", str(ini_list))

                      # Converting list into dictionary using zip() and dictionary
res = dict(zip(ini_list, [None]*len(ini_list)))
                     
                     # printing final result
print("final dictionary",str(res))

#---------------------------> USING dict <-----------------------------                     
ini_list = [1,2,3,4,5]

                      # Converting list into dict()
res = dict.fromkeys(ini_list)
print("final dictionary",str(res))
