![kafka](https://github.com/choojun/choojun.github.io/assets/6356054/9e24ef13-f41f-4d8a-a731-889cdb9f76df)

# J. Kafka [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. Kafka has three key capabilities under a distributed, highly scalable, elastic, fault-tolerant, and secure manner, as listed as follow
   * To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems
   * To store streams of events durably and reliably for as long as you want
   * To process streams of events as they occur or retrospectively
2. Kafka is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol. As a server, Kafka is run as a cluster of one or more servers that can span multiple datacenters or cloud regions. As a clients, Kafka allows us to write distributed applications and microservices that read, write, and process streams of events in parallel, at scale, and in a fault-tolerant manner even in the case of network problems or machine failures
3. Read more on Kafka and its related middlewares at URL https://kafka.apache.org/documentation/ , https://kafka.apache.org/quickstart and https://doc.akka.io/libraries/alpakka-kafka/current/home.html

## J1. Install Kafka [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Login as **hduser**, and check the installed scala package
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ scala -version
   ~~~

2. You may install the required scala version (2.13.x) as steps as follows
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ sudo apt update && sudo apt install zip unzip
   hduser@MyPC:~$ curl -s "https://get.sdkman.io" | bash
   hduser@MyPC:~$ source "/home/hduser/.sdkman/bin/sdkman-init.sh"
   hduser@MyPC:~$ sdk install scala 2.13.16
   hduser@MyPC:~$ scala -version
   ~~~

3. Download and setup the respective version of Kafka based on the installed version of Scala. The available Kafka versions may be found at the Kafka download page - https://kafka.apache.org/downloads
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ wget https://archive.apache.org/dist/kafka/4.3.1/kafka_2.13-4.3.1.tgz
   hduser@MyPC:~$ tar -xvzf kafka_2.13-4.3.1.tgz  
   hduser@MyPC:~$ mv kafka_2.13-4.3.1 kafka
   hduser@MyPC:~$ chown hduser:hadoop -R kafka
   ~~~
4. In ~/.bashrc file, add the following lines at the end of the file.
   ~~~bash
   export KAFKA_HOME=/home/hduser/kafka
   export PATH=$PATH:$KAFKA_HOME/bin
   ~~~
   > Remember to issue source ~/.bashrc after saving the file.

## J2. Starting and Stopping Kafka Broker [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Remain login as **hduser**. Ensure the following services started sequentially and check them with command jps
    - SSH
    - HDFS
    - YARN

2. Start Kafka broker server in the background after generated the UUID and formatted the required storage.
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ KAFKA_CLUSTER_ID="$(~/kafka/bin/kafka-storage.sh random-uuid)"
   hduser@MyPC:~$ ~/kafka/bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c ~/kafka/config/server.properties
   hduser@MyPC:~$ ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties
   hduser@MyPC:~$ jps
   ~~~
   > You should observe the Kafka process with the command jps. You should observe a total of **seven** services, i.e. Jps, SecondaryNameNode, ResourceManager, NodeManager, DataNode, Kafka, NameNode
   >
   Note that you need to generate one ID, and use the same ID on all cluster nodes. In s multiple nodes of cluster environment, you need to run the storage tool script on each node utilizing the same cluster ID, example: **bin/kafka-storage.sh format -t <CLUSTER_ID> -c <path-to-server.properties>** . When You Would Need to Format Again?
 
   * **Brand new node**: When provisioning a fresh node or adding a new broker to an existing quorum for the first time.

   * **Wiped data directories (applied to standalone mode)**: If you manually clear, or delete the contents of your configured log.dirs (happening  when shutdown distro of WSL). Deleting log.dirs including any events you have created along the way, can be performed manually using the command line: **rm -rf /tmp/kafka-logs /tmp/kraft-combined-logs** .

   * **Cluster reset (applied to standalone mode)**: If you are intentionally tearing down the cluster and building a brand-new cluster ID.

   Apache Kafka 4.0 (released in March 2025) and KRaft are permanently and exclusively linked because Kafka 4.0 has completely removed Apache ZooKeeper and relies on KRaft as its sole metadata management system. **KRaft** stands for **Kafka Raft** — Kafka’s own implementation of the Raft consensus protocol. Instead of relying on an external system, i.e. ZooKeeper, Kafka now manages its own metadata using a quorum of dedicated controller nodes within the cluster itself. in KRaft, a set of controller nodes (typically 3 or 5) form a Raft quorum. One is elected the active controller and manages a special metadata partition log. All cluster metadata — topics, partitions, ISRs, configurations — is stored in this internal log. When the active controller fails, the Raft protocol ensures a new leader is elected from the remaining controllers, and because they already have the metadata in memory, failover is nearly instantaneous.

| Aspect of Kafka with   | ZooKeeper (ZK) Mode           | KRaft Model                     |
|------------------------|-------------------------------|---------------------------------|
| 1. Architecture           | Two separate systems          | Single self-contained system    |
| 2. Metadata Storage       | ZooKeeper znodes              | Internal Kafka metadata log     |
| 3. Controller Election    | Ephemeral znodes in ZK        | Raft consensus amon controllers |
| 4. Failover Speed         | Seconds to minutes            | Near-instantaneous (in-memory)  |
| 5. Partition Limit        | ~200,000 practical ceiling    | Millions of partition supported |
| 6. Operational Complexity | Manage 2 cluster & monitoring | Manage 1 system                 |
| 7. Security Config        | Separate ZK + Kafka auth      | Unified security model          |
| 8. Recovery Time          | Load full state from ZK       | 10x faster - already in memory  |

3. Stopping Kafka.
   ~~~bash
   hduser@MyPC:~$ cd ~/kafka
   hduser@MyPC:~$ ~/kafka/bin/kafka-server-stop.sh
   hduser@MyPC:~$ jps
   ~~~
   > **Attention**: When you have finished your exercises (before shutdown your Windows), you need stop the HDFS, YARN and Kafka services.




## J3. Producing and Examining Messages - using Terminal [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Remain login as **hduser**. 
2. Create a Topic.
   ~~~bash
   hduser@MyPC:~$ ~/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
   ~~~

3. List all available topics
   ~~~bash
   hduser@MyPC:~$ ~/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   ~~~

4. Create another topic known as automobile.
5. List all available topics.
6. To obtain information about a specific Kafka topic
   ~~~
   hduser@MyPC:~$ ~/kafka/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test
   ~~~



## J4. Producer - Consumer Terminals [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. To simulate a **producer terminal**, open another terminal of Ubuntu and login as **hduser**.
2. List all available topics, and carry out the following steps after your Consumer Terminal is ready to consume messages.

3. **Producer terminal**: Send a few messages under the topic test.
   ~~~
   hduser@MyPC:~$ ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
   ~~~
   > A prompt (>) should appear for you to input your messages. For example, type in the following messages
   > > This is the first test message
   > > 
   > > This is the second test message
   > 
   > To quit, press Ctrl-C. Note that messages are stored by default in the /tmp/kafka-logs/ directory or set as the value of log.dirs in the config/server.properties file.

4. **Producer terminal**: To delete a specific topic.
   ~~~
   hduser@MyPC:~$ ~/kafka/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic test
   ~~~

5. To simulate a **consumer terminal**, open another terminal of Ubuntu and login as **hduser**.
6. **Consumer terminal**: To consume messages by start a console-based consumer with command as follow.
   ~~~
   hduser@MyPC:~$ ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
   ~~~
   > At your **Producer terminal**, send more messages (refer to Step 3) and observe corresponding effects. Note that new messages arriving in the **Consumer terminal**.

6. To examine the incoming messages.
   ~~~
   hduser@MyPC:~$ ~/kafka/bin/kafka-run-class.sh kafka.tools.DumpLogSegments --deep-iteration --print-data-log --files /tmp/kraft-combined-logs/test-0/00000000000000000000.log
   ~~~
   > Note that follow the file name of the *.log file that appears in your directory


## J5. Accessing Kafka in Python [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Login as **hduser**, activate the venv, and check the installed kafka-python package
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduser@MyPC:~$ pip install kafka-python
   ~~~

2. Use another terminal as **consumer** by login as **hduser**, activate the venv, and start the python interpreter
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduser@MyPC:~$ python
   ~~~

3. In the **consumer terminal**, enter the following Python statements to consume messages
   ~~~python
   >>> from kafka import KafkaConsumer
   >>> consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
   >>> 
   >>> for msg in consumer:
   ...     print("msg: ", msg)
   ~~~

4. Use another terminal as **producer** by login as **hduser**, activate the venv, and start the python interpreter
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduser@MyPC:~$ python
   ~~~

5. In the **producer terminal**, enter the following Python statements to generate messages
   ~~~python
   >>> from kafka import KafkaProducer
   >>> from json import dumps
   >>> producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
   >>> producer.send('automobile', value='The new Ford Ranger')
   >>> import time
   >>> i = 1
   >>> while True:
   ...     time.sleep(10)
   ...     print("i = ", i)
   ...     producer.send('test', str(i*10) + " seconds have passed")
   ...     i += 1
   ~~~

6. Further configure delay in sending out messages from **producer terminal**.
   By default, a buffer is available to send the messages immediately even if there is still unused space in the buffer. To reduce the number of requests, you may set the linger_ms parameter of the KafkaProducer constructor to instruct the producer to wait up to the given number of ms before sending a request in order to enable more records to arrive for batch sending of the messages, thus leading to fewer and more efficient requests handling when not under the maximal load at the cost of a small amount of latency.
   ~~~python
   >>> producer=KafkaProducer(linger_ms=8000, bootstrap_servers=['localhost:9092'], value_serializer=lambda x:dumps(x).encode('utf-8'))
   >>> producer.flush()
   >>> future=producer.send('test','test message 1')
   >>> future=producer.send('test','test message 2')
   >>> future=producer.send('test','test message 3')
   ~~~
   > In the above example, the 8s delay will result in all three messages appearing at almost the same time to the consumer.


## J6. Accessing Kafka in PySpark Interactive Shell (Pyspark Shell) - by Specifying Partition [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Use another terminal as **producer** by login as **hduser**, activate the venv, and invoke the Pyspark Shell with 4 executor cores
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduserMyPC@MyPC:~$ pyspark --executor-cores 4
   ~~~

2. In the **producer terminal**, enter the following Python statements to generate messages
   ~~~python
   >>> from kafka import KafkaProducer
   >>> from json import dumps
   >>> import time
   >>> producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
   >>> i = 1
   >>> while True:
   ...	  time.sleep(10)
   ...	  print("i = ", i)
   ...	  producer.send('test', str(i*10) + " seconds have passed", partition=0)
   ...     i += 1
   ~~~

3. Use another terminal as **consumer** by login as **hduser**, activate the venv, and invoke Pyspark Shell
   ~~~python
   >>> from kafka import KafkaConsumer                                                  
   >>> from kafka import TopicPartition
   >>> consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
   >>> consumer.assign([TopicPartition('test', 2)])
   >>> consumer.assign([TopicPartition('test', 0)])
   >>> for msg in consumer:
   ...     print("msg in consumer ", msg)
   ~~~


## J7. Accessing Kafka in in PySpark Interactive Shell (Pyspark Shell) - with Serialized JSON Messages [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. In **producer terminal**, update the following lines of code based on the copy of J6
   ~~~python
   >>> i = 1                                               
   >>> while True:
   ...     output = "Elapsed time: " + str(i * 10) + "s"
   ...     producer.send('test', {'message':output})
   ...     print('message ' + output + " sent")
   ...     time.sleep(10)
   ...     i += 1
   ~~~

2. Create a file named send_messages.py
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduserMyPC@MyPC:~$ nano send_messages.py
   ~~~

3. Add the following statements into send_messages.py and then save the file
   ~~~python
   from kafka import KafkaProducer
   from json import dumps
   import time
   producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
   producer.send('automobile', value='The new Proton X70')
   producer.send('automobile', value='Proton X50')
   producer.flush()
   ~~~

4. Run the python file
   ~~~bash
   (de-test-venv) hduserMyPC@MyPC:~$ python send_messages.py
   ~~~

5. Exit the Pyspark Shell and deactivate the virtual environment for ending the exercise.
   ~~~bash
   >>> exit()
   (de-test-venv) hduserMyPC@MyPC:~$ deactivate
   hduserMyPC@MyPC:~$
   ~~~




