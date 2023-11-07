import pika

# Conectar-se ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar a fila da qual você deseja consumir mensagens
channel.queue_declare(queue='message_queue')

# Callback para lidar com mensagens recebidas
def callback(ch, method, properties, body):
    print(f"Received message: {body}")

# Configurar o consumidor
channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit, press Ctrl+C')

# Começar a consumir mensagens
channel.start_consuming()
