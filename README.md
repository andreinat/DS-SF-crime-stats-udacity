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

#### Start Kafka Server

```/usr/bin/kafka-server-start config/server.properties```

#### Start producer

```python kafka_server.py```

#### Kafka consumer

```bin/kafka-console-consumer.sh --bootstrap-server localhost:<your-port-number> --topic <your-topic-name> --from-beginning```

#### Spark job

```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py```

### Test producer

Alternatively you should use the consumer_server.py to test if the producer was properly configured


### How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Changing the parameters increase or decrease the data ingestion, and can be seen in the value of “processedRowsPerSecond”.

### What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Following the previous logic, I used the processedRowsPerSecond as indicator, and tried modifying different parameters:
* maxRatePerPartition using 10
* spark.sql.shuffle.partitions using 8

It seems like the best performance was using these 2 values, increased almost by 10x the processed rows

