import pika, json

params = pika.URLParameters("amqps://wnulaqag:U6o1HBmSm_ObLXWJJO-S00hIP9JnHJbC@rat.rmq2.cloudamqp.com/wnulaqag")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
