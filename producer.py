from faker import Faker
from kafka import KafkaProducer
import json
import time
faker=Faker()
def get_register_data():
    return {
        "name":faker.name(),
        "address":faker.address(),
        "created_at":faker.year()
        
    }
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer=KafkaProducer(bootstrap_servers=['machine_ip:9092'],
                       value_serializer=json_serializer)

if __name__=="__main__":
    while True:
        register_data=get_register_data()
        print(register_data)
        producer.send('registered_user',register_data)
        time.sleep(3)