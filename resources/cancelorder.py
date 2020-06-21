import json
import falcon
import utils.validator as validator
from data.mock.OrderCancel import OrderCancel


class CancelOrder(object):
        
        def on_put(self, req, resp, id):
            if validator.validate_orderId(id):
                response =  OrderCancel.cancel(self, id)      
                resp.body = response
                resp.status = falcon.HTTP_200
            else :
                resp.status = falcon.HTTP_404

