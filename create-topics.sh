#!/bin/bash
# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
cub kafka-ready -b kafka-1:9092 1 20

# Create topic with desired number of partitions
echo "Creating topic 'shopping' with 10 partitions"
/bin/./kafka-topics --create \
  --bootstrap-server kafka-1:9092 \
  --topic shopping \
  --partitions 10 \
  --replication-factor 3 \
  --if-not-exists

# You can add more topics if needed
# kafka-topics.sh --create \
#   --bootstrap-server kafka-1:9092 \
#   --topic another_topic \
#   --partitions 5 \
#   --replication-factor 3 \
#   --if-not-exists