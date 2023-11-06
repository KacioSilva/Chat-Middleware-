from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

# Configurações do RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')

    if message:
        channel.basic_publish(exchange='', routing_key='message_queue', body=message)
        return jsonify({"status": "Message sent"})
    else:
        return jsonify({"error": "Message is empty"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
