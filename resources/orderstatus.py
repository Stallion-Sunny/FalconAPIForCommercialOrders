import json
import falcon
import utils.validator as validator
from data.mock.OrderStatusData import OrderStatusData

class OrderStatus(object):
    
    def on_get(self, req, resp, order_id):
        if validator.validate_orderId(order_id):       
            resp.body = OrderStatusData.toJson(self,order_id)
            resp.status = falcon.HTTP_200
        else :
            resp.status = falcon.HTTP_404