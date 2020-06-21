import falcon
from data.mock.OrderComplaint import orderComplaint


class complaintOrder(object):
    
    def on_put(self,req,resp,id):
        
        if id !='': 
            complaintresponse=orderComplaint.registerComplaint(self,id)           
            resp.body=complaintresponse
            resp.status= falcon.HTTP_200

        else:            
            resp.body= 'No id provided, please provide an ID in url to make a valid call'
            resp.status=falcon.HTTP_404

        

