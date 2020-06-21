import json
import configparser


class OrderCancel:
    
    def cancel(self, id):
            # cancelresponse = {}
                        
            config = configparser.ConfigParser(allow_no_value=True)
            config.read('config.ini')
            #print(config.sections())
            with open(config.get('DEFAULT', 'orderdatafile'), 'r') as orderStatus:
                data = json.load(orderStatus)
                orderStatus.close()

                # Filter python objects with list comprehensions
                output_dict = [x for x in data if x['template_id'] == id[-1:] and x['order_status'] !="cancelled"]
                if len(output_dict) !=0:
                    filter_index = data.index(output_dict[0])              
        

                    data[filter_index]["order_status"] = "cancelled"
                    data[filter_index]["is_cancelled"] ="True"
                       
                    # writer the updates back to json file
                    # with open(config.get('DEFAULT', 'orderdatafile'), 'w') as writer:
                    #     json.dump(data, writer, indent=4, sort_keys=False)
                    #     writer.close()
                     
                    # cancelresponse["order_id"] = data[filter_index]["order_id"]
                    # cancelresponse["name"]=output_dict[0]["name"]
                    # cancelresponse["order_status"]=output_dict[0]["order_status"]
                    return json.dumps(output_dict[0])
                        
                else:
                   # cancelresponse["message"] ="No record found for cancellation."
                   return json.dumps("No record found for cancellation." )
            

           