# kafka-python


# Kafka Producer and Consumer Application

## Introduction
This application consists of Python scripts for a Kafka producer and consumer, along with Docker Compose configuration for running Kafka and Zookeeper services.

## Producer Script (producer.py)
The `producer.py` script fetches data from the JCDecaux bike sharing API and sends it to a Kafka topic named "velib-stations".

### Dependencies
- Python
- Kafka Python library (`kafka-python`)
- `urllib` module for fetching data from the API

### Operation
1. Import necessary libraries.
2. Define API key and URL for JCDecaux API.
3. Define Kafka bootstrap servers.
4. Create a Kafka producer.
5. Fetch data from the API and send it to the Kafka topic.

## Consumer Script (consumer.py)
The `consumer.py` script subscribes to the "velib-stations" Kafka topic, reads messages, and processes them.

### Dependencies
- Python
- Kafka Python library (`kafka-python`)

### Operation
1. Import necessary libraries.
2. Create a Kafka consumer.
3. Consume messages from the Kafka topic and process them.

## Docker Compose Setup (docker-compose.yml)
The Docker Compose setup defines services for Zookeeper and Kafka, using Confluent images.

### Configuration
- Zookeeper: Defines three instances of Zookeeper with different server IDs and client ports.
- Kafka: Defines three Kafka broker instances, each connected to the respective Zookeeper instance. Advertised listeners are set to `localhost` for internal communication.

## Running the Application
1. Clone the repository.
2. Navigate to the repository directory.
3. Start Kafka and Zookeeper using Docker Compose:
   ```bash
   docker-compose up -d
