# Data Engineering with Distributed Environment for Data Analytics: 
## An One-Stop of Setup and Configuration in the Microsoft Windows Subsystem for Linux (WSL) - UBuntu 24.04 LTS

Data engineering involves building systems to collect and utilize data. This data typically supports subsequent analysis and data science, often incorporating machine learning. Making data usable generally requires significant computational resources, storage, and processing. In essence, data engineering is the design and development of systems that allow individuals to gather and analyze raw data from diverse sources and formats. This website provides a one-stop setup and configuration for the system using Microsoft WSL. Hereby, the website has also incorporated a suite of distributed-ready open source software and guided exploration through selected application samples in the following setup sections.

| Section (Tested with WSL2 and [Ubuntu](https://ubuntu.com/) 24.04 LTS) | Windows 7 | Windows 10 | Windows 11 |
|---|---|---|---|
| A. [Remove/Setup WSL with Ubuntu](wsl_setup.md) | ❌ | ✔ | ✔ |
| B. [Running Ubuntu on WSL](wsl_ubuntu.md) | ❌ | ✔ | ✔ |
| C. [Backup the Distro on WSL](wsl_backup.md) | ❌ | ✔ | ✔ |
| D. [Restore (Import) the Distro on WSL](wsl_restore.md) | ❌ | ✔ | ✔ |

#### Note for Apple MacOS users
If you are using Apple machines (MacBooks and iMacs with Intel/Apple Silicon processor), you may need to install [VMware Fusion Pro](https://blogs.vmware.com/cloud-foundation/tag/desktop-hypervisor/) (Free for educational and personal use) to virtualize Ubuntu 24.04.x. You can find the specific 24.04.x installer at https://ubuntu.com/download/alternative-downloads. After completing the Ubuntu setup, follow the same instructions in Sections E to Z to set up the required environment.

| Setup Section (Tested with [OpenJDK](https://openjdk.org/) 17 LTS) | Required Framework and Software Combinations |
|---|---|
| E. [Hadoop](wsl_hadoop.md)| [Apache Hadoop](https://hadoop.apache.org/) 3.4.1 or 3.4.3 ? E5-2, E8-3| 
| F. [HDFS File Operations and MapReduce](wsl_hdfs.md) | [Apache Hadoop](https://hadoop.apache.org/) 3.4.1 | 
| G. [Spark, PySpark Shell, Spark SQL and JupyterLab](wsl_pyspark.md) | [Apache Spark](https://spark.apache.org/) 4.0.4 or 4.0.5 ? G1-2, G2-1 | 
| H. [Spark and Machine Learning](wsl_pyspark_ml.md) | [Apache Spark](https://spark.apache.org/) 4.0.4 with Scala 2.13.18 |  
| I. [Spark and Visualisation](wsl_pyspark_viz.md) | [Apache Spark](https://spark.apache.org/) 4.0.4 with Scala 2.13.18 | 
| J. [Kafka](wsl_kafka.md) | [Apache Kafka](https://kafka.apache.org/) 4.3.1 or 4.3.2 ? J1-3 | 
| K. [HBase](wsl_hbase.md) | [Apache HBase](https://hbase.apache.org/) 3.0.0 ? K1-2, K1-3, K1-4 |
| L. [HappyBase with HBase Thift](wsl_happybase.md) | [HappyBase](https://happybase.readthedocs.io/) 1.2.0 | 
| M. [Hive with Tez and MySQL](wsl_hive.md) | [Apache Hive](https://hive.apache.org/) 4.2.1 with [Apache Tez](https://tez.apache.org/) 0.10.5 and [MySQL](https://www.mysql.com/downloads/) 8.0.46 |
> Needed Web browser, constant Internet connection, [SSH](https://en.wikipedia.org/wiki/Secure_Shell) and [PDSH](https://github.com/chaos/pdsh), [Python](https://www.python.org/) 3.12.x
>
> **Optional**: To restore from the pre-setup WSL distro, download the required release from the URL https://github.com/choojun/wsl/releases and follow the steps in Section D after identifying your Ubuntu version.

-----------------------------------------------------------

Assuming you have successfully set up all the required frameworks and software listed above, run the following commands:

### 1. To start all services, e.g. at the beginning of every practical.

> [!NOTE]
> **Session 1**
~~~bash
tarumt@MyPC:~$ su - hduser
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ sudo service ssh start
hduser@MyPC:~$ sudo service ssh status
hduser@MyPC:~$ ~/hadoop3/sbin/start-dfs.sh
hduser@MyPC:~$ ~/hadoop3/sbin/start-yarn.sh
hduser@MyPC:~$ jps
~~~
> Six (6) active services can be observed, including jps, DataNode, NameNode, SecondaryNameNode, NodeManager, ResourceManager. <br>
> <img width="28" height="25" alt="o5" src="https://github.com/user-attachments/assets/0ef39d71-d3a0-4088-99d1-0d2861a016df" /> Self-check: <br>
> DFS - http://localhost:9870 <br>
> YARN - http://localhost:8088/

~~~bash
hduser@MyPC:~$ cd ~/kafka
hduser@MyPC:~/kafka$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
hduser@MyPC:~/kafka$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
hduser@MyPC:~/kafka$ bin/kafka-server-start.sh config/server.properties
~~~


> [!NOTE]
> **Session 2**

Start the ZooKeeper, Hbase and Thrift services.
~~~bash
hduser@MyPC:~$ cd ~/hbase
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ ~/hbase/bin/hbase-daemon.sh start zookeeper
hduser@MyPC:~$ ~/hbase/bin/start-hbase.sh
hduser@MyPC:~$ jps
hduser@MyPC:~/hbase$ bin/hbase thrift start -p 9090 &
hduser@MyPC:~/hbase$ 
hduser@MyPC:~/hbase$ jps
~~~
> <img width="28" height="25" alt="o5" src="https://github.com/user-attachments/assets/0ef39d71-d3a0-4088-99d1-0d2861a016df" /> Self-check: <br>
> HBase web UI - http://localhost:16010

~~~bash
hduser@MyPC:~$ ~/hadoop3/bin/yarn --daemon start timelineserver
hduser@MyPC:~$ jps
hduser@MyPC:~$ sudo systemctl start apache2
hduser@MyPC:~$ sudo systemctl status apache2
hduser@MyPC:~$
~~~
> <img width="28" height="25" alt="o5" src="https://github.com/user-attachments/assets/0ef39d71-d3a0-4088-99d1-0d2861a016df" /> Self-check: <br>
> Tez web UI - http://localhost/tez-ui/ <br>
> It visualises Directed Acyclic Graphs (DAGs), vertices, tasks, data transfer edges, and resource bottlenecks for Tez jobs.

Start the HiveServer2
~~~bash
hduser@MyPC:~$ cd ~/hive
hduser@MyPC:~/hive$ bin/hiveserver2
~~~
> <img width="28" height="25" alt="o5" src="https://github.com/user-attachments/assets/0ef39d71-d3a0-4088-99d1-0d2861a016df" /> Self-check: <br>
> HiveServer2 web UI - http://localhost:10002




### 2. To stop all services, e.g. at the end of every practical.

> [!NOTE]
> **Session 2**

Use Ctrl-c to stop HiveServer2
~~~bash
hduser@MyPC:~/hive$ jps
hduser@MyPC:~/hive$ cd ~
hduser@MyPC:~$
~~~

Stop the Thrift service using the identified pid
~~~bash
hduser@MyPC:~$ ps -aux | grep 9090
hduser    9441  1.5  3.1 2928716 152960 pts/2  Sl   07:46   0:05
hduser@MyPC:~$ kill 9441
hduser@MyPC:~$ jps
~~~

Stop the Hbase and ZooKeeper services.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ ~/hbase/bin/stop-hbase.sh
hduser@MyPC:~$ ~/hbase/bin/hbase-daemon.sh stop zookeeper
hduser@MyPC:~$ jps
~~~


> [!NOTE]
> **Session 1**
Use Ctrl-c to stop Kafka
~~~bash
hduser@MyPC:~$ 
hduser@MyPC:~$ jps
~~~
> Optionally, use the following command to stop Kafka in Session 2.
> ~~~bash
> hduser@MyPC:~$ cd ~/kafka
> hduser@MyPC:~$ ~/kafka/bin/kafka-server-stop.sh
> hduser@MyPC:~$ jps
> ~~~

Stop the HTTPD service.
~~~bash
hduser@MyPC:~$ sudo systemctl stop apache2
hduser@MyPC:~$ sudo systemctl status apache2
hduser@MyPC:~$ cd ~/hadoop3
hduser@MyPC:~/hadoop3$ bin/yarn --daemon stop timelineserver
hduser@MyPC:~/hadoop3$ jps
~~~

Stop the YARN and HDFS services.
~~~bash
hduser@MyPC:~/hadoop3$ sbin/stop-yarn.sh
hduser@MyPC:~/hadoop3$ sbin/stop-dfs.sh
hduser@MyPC:~/hadoop3$ jps
hduser@MyPC:~/hadoop3$ cd ~
hduser@MyPC:~$ exit
~~~

-----------------------------------------------------------


## References:
https://learn.microsoft.com/en-us/windows/wsl/
https://ubuntu.com/
https://hadoop.apache.org/
https://openjdk.org/
https://spark.apache.org/
https://www.scala-lang.org/
https://kafka.apache.org/
https://hbase.apache.org/
https://happybase.readthedocs.io/
https://thrift.apache.org/
https://hive.apache.org/
https://db.apache.org/derby/
https://jupyter.org/
https://www.python.org/


https://www.wikipedia.org/
https://www.tablesgenerator.com/
https://www.kaggle.com/datasets/moxxis/harry-potter-lstm
https://linuxiac.com/windows-subsystem-for-linux-explained-wsl-wsl2/
https://web.facebook.com/groups/1073126727485389/posts/1624393212358735


