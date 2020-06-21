import json
import falcon
import utils.validator as validator
from data.mock.OrderTrackingData import OrderTrackingData

class OrderTracking(object):
    
    def on_get(self, req, resp, id):
        orderTracking = OrderTrackingData()
        if validator.validate_orderId(id) or validator.validate_trackingId(id):
            resp.body = orderTracking.toJson(id)
            resp.status = falcon.status.HTTP_200

        else:
            resp.status=falcon.status.HTTP_404