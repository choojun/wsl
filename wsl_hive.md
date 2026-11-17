![hive](https://github.com/choojun/choojun.github.io/assets/6356054/18bc2a47-52bc-4e0c-a0c2-5c373b9db3d3)

# M. Hive with Tez and MySQL [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

Let's recap what we have learned so far. We have completed the setup for both [Apache Spark](wsl_spark.md) and [Hadoop MapReduce](wsl_hdfs.md), which are two distinct Big Data frameworks. The former is a high-performance in-memory data-processing engine, while the latter is a mature batch-processing platform operating at petabyte scale. Note that **Apache Hive** and [Apache HBase](wsl_hbase.md) serve very different purposes. Apache Hive is a distributed data warehouse system providing a SQL-like interface for MapReduce jobs, whereas [Apache HBase](wsl_hbase.md) is a distributed NoSQL key-value database running on [Hadoop](wsl_hadoop.md).

Specifically, Apache Hive is a distributed, fault-tolerant data warehouse system enabling large-scale analytics. It facilitates reading, writing, and managing petabytes of data residing in distributed storage using SQL. Read more on Hive at URL https://cwiki.apache.org/confluence/display/Hive/GettingStarted , https://cwiki.apache.org/confluence/display/Hive/Home , https://hive.apache.org/docs/latest/introduction-to-apache-hive/ , https://hive.apache.org/docs/latest/user/hiveserver2-overview/ ,  https://hive.apache.org/development/designdocs/design/ , https://hive.apache.org/docs/latest/language/languagemanual/ , https://hive.apache.org/docs/latest/user/hive-transactions/ , https://hive.apache.org/docs/latest/language/languagemanual-ddl/ , https://hive.apache.org/docs/latest/admin/replication/

## M1. Install and Configure Hive [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login as **hduser**. Ensure that **ALL SERVICES ARE STOPPED**, and check it by using the jps command before download and install Hive.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ jps
hduser@MyPC:~$ wget https://archive.apache.org/dist/hive/hive-4.1.0/apache-hive-4.1.0-bin.tar.gz
hduser@MyPC:~$ tar -xvzf apache-hive-4.1.0-bin.tar.gz
hduser@MyPC:~$ mv apache-hive-4.1.0-bin hive
~~~

2. Edit the file ~/.bashrc with the the following lines.
~~~bash
export HADOOP_MAPRED_HOME=/home/hduser/hadoop3
export HADOOP_COMMON_HOME=/home/hduser/hadoop3
export HADOOP_HDFS_HOME=/home/hduser/hadoop3
export YARN_HOME=/home/hduser/hadoop3
export HIVE_HOME=/home/hduser/hive
export PATH=$PATH:$HIVE_HOME/bin
export HIVE_CONF_DIR=/home/hduser/hive/conf
export HADOOP_CLASSPATH=/home/hduser/hadoop3/share/hadoop/common/*:/home/hduser/hadoop3/share/hadoop/common/lib/*:/home/hduser/hadoop3/share/hadoop/client/*:/home/hduser/hadoop3/share/hadoop/hdfs/lib/*:/home/hduser/hadoop3/share/hadoop/hdfs/*:/home/hduser/hadoop3/share/hadoop/tools/lib/*:/home/hduser/hadoop3/share/hadoop/mapreduce/*:/home/hduser/hadoop3/share/hadoop/yarn/*:/home/hduser/hadoop3/share/hadoop/yarn/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/*
export HIVE_CLASSPATH=/home/hduser/hive/lib/*
~~~

3. Re-load the environment.
~~~bash
hduser@MyPC:~$ source ~/.bashrc
~~~

4. Duplicate for the file ~/hive/conf/hive-site.xml 
~~~bash
hduser@MyPC:~$ cd ~/hive
hduser@MyPC:~/hive$ cp ~/hive/conf/hive-default.xml.template ~/hive/conf/hive-site.xml
~~~

5. Edit the file ~/hive/conf/hive-site.xml 
* Replace all occurrences of ${system:java.io.tmpdir} to /tmp/hive and this location is the new location for Hive storing all its temporary files.
* Replace all occurrences of ${system:user.name} to ${user.name} which should be the user name you log in with
* Replace all occurrences of /user/hive tp /user/hduser
> You may want to use the nano's search (Ctrl-w with Enter) to find the targeted keyword, and replace them one by one.

6. Edit the file ~/hive/bin/hive-config.sh with the the following lines 
~~~bash
export HADOOP_HOME=/home/hduser/hadoop3
export SPARK_HOME=/home/hduser/spark
export HBASE_HOME=/homehduser/hbase
export HADOOP_MAPRED_HOME=/home/hduser/hadoop3
export HADOOP_COMMON_HOME=/home/hduser/hadoop3
export HADOOP_HDFS_HOME=/home/hduser/hadoop3
export YARN_HOME=/home/hduser/hadoop3
export HIVE_HOME=/home/hduser/hive
export HIVE_CONF_DIR=/home/hduser/hive/conf
export HADOOP_CLASSPATH=/home/hduser/hadoop3/share/hadoop/common/*:/home/hduser/hadoop3/share/hadoop/common/lib/*:/home/hduser/hadoop3/share/hadoop/client/*:/home/hduser/hadoop3/share/hadoop/hdfs/lib/*:/home/hduser/hadoop3/share/hadoop/hdfs/*:/home/hduser/hadoop3/share/hadoop/tools/lib/*:/home/hduser/hadoop3/share/hadoop/mapreduce/*:/home/hduser/hadoop3/share/hadoop/yarn/*:/home/hduser/hadoop3/share/hadoop/yarn/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/*
export HIVE_CLASSPATH=/home/hduser/hive/lib/*
~~~

7. Duplicate for the file ~/hive/conf/hive-env.sh 
~~~bash
hduser@MyPC:~$ cd ~/hive
hduser@MyPC:~$ cp ~/hive/conf/hive-env.sh.template ~/hive/conf/hive-env.sh
~~~

8. Edit the file ~/hive/conf/hive-env.sh with the the following lines 
~~~bash
export HADOOP_HOME=/home/hduser/hadoop3
export SPARK_HOME=/home/hduser/spark
export HBASE_HOME=/homehduser/hbase
export HADOOP_MAPRED_HOME=/home/hduser/hadoop3
export HADOOP_COMMON_HOME=/home/hduser/hadoop3
export HADOOP_HDFS_HOME=/home/hduser/hadoop3
export YARN_HOME=/home/hduser/hadoop3
export HIVE_HOME=/home/hduser/hive
export HIVE_CONF_DIR=/home/hduser/hive/conf
export HADOOP_CLASSPATH=/home/hduser/hadoop3/share/hadoop/common/*:/home/hduser/hadoop3/share/hadoop/common/lib/*:/home/hduser/hadoop3/share/hadoop/client/*:/home/hduser/hadoop3/share/hadoop/hdfs/lib/*:/home/hduser/hadoop3/share/hadoop/hdfs/*:/home/hduser/hadoop3/share/hadoop/tools/lib/*:/home/hduser/hadoop3/share/hadoop/mapreduce/*:/home/hduser/hadoop3/share/hadoop/yarn/*:/home/hduser/hadoop3/share/hadoop/yarn/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/*:/home/hduser/hadoop3/share/hadoop/yarn/timelineservice/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/lib/*:/home/hduser/hadoop3/share/hadoop/yarn/csi/*
export HIVE_CLASSPATH=/home/hduser/hive/lib/*
~~~

9. Start both DFS and YARN services before create/alter those required Hive directories in the HDFS. 
~~~bash
hduser@MyPC:~$ jps
hduser@MyPC:~$ cd ~/hadoop3
hduser@MyPC:~/hadoop3$ sbin/start-dfs.sh
hduser@MyPC:~/hadoop3$ sbin/start-yarn.sh
hduser@MyPC:~/hadoop3$ jps
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /tmp
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /tmp/hduser
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /user
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /user/hduser
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /user/hduser/warehouse
hduser@MyPC:~/hadoop3$ hdfs dfs -mkdir /user/hduser/lib
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod g+w /tmp
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod g+w /tmp/hduser
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod 777 /user
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod g+w /user/hduser
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod -R 775 /user/hduser/warehouse
hduser@MyPC:~/hadoop3$ hdfs dfs -chmod 777 /user/hduser/lib
~~~

10. Change mode of access for hadoop's data and namenode, which are created in [Section E](wsl_hdoop.md). **Attention**: Stop both DFS and YARN services after this step.
~~~bash
hduser@MyPC:~$ chmod -R g+w /home/hduser/hadoopData
hduser@MyPC:~$ chmod -R g+w /home/hduser/hadoopName
hduser@MyPC:~$ jps
hduser@MyPC:~$ cd ~/hadoop3
hduser@MyPC:~/hadoop3$ sbin/stop-yarn.sh
hduser@MyPC:~/hadoop3$ sbin/stop-dfs.sh
hduser@MyPC:~/hadoop3$ jps
~~~

11. Edit the ~/hadoop3/etc/hadoop/hadoop-env.sh file by including additional paths into the HADOOP_CLASSPATH as follows
~~~bash
export HADOOP_CLASSPATH=/usr/lib/jvm/java-17-openjdk-amd64/lib/tools.jar:/home/hduser/hive/lib/*:/home/hduser/hadoop3/share/hadoop/common/*:/home/hduser/hadoop3/share/hadoop/common/lib/*:/home/hduser/hadoop3/share/hadoop/client/*
~~~

12. Find the targeted jar file. Delete the log4j-slf4j-impl-2.6.2.jar file if found multiple copies (optional)
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ find . -name log4j-slf4j-impl-*.jar
hduser@MyPC:~$ rm ~/hive/lib/log4j-slf4j-impl-2.24.3.jar
~~~
> We delete the file log4j-slf4j-impl-2.24.3.jar because the similar file is also presented in the Hadoop directory, and it gives error to us occasionally

## M2. Install and Configure MySQL with JDBC Driver [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Install MySQL Server, and verify that the service is up and running:
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ sudo apt update
hduser@MyPC:~$ sudo apt install mysql-server
hduser@MyPC:~$ sudo systemctl status mysql
~~~
> Exit the status checking using Ctrl-c.

2. Download the MySQL JDBC Driver at URL https://dev.mysql.com/downloads/connector/j/ . Choose **Ubuntu Linux** from the Operating System dropdown, select our installed Ubuntu version **24.04**, and download the .deb file (click "No thanks" to skip Oracle login). Assuming you have downloaded **mysql-connector-j_26.10.0-1ubuntu24.04_all.deb** , execute the following commands.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ sudo cp -r /mnt/c/de/mysql-connector-j_26.10.0-1ubuntu24.04_all.deb /home/hduser
hduser@MyPC:~$ ls -al
hduser@MyPC:~$ sudo chown hduser:hduser -R /home/hduser/mysql-connector-j_26.10.0-1ubuntu24.04_all.deb
hduser@MyPC:~$ ls -al
hduser@MyPC:~$ sudo dpkg -i mysql-connector-j_*.deb
hduser@MyPC:~$ sudo apt install mysql-connector-j
~~~

3. Access the MySQL Shell, and create a dedicated username (**admin**), password (**password**) and new database metastore_db before grant permissions to the user **admin**.
~~~bash
hduser@MyPC:~$ sudo mysql
mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
mysql> CREATE DATABASE metastore_db;
mysql> GRANT ALL PRIVILEGES ON metastore_db.* TO 'admin'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> EXIT;
~~~

4. Test the new created credentials before next step.
~~~bash
hduser@MyPC:~$ mysql -u admin -p
mysql> SHOW DATABASES;
mysql> use metastore_db;
mysql> show tables;
mysql> EXIT;
~~~

5. Configure the Hive to use MySQL by changing the following property values in file ~/hive/conf/hive-site.xml
~~~xml
    <property>
      <name>javax.jdo.option.ConnectionURL</name>
      <value>jdbc:mysql://localhost:3306/metastore_db?createDatabaseIfNotExist=true</value>
      <description>JDBC connect string for a JDBC metastore</description>
    </property>
    <property>
      <name>javax.jdo.option.ConnectionDriverName</name>
      <value>com.mysql.cj.jdbc.Driver</value>
      <description>Driver class name for a JDBC metastore</description>
    </property>
    <property>
      <name>javax.jdo.option.ConnectionPassword</name>
      <value>password</value>
    </property>
    <property>
      <name>javax.jdo.option.ConnectionUserName</name>
      <value>admin</value>
    </property>
    <property>
      <name>hive.exec.local.scratchdir</name>
      <value>/tmp/hive/${user.name}</value>
      <description>Local scratch space for Hive jobs</description>
    </property>
    <property>
      <name>hive.downloaded.resources.dir</name>
      <value>/tmp/hive/${hive.session.id}_resources</value>
      <description>Temporary local directory for added resources in the remote file system.</description>
    </property>
    <property>
      <name>hive.querylog.location</name>
      <value>/tmp/hive/${user.name}</value>
      <description>Location of Hive run time structured log file</description>
    </property>
    <property>
      <name>hive.server2.logging.operation.log.location</name>
      <value>/tmp/hive/${user.name}/operation_logs</value>
      <description>Top level directory where operation logs are stored if logging functionality is >
    </property>
    <property>
      <name>hive.downloaded.resources.dir</name>
      <value>/tmp/hive/${hive.session.id}_resources</value>
      <description>Temporary local directory for added resources in the remote file system</description>
    </property>
    <property>
      <name>hive.external.table.purge.default</name>
      <value>true</value>
    </property>
    <property>
      <name>hive.metastore.schema.verification</name>
      <value>false</value>
    </property>
~~~

6. To allow Hive to connect to MySQL (metastore_db) through JDBC, add the following lines to the file ~/hadoop3/etc/hadoop/core-site.xml of your Hadoop installation. **Warning: Note that your Hive and other services SHOULD NOT running at this step.**
 ~~~xml
 <configuration>
     <property>
         <name>hadoop.proxyuser.hduser.hosts</name>
         <value>*</value>
     </property>
     <property>
         <name>hadoop.proxyuser.hduser.groups</name>
         <value>*</value>
     </property>
 </configuration>
 ~~~


7. To allow PySpark to connect to hive cluster, duplicate (by overwriting) the following files to destination Spark
~~~bash
hduser@MyPC:~$ cp -f ~/hadoop3/etc/hadoop/core-site.xml ~/spark/conf/
hduser@MyPC:~$ cp -f ~/hadoop3/etc/hadoop/hdfs-site.xml ~/spark/conf/
hduser@MyPC:~$ cp -f ~/hive/conf/hive-site.xml ~/spark/conf/

hduser@MyPC:~$ cp -f /usr/share/java/mysql-connector-j-26.10.0.jar ~/spark/jars/
hduser@MyPC:~$ cp -f /usr/share/java/mysql-connector-j-26.10.0.jar ~/hive/lib/
~~~
> **Attention**: ensure Hadoop, Spark, HBase and Hive are successfully installed **BEFORE** proceeding with this step. **You need to redo this step if ANY CHANGES on the involved their files in nearly future.**

8. Edit the file ~/.bashrc with the the following lines
~~~bash
export CLASSPATH=$CLASSPATH:/usr/share/java/mysql-connector-j-26.10.0.jar
~~~
> Remember to issue source ~/.bashrc after saving the file.

9. Use existing session (named as **session 1**) to ensure the MySQL is running and start **HDFS**, **YARN**, **Kafka**, **HBase** and **Thrift** services.
> **Tips**: Note that a total of eleven (11) services can be observed eventually.
> ~~~bash
> hduser@MyPC:~$ sudo systemctl status mysql
> hduser@MyPC:~$
> hduser@MyPC:~$ cd ~/hadoop3
> hduser@MyPC:~/hadoop3$ sbin/start-dfs.sh
> hduser@MyPC:~/hadoop3$ sbin/start-yarn.sh
> hduser@MyPC:~/hadoop3$ jps
> hduser@MyPC:~/hadoop3$ cd ~
> hduser@MyPC:~$ cd ~/kafka
> hduser@MyPC:~/kafka$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
> hduser@MyPC:~/kafka$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
> hduser@MyPC:~/kafka$ bin/kafka-server-start.sh config/server.properties
> hduser@MyPC:~/kafka$ jps
> hduser@MyPC:~/kafka$ cd ~
> hduser@MyPC:~$ cd ~/hbase
> hduser@MyPC:~/hbase$ ~/hbase/bin/hbase-daemon.sh start zookeeper
> hduser@MyPC:~/hbase$ ~/hbase/bin/start-hbase.sh
> hduser@MyPC:~/hbase$ jps
> hduser@MyPC:~/hbase$ bin/hbase thrift start -p 9090 &
> hduser@MyPC:~/hbase$ jps
> hduser@MyPC:~/hbase$ cd ~
> hduser@MyPC:~$
> ~~~

10. Use the **session 1** to run the following command to initialize MySQL as the Metastore database for Hive. It might take a few minutes. Please be patient while you wait for its completion
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ java -cp home/hduser/hive/lib/*:/home/hduser/spark/jars/* org.apache.hive.beeline.HiveSchemaTool -initSchemaTo 4.1.0 -dbType mysql
~~~
> **Attention**: Note that in the setup of Hive 4.1.0, you may have corrupted characters in file ~/hive/conf/hive-site.xml, which is inherited from its template (duplicated in Section M1), particularlly under the description of 'hive.txn.xlock.iow'. Just delete it if there is an error, and re-run above command.


## M3. Install and Configure Tez [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Use the **session 1** to install and configure Tez.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ wget https://archive.apache.org/dist/tez/0.10.5/apache-tez-0.10.5-bin.tar.gz
hduser@MyPC:~$ tar -xzf apache-tez-0.10.5-bin.tar.gz
hduser@MyPC:~$ mv apache-tez-0.10.5-bin tez 
~~~

2. Make a directory named tez, and copy the necessary files into the HDFS file system.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ hdfs dfs -mkdir tez
hduser@MyPC:~$ hdfs dfs -put -f /home/hduser/tez/* /user/hduser/tez
hduser@MyPC:~$ hdfs dfs -put /home/hduser/hive/lib/hive-exec-4.1.0.jar /user/hduser/tez
hduser@MyPC:~$ ?? rm ~/tez/lib/slf4j-reload4j-1.7.36.jar
~~~

3. In ~/.bashrc file, add the following lines at the end of the file.
~~~bash
export TEZ_HOME=/home/hduser/tez
export TEZ_CONF_DIR=/home/hduser/tez/conf
export TEZ_JARS=/home/hduser/tez
if [ -z "$HIVE_AUX_JARS_PATH" ]; then
    export HIVE_AUX_JARS_PATH="$TEZ_JARS"
else
    export HIVE_AUX_JARS_PATH="$HIVE_AUX_JARS_PATH:$TEZ_JARS"
fi
export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$TEZ_CONF_DIR:$TEZ_JARS/*:$TEZ_JARS/lib/*
~~~


4. Create file /home/hduser/tez/conf/tez-site.xml, and add the following lines.
~~~bash
<configuration>
    <property>
        <name>tez.lib.uris</name>
        <value>hdfs:///user/hduser/tez/share/tez.tar.gz</value>
    </property>
    <property>
        <name>tez.use.cluster.hadoop-libs</name>
        <value>true</value>
    </property>
    <property>
        <name>tez.history.logging.service.class</name>
        <value>org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService</value>
    </property>
    <property>
        <name>tez.tez-ui.history-url.base</name>
        <value>http://localhost:9999/tez-ui/</value>
    </property>
</configuration>
~~~

5. Edit the file ~/hive/conf/hive-site.xml
~~~bash
   <property>
       <name>hive.execution.engine</name>
       <value>tez</value>
   </property>
   <property>
       <name>hive.tez.container.size</name>
       <value>4096</value>
   </property>
   <property>
       <name>hive.tez.java.opts</name>
       <value>-Xmx3072m</value>
   </property>
   <property>
       <name>hive.tez.cpu.vcores</name>
       <value>1</value>
   </property>

   <property>
       <name>tez.lib.uris</name>
       <value>hdfs:///user/hduser/tez/share/tez.tar.gz</value>
   </property>
~~~

6. Download, extract the Apache Tomcat and locate the required war for Tez.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ wget https://archive.apache.org/dist/tomcat/tomcat-11/v11.0.29/bin/apache-tomcat-11.0.29.tar.gz
hduser@MyPC:~$ tar -xzf apache-tomcat-11.0.29.tar.gz
hduser@MyPC:~$ mv apache-tomcat-11.0.29 tomcat
hduser@MyPC:~$ chown -R hduser:hduser ~/tomcat
hduser@MyPC:~$ chmod -R g+r ~/tomcat
hduser@MyPC:~$ chmod g+x ~/tomcat
hduser@MyPC:~$ cd ~/tomcat/webapps
hduser@MyPC:~$ wget https://repository.apache.org/content/repositories/releases/org/apache/tez/tez-ui/0.10.5/tez-ui-0.10.5.war
hduser@MyPC:~$ cd ~
~~~

6. Start the Apache Tomcat.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ cd tomcat
hduser@MyPC:~$ bin/startup.sh
hduser@MyPC:~$ jps
~~~
> Note that a total of twelve (12) services, i.e. Bootstrap is newly added, can be observed eventually.
>
> To stop the Tomcat, issue command bin/shutdown.sh.

## M4. Running HiveServer2 and Beeline [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. HiveServer2 (HS2) is a service that enables clients to execute queries against Hive. HS2 supports multi-client concurrency and authentication. It is designed to provide better support for open API clients like JDBC and ODBC. Read more on HiveServer2 at URL https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview

2. HiveServer2 supports a command shell Beeline that works with HiveServer2. It's a JDBC client that is based on the SQLLine CLI (http://sqlline.sourceforge.net/). Read more on Beeline at URL https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients

3. Assume other necessary services have been executed in the **session 1**, those from M1, M2 and M3.

4. Use the shell **session 1**, and run the Hive over there. Leave the session running and DO NOT CLOSE the session after the execution of following command. 
~~~bash
hduser@MyPC:~$ cd ~/hive
hduser@MyPC:~/hive$ cp ~/hbase/lib/client-facing-thirdparty/opentelemetry-semconv-1.29.0-alpha.jar  ~/hbase/lib
hduser@MyPC:~/hive$ cd ~/hive/lib
hduser@MyPC:~/hive/lib$ rm log4j-slf4j-impl-2.24.3.jar
hduser@MyPC:~/hive/lib$ wget https://repo1.maven.org/maven2/org/apache/tez/tez-mapreduce/0.10.5/tez-mapreduce-0.10.5.jar
hduser@MyPC:~/hive/lib$ wget https://repo1.maven.org/maven2/org/apache/tez/tez-runtime-library/0.10.5/tez-runtime-library-0.10.5.jar
hduser@MyPC:~/hive/lib$ wget https://repo1.maven.org/maven2/org/apache/tez/tez-dag/0.10.5/tez-dag-0.10.5.jar
hduser@MyPC:~/hive/lib$ wget https://repo1.maven.org/maven2/org/apache/tez/tez-common/0.10.5/tez-common-0.10.5.jar
hduser@MyPC:~/hive/lib$ cd ~/hive
hduser@MyPC:~/hive$ bin/hiveserver2
~~~
> To stop the Hive, use Ctrl-C.
>
> To access the WebUI, visit http://localhost:10002/

5. Use a new shell **session 2**. Ensure that one additional service from HiveServer2 (i.e., the RunJar process) is visible when using the jps command before launching and logging into the Beeline shell using your MySQL credentials. 
~~~bash
hduser@MyPC:~$ jps
hduser@MyPC:~$ cd ~/hive
hduser@MyPC:~/hive$ bin/beeline
Beeline version 4.1.0 by Apache Hive
beeline> !connect jdbc:hive2://
Connecting to jdbc:hive2://
Enter username for jdbc:hive2://: admin
Enter password for jdbc:hive2://: ********
Hive Session ID = ae91436a-bdad-431b-afd7-440e9fe20cdb
Connected to: Apache Hive (version 4.1.0)
Driver: Hive JDBC (version 4.1.0)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://>
~~~
> To stop the Beeline, use either command !q (after login) or Ctrl-c (before login).
> 
> Note that we always need to terminate the running RunJar service/s (if any) BEFORE re-run the HiveServer2.

## M5. Quick start with Hive [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Create a new database
~~~bash
0: jdbc:hive2://> show databases;
0: jdbc:hive2://> create database choojunhive;
0: jdbc:hive2://> show databases;
~~~

2. Create a new table
~~~bash
0: jdbc:hive2://> CREATE TABLE IF NOT EXISTS choojunhive.employee (id int, name string, age int, gender string) COMMENT 'Employee Table' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
0: jdbc:hive2://> DESCRIBE choojunhive.employee;
~~~

3. Insert and retrive records 
~~~bash
0: jdbc:hive2://> INSERT INTO choojunhive.employee VALUES (1,'Ahmad',19,'M');
0: jdbc:hive2://> INSERT INTO choojunhive.employee VALUES (2,'Baba',20,'M');
0: jdbc:hive2://> INSERT INTO choojunhive.employee VALUES (3,'Chong',21,'M');
0: jdbc:hive2://> select * from choojunhive.employee;
~~~

4. Drop created table and database. 
~~~bash
0: jdbc:hive2://> DROP TABLE choojunhive.employee;
0: jdbc:hive2://> DROP DATABASE choojunhive;
0: jdbc:hive2://> show databases;
~~~
> c
> 
> Note that we always need to terminate the running RunJar service/s (if any) BEFORE re-run the HiveServer2.

5. Try out the Guided Tutorials as follows
   * https://cwiki.apache.org/confluence/display/hive/tutorial
   * https://www.simplilearn.com/tutorials/hadoop-tutorial/hive
