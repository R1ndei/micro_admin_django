import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_django.settings")
django.setup()

from products.models import Product

params = pika.URLParameters("amqps://wnulaqag:U6o1HBmSm_ObLXWJJO-S00hIP9JnHJbC@rat.rmq2.cloudamqp.com/wnulaqag")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("STARTED")

channel.start_consuming()

channel.close()
