import json
import configparser
import random
import time

class orderComplaint:

    def generateComplaintNumber(self):
        complaintNumber = "CN0X"
        timestamp = int(time.time())
        timestamp = str(timestamp)
        randomDigits = 17 - (len(timestamp))

        lower = 10 ** (randomDigits - 1)
        upper = (10 ** (randomDigits)) - 1
        generatedRandomNumber = random.randint(lower, upper)
        complaintNumber = complaintNumber + timestamp + str(generatedRandomNumber)
        return complaintNumber

    def registerComplaint(self,id):
            print(id)
            complaintresponse={}
            complaintNumber=""
            config = configparser.ConfigParser(allow_no_value=True)
            config.read('config.ini')           
        
            with open(config.get('DEFAULT', 'orderdatafile'), 'r') as orderStatus:
                data = json.load(orderStatus)
                output_dict = [x for x in data if x['template_id'] == id[-1:]]
           
                if len(output_dict)!=0:
                    filter_index = data.index(output_dict[0])                
                    
                    #update the complaintnumber if its empty or if its not there in the order_details
                    if 'complain_number' not in data[filter_index] or data[filter_index]["complain_number"]=="":
                        complaintNumber= orderComplaint.generateComplaintNumber(self)
                        data[filter_index]["complain_number"] = complaintNumber
                        with open(config.get('DEFAULT', 'orderdatafile'), 'w') as writer:
                            json.dump(data, writer, indent=4, sort_keys=False)
                            writer.close()
                    
                    #response body       
                    complaintresponse=data[filter_index]
                else:                
                    #Use Case when the requested order_id does not match any order details
                    complaintresponse["message"]='Order Not Found' 
            
            orderStatus.close()                          
                
            return json.dumps(complaintresponse)                
                



                



       













