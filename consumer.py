from confluent_kafka import Consumer, KafkaException, KafkaError
import sys
from topics import Topic

# Kafka configurations
conf = {
    'bootstrap.servers': 'kafka-2:9094',   # Change to your Kafka broker address
    'group.id': 'shopping-consumer-group',          # Consumer group name
    'auto.offset.reset': 'earliest'           # Start from the earliest message if no offset exists
}

# Create the Kafka consumer instance
consumer = Consumer(conf)

# List of topics to consume from
topics = [Topic.SHOPPING]  # Replace with your topic name

def consume_messages():
    try:
        # Subscribe to the topic(s)
        consumer.subscribe(topics)

        print(f"Consumer started, listening to topics: {topics}")
        
        while True:
            # Poll for messages (timeout after 1 second)
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                # No message received in the last poll cycle
                continue
            if msg.error():
                # Error handling (e.g., KafkaError or other consumer-related errors)
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Print the consumed message
                print(f"Consumed message: {msg.value().decode('utf-8')} from topic: {msg.topic()}")

    except KeyboardInterrupt:
        print("Consumer interrupted")
    
    finally:
        # Close the consumer gracefully
        consumer.close()

if __name__ == "__main__":
    consume_messages()