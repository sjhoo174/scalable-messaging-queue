from confluent_kafka import Producer
import multiprocessing
from topics import Topic
import sys

# Kafka configurations
conf = {
    'bootstrap.servers': 'kafka-1:9092',  # Kafka broker address
    'client.id': 'customers',         # Client ID for the producer
}

# Create the Kafka producer instance

# This function will be called whenever a message is successfully delivered to the Kafka broker or an error occurs
def delivery_report(err, msg):
    """ Callback function to confirm message delivery or error. """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

NUMBER_OF_CUSTOMERS = 100
NUMBER_OF_CUSTOMER_ACTIONS = 5

def customer_worker(customer_id):
    producer = Producer(conf)
    try:
        # for i in range(NUMBER_OF_CUSTOMER_ACTIONS):
        while True:
            i = 0
            message = f"customer {customer_id} performed action {i+1}"
            print(f"Customer {customer_id} sending action {i}")
            # Produce the message to the Kafka topic asynchronously
            producer.produce(Topic.SHOPPING, key=str(customer_id).encode('utf-8'),  value=message.encode('utf-8'), callback=delivery_report)

            # Poll to handle delivery reports
            producer.poll(0)
            print(f"Customer {customer_id} finished polling after action {i}")

            # Ensure all messages are delivered before exiting
            producer.flush()
    except KeyboardInterrupt:
        print("\nProducer interrupted.")


def produce_messages():
    processes = []
    for i in range(1, NUMBER_OF_CUSTOMERS+1):  # Create 100 processes
        p = multiprocessing.Process(target=customer_worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All customers finished processing")


if __name__ == "__main__":
    produce_messages()
