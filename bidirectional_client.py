from __future__ import print_function

import bidirectional_pb2 as bidirectional_pb2
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import grpc
import time

from faker import Faker
fake_data = Faker()


'''def generate_fake_data():
    for _ in range(0,30):
        data=[fake_data.name(),fake_data.address()]
        print(data)
        '''
        
    
'''    
def make_data(fake_data):
    return bidirectional_pb2.Message(
        message=fake_data
    )
    '''

'''
def generate_messages(channel):
    for _ in range(0,10):
        
        messages = [
            make_data(channel),
            make_data(fake_data.name()),
            make_data(fake_data.email()),
            
        ]
        for msg in messages:
            print("Hello Server Sending you the %s" % msg.message)
            yield msg
'''
'''
def send_message(stub):
    startTime = time.time()
    responses = stub.GetServerResponse(generate_messages())
    endTime = time.time()
    print(endTime-startTime)
    for response in responses:
        print("Hello from the server received your %s" % response.message)
'''

def run():
    for _ in range(0,30):
        messages=[fake_data.name(),fake_data.address()]
        #print(messages)
  
    p = Publisher('localhost',50051)
    #p = p.connect()
    
    msg=p.response(p.bind_message(messages,"test"),"test")
    print(msg)
        
class Publisher(object):
    
    def __init__(self,host,port):
        
        #initiate channel
        self.channel = grpc.insecure_channel('{}:{}'.format(host,port))
        #self.stub = None  
        self.stub = bidirectional_pb2_grpc.BidirectionalStub(self.channel)

        self.name=None 
    '''    
    def connect(self):
        self.stub = bidirectional_pb2_grpc.BidirectionalStub(self.channel)
        #self.name = name
        return self.stub
        '''
    def response(self,message,channel):
        message=bidirectional_pb2.Message(message=message,channel=channel)
        responses = self.stub.GetServerResponse(message)
        print(responses)
        #todo if response.channel == channel 
        #         yeild response 
        #     else 
        #         yeild(none,response)
        yield (self.name, responses)
    
    def bind_message(self,message,channel):
        return bidirectional_pb2.Message(
        message=str(message),
        channel=str(channel)
    )


if __name__ == '__main__':
    run()
