import falcon

from resources.orderstatus import OrderStatus
from resources.ordertracking import OrderTracking
from resources.cancelorder import CancelOrder
from resources.ordercomplaint import complaintOrder

app = application = falcon.API()

orderstatus     = OrderStatus()
ordertracking   = OrderTracking()
cancelorder = CancelOrder()
ordercomplaint = complaintOrder()

app.add_route('/orders/{order_id}', orderstatus)
app.add_route('/tracking/{id}', ordertracking)
app.add_route('/cancel/{id}', cancelorder)
app.add_route('/complaint/{id}', ordercomplaint)
