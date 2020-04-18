# DS-SF-crime-stats-udacity
Analysis of San Francisco Crime Incidents using Kafka &amp; Spark

## Dev Environment

* Spark 2.4.3
* Scala 2.11.x
* Java 1.8.x
* Kafka build with Scala 2.11.x
* Python 3.6.x or 3.7.x

## How to run
Start Zookeeper Server

```/usr/bin/zookeeper-server-start config/zookeeper.properties```

Start Kafka Server

```/usr/bin/kafka-server-start producer.properties```

Start producer

```python kafka_server.py```

Kafka consumer

```bin/kafka-console-consumer.sh --bootstrap-server localhost:<your-port-number> --topic <your-topic-name> --from-beginning```

Spark job

```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py```
