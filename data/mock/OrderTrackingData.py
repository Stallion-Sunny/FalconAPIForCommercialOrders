import json
import configparser


class OrderTrackingData:
    def toJson(self, id):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('config.ini')
        #print(config.sections())
        with open(config.get('DEFAULT', 'orderdatafile'), 'r') as orderStatus:
            data = json.load(orderStatus)

            # Filter python objects with list comprehensions
        output_dict = [x for x in data if x['template_id'] == id[-1:]]
        # return data in json array
        return json.dumps(output_dict)
