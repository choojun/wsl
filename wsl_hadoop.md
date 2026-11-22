![hadoop](https://github.com/choojun/choojun.github.io/assets/6356054/0233d690-e03c-4699-a0e9-e9f932139de3)

# E. Hadoop [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()
Hadoop is an open-source software framework for the distributed storage and parallel processing of massive datasets across clusters of computers

1. Throughout our practical, we will assume that the Hadoop user name is **hduser**.
2. The first time that you launch your WSL Linux distro, you will be prompted to create a default user account. You may choose to either 
    * name the default user account as tarumt, and 
    * create a separate user account named hduser.
3. The **NameNode** is the hardware that contains the GNU/Linux operating system and software. The Hadoop distributed file system acts as the master server and can manage the files, control a client's access to files, and overseas file operating processes such as renaming, opening, and closing files. A **DataNode** is hardware having the GNU/Linux operating system and DataNode software. For every node in a HDFS cluster, you will locate a DataNode. These nodes help to control the data storage of their system as they can perform operations on the file systems if the client requests, and also create, replicate, and block files when the NameNode instructs.   ![hdfsarchitecture-image](https://github.com/choojun/choojun.github.io/assets/6356054/347b07e8-385f-416d-9371-e43407251f74)
4. The HDFS file system consists of a set of Master services (NameNode, secondary NameNode, and DataNodes). The **NameNode** and **secondary NameNode** manage the HDFS metadata. The **DataNodes** host the underlying HDFS data. The **NameNode** tracks which DataNodes contain the contents of a given file in HDFS. HDFS divides files into blocks and stores each block on a DataNode. Multiple DataNodes are linked to the cluster. The NameNode then distributes replicas of these data blocks across the cluster. It also instructs the user or application where to locate wanted information.
5. Read more on Hadoop at URL https://en.wikipedia.org/wiki/Apache_Hadoop and https://hadoop.apache.org/

## E1. Setup User Environment [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login with user **tarumt**, and create a new group named hadoop
   ~~~bash
   tarumt@MyPC:~$ cd ~
   tarumt@MyPC:~$ sudo addgroup hadoop
   ~~~

2.	Create a new user account named hduser (if applicable)
Add the new user:
   ~~~bash
   tarumt@MyPC:~$ sudo adduser hduser
   tarumt@MyPC:~$ sudo adduser student
   ~~~

3. Grant the user sudo privileges and set its home directory
   ~~~bash
   tarumt@MyPC:~$ sudo usermod -aG sudo hduser
   tarumt@MyPC:~$ sudo usermod -d /home/hduser -m -s /bin/bash hduser
   tarumt@MyPC:~$ sudo usermod -aG sudo student
   tarumt@MyPC:~$ sudo usermod -d /home/student -m -s /bin/bash student
   ~~~

4.	Add hduser to the hadoop group
   ~~~bash
   tarumt@MyPC:~$ sudo usermod -a -G hadoop hduser
   tarumt@MyPC:~$ sudo usermod -a -G hadoop student
   ~~~

5.	Switch to the user account hduser (if applicable)
   ~~~bash
   tarumt@MyPC:~$ su - hduser
   hduser@MyPC:~$ exit
   tarumt@MyPC:~$ su - student
   student@MyPC:~$ exit
   ~~~
   > If you want to go back to your original user session
   ~~~bash
   $ exit
   ~~~

## E2. Setup Operating System Environment [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Reboot/terminate Ubuntu in WSL, and run the following commands from Ubuntu with user **hduser**

2. Check if ssh has been installed
   ~~~bash
   hduser@MyPC:~$ service ssh status
   ~~~
   > Ctrl-C to terminate the examination of ssh status.

3. If ssh has not been installed, install ssh before examining its status
   ~~~bash
   hduser@MyPC:~$ sudo apt update
   hduser@MyPC:~$ sudo apt upgrade
   hduser@MyPC:~$ sudo apt install ssh
   hduser@MyPC:~$ service ssh status
   ~~~
   > Ctrl-C to terminate the examination of ssh status.
   > Test the ssh to localhost for created user, e.g. **tarumt**, **hduser** and **student**
   > ~~~bash
   > $ ssh localhost
   > ~~~
   > Issue the following command to exit from the test.
   > ~~~bash
   > $ exit
   > ~~~

4. Install pdsh
   ~~~bash
   hduser@MyPC:~$ sudo apt update && sudo apt install pdsh
   ~~~

5. Install Python (if necessary)
   ~~~bash
   hduser@MyPC:~$ sudo apt update
   hduser@MyPC:~$ python3 --version 
   hduser@MyPC:~$ sudo apt install software-properties-common
   hduser@MyPC:~$ sudo apt install python3 python3-dev python3-wheel python3-full
   ~~~

6. Check current python versions and symlinks
   ~~~bash
   hduser@MyPC:~$ ls -l /usr/bin/python* 
   ~~~
   > Ensure that links are pointed to targeted version of Python as Step 5.

7. Set environment variables by editing your ~/.bashrc file (for **hduser**):
   ~~~bash
   hduser@MyPC:~$ nano ~/.bashrc
   ~~~

8. In ~/.bashrc file, set Python 3 as the default python version, add the following command to set Python 3 as the default python version:
   ~~~bash
   alias python=python3
   ~~~
> Ctrl-x to save after edited the file.

9. In ~/.bashrc file, add the following lines at the end of the file based on the python3.x from your installation (e.g. Ubuntu 24.04 coming with Python 3.12):
   ~~~bash
   export CPATH=/usr/include/python3.12:$CPATH
   export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH
   ~~~
   > Ctrl-x to save after edited the file.

10. Source the file:
    ~~~bash
    hduser@MyPC:~$ source ~/.bashrc
    ~~~

11. Install pip or upgrade pip (if necessary)
    ~~~bash
    hduser@MyPC:~$ sudo apt update && sudo apt install python3-pip
    hduser@MyPC:~$ pip3 --version
    ~~~~

12. Check which Java version is installed in the distro
    ~~~bash
    hduser@MyPC:~$ java -version
    ~~~

13. Install targeted OpenJDK
    ~~~bash
    hduser@MyPC:~$ sudo apt update && sudo apt-get install openjdk-17-jdk
    hduser@MyPC:~$ java -version
    ~~~
    > After this, remember to check if the correct version of Java is installed.





## E3. Setup SSH and PDSH [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

Run the following commands from Ubuntu with user **hduser**
> Secure Shell (SSH), also sometimes called Secure Socket Shell, is a protocol for securely accessing your site’s server over an unsecured network. In other words, it’s a way to safely log in to your server remotely using your preferred command-line interface.

1. Check if the SSH service is running
   ~~~bash
   hduser@MyPC:~$ service ssh status
   ~~~
   > Ctrl-C to terminate the examination of ssh status.

2. Start SSH
   ~~~bash
   hduser@MyPC:~$ sudo service ssh start
   ~~~
   > Note that WSL does not automatic start sshd (SSH daemon) occasionally. Please start the sshd manually

3. Install the ufw and open the SSH port (if necessary)
   ~~~bash
   hduser@MyPC:~$ sudo apt update && sudo apt install ufw
   hduser@MyPC:~$ sudo ufw allow ssh
   ~~~
   > Ubuntu comes with a firewall configuration tool, known as UFW. If the firewall is enabled on your system, make sure to open the targeted SSH port, i.e. port 22.

4. Reload SSH
   ~~~bash
   hduser@MyPC:~$ sudo /etc/init.d/ssh reload
   ~~~

5. Modify pdsh’s default rcmd to ssh, by checking your pdsh default rcmd rsh:
   ~~~bash
   hduser@MyPC:~$ pdsh -q -w localhost
   ~~~

6. Modify pdsh’s default rcmd to ssh, **by adding** the following command to **~/.bashrc** file (for **hduser**)
   ~~~bash
   export PDSH_RCMD_TYPE=ssh
   ~~~
   > Remember to save the edited file by ctrl-x.

7. Run the following command to ensure the settings applied.
   ~~~bash
   hduser@MyPC:~$ source ~/.bashrc
   ~~~



## E4. Disable IPv6 [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

Run the following commands from Ubuntu with user **hduser**

1. Edit the /etc/sysctl.conf file with the following command.
   ~~~bash
   hduser@MyPC:~$ sudo nano /etc/sysctl.conf
   ~~~

2. Add the following lines to the end of the sysctl.conf file:
   ~~~bash
   # disable ipv6
   net.ipv6.conf.all.disable_ipv6 = 1
   net.ipv6.conf.default.disable_ipv6 = 1
   net.ipv6.conf.lo.disable_ipv6 = 1
   ~~~
   > Remember to save the edited file by ctrl-x.

3. To reload the /etc/sysctl.conf settings, issue the following command.
   ~~~bash
   hduser@MyPC:~$ sudo sysctl -p
   ~~~

4. Check if IPv6 has been successfully disabled
   ~~~bash
   hduser@MyPC:~$ cat /proc/sys/net/ipv6/conf/all/disable_ipv6
   ~~~
   > 0 means IPv6 is enabled; **1 means IPv6 is disabled**.

5. **Suppose that IPv6 is still enabled after rebooting**, you must carry out the following:

   - Create (with root privileges) the file /etc/rc.local 
     ~~~bash
     hduser@MyPC:~$ sudo nano /etc/rc.local
     ~~~
   - Insert the following into the file /etc/rc.local:
     ~~~bash
     #!/bin/bash
     /etc/sysctl.d
     /etc/init.d/procps restart
     exit 0
     ~~~
   - Make the file executable
     ~~~bash
     hduser@MyPC:~$ sudo chmod 755 /etc/rc.local
     ~~~


## E5. Install Hadoop [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Switch to the **hduser** account

2. Download the Hadoop binary by finding the appropriate Hadoop binary from the Hadoop releases page.
> We will use Hadoop 3.4.1 to avoid problems with HBase in a later practical. Read more at URL https://hbase.apache.org/book.html#hadoop
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ wget https://downloads.apache.org/hadoop/common/hadoop-3.4.3/hadoop-3.4.3.tar.gz
   ~~~
   > Or, you may copy the downloaded tar.gz file manually to destination ~/hduser/

3.	Untar the file
   ~~~bash
   hduser@MyPC:~$ tar -xvzf hadoop-3.4.3.tar.gz
   ~~~

4.	Rename the folder as hadoop3
   ~~~bash
   hduser@MyPC:~$ mv hadoop-3.4.3 hadoop3
   hduser@MyPC:~$ sudo chown -R hduser:hadoop hadoop3
   hduser@MyPC:~$ sudo chmod g+w -R hadoop3
   ~~~

## E6. Configure passphraseless ssh for Hadoop [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Ensure that you are login with the **hduser** 

2. Ensure that you can SSH to the localhost in Ubuntu, try
   > ~~~bash
   > $ ssh localhost
   > ~~~
   > Remember to issue the following command to exit after the above test.
   > ~~~bash
   > $ exit
   > ~~~

3. To ssh to localhost without a passphrase, run the following command to initialize your private and public keys:
   ~~~bash
   hduser@MyPC:~$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
   hduser@MyPC:~$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   hduser@MyPC:~$ chmod 0600 ~/.ssh/authorized_keys
   ~~~

4. Test the configuration
   ~~~bash
   hduser@MyPC:~$ ssh localhost
   ~~~
   > Remember to exit the ssh by issuing the following command.
   > ~~~bash
   > $ exit
   > ~~~

5. Repeat the same steps 1 to 4 for user **student**.

## E7. Configure Pseudo-distributed Mode for Hadoop [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Ensure that you are login with the **hduser** 

2. Setup the environment variables in the ~/.bashrc file (for hduser) by adding the environment variables to the end of the file
   ~~~bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   export HADOOP_HOME=/home/hduser/hadoop3
   export PATH=$PATH:$HADOOP_HOME/bin
   ~~~
   > Remember to save the edited file by ctrl-x.

3. Source the file:
   ~~~bash
   hduser@MyPC:~$ source ~/.bashrc
   ~~~

4. Change directory to the Hadoop folder
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ cd hadoop3
   ~~~

5. Edit the ~/hadoop3/etc/hadoop/hadoop-env.sh file by adding the following environment variables at the end of file
   ~~~bash
   # Add Java 17 compatibility opens flags for Hadoop
   export HADOOP_OPTS="$HADOOP_OPTS --add-opens=java.base/java.lang=ALL-UNNAMED"
   export HADOOP_OPTS="$HADOOP_OPTS --add-opens=java.base/java.util=ALL-UNNAMED"
   export HADOOP_OPTS="$HADOOP_OPTS --add-opens=java.base/java.io=ALL-UNNAMED"
   export HADOOP_OPTS="$HADOOP_OPTS --add-opens=java.base/java.net=ALL-UNNAMED"
   export HADOOP_OPTS="$HADOOP_OPTS --add-opens=java.base/java.util.concurrent=ALL-UNNAMED"

   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
   export HADOOP_LOG_DIR=${HADOOP_HOME}/logs
   ~~~
   > Remember to save the edited file by ctrl-x.

6. Verify if the installation was successful
   ~~~bash
   hduser@MyPC:~/hadoop3$ hadoop
   ~~~
   > Running the above command should display various options.

7. Edit the ~/hadoop3/etc/hadoop/core-site.xml file by adding the following configuration.
   ~~~xml
   <configuration>
       <property>
           <name>fs.defaultFS</name>
           <value>hdfs://localhost:9000</value>
       </property>
   </configuration>
   ~~~
   > Remember to save the edited file by ctrl-x.

8. Edit the ~/hadoop3/etc/hadoop/hdfs-site.xml file by adding the following configuration.
   ~~~xml
    <configuration>
       <property>
          <name>dfs.replication</name>
          <value>1</value>
       </property>
       <property>
          <name>dfs.datanode.data.dir</name>
          <value>/home/hduser/hadoopData/dfs/data</value>
          <final>true</final>
       </property>
       <property>
          <name>dfs.namenode.name.dir</name>
          <value>/home/hduser/hadoopName/dfs/data</value>
          <final>true</final>
       </property>
       <property>
          <name>dfs.webhdfs.enabled</name>
          <value>true</value>
       </property>
    </configuration>
   ~~~
   > Remember to save the edited file by ctrl-x.

9. Edit the ~/hadoop3/etc/hadoop/mapred-site.xml file by adding the following configuration.
   ~~~xml
    <configuration>
       <property>
          <name>mapreduce.framework.name</name>
          <value>yarn</value>
       </property>
       <property>  
          <name>mapreduce.application.classpath</name>      
          <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
       </property>
       <property>
          <name>mapreduce.map.java.opts</name>
          <value>-Xmx1024m --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED</value>
       </property>
       <property>
          <name>mapreduce.reduce.java.opts</name>
          <value>-Xmx1024m --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED</value>
       </property>
    </configuration>
   ~~~
   > Remember to save the edited file by ctrl-x.

10. Edit the ~/hadoop3/etc/hadoop/yarn-site.xml file by adding the following configuration.
    ~~~xml
    <configuration>
      <property>
         <name>yarn.nodemanager.aux-services</name>
         <value>mapreduce_shuffle</value>
      </property>
      <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
      </property>
      <property>
         <name>yarn.nodemanager.env-whitelist</name>    
         <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
      </property>
      <property>
         <name>yarn.resourcemanager.address</name>
         <value>127.0.0.1:8032</value>
      </property>
      <property>
         <name>yarn.log-aggregation.retain-seconds</name>
         <value>604800</value>
      </property>
    </configuration>
    ~~~
    > Remember to save the edited file by ctrl-x.

11. Edit the ~/hadoop3/etc/hadoop/yarn-env.sh file by adding the following configuration.
    ~~~bash
    # Force YARN to pass modular opens flags to its JVM instances
    export YARN_OPTS="$YARN_OPTS --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED"
    ~~~
    > Remember to save the edited file by ctrl-x.



12. Format the namenode 
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ ls
    hduser@MyPC:~$ ~/hadoop3/bin/hdfs namenode -format
    hduser@MyPC:~$ ls
    ~~~
    > Running the above command should display information on formating the namenode of Hadoop with installed Java. You should observe the namenode formated and **terminated without any error**. 

13. Start the Hadoop Distributed File System (DFS) services
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ ~/hadoop3/sbin/start-dfs.sh
    hduser@MyPC:~$ jps
    ~~~
    > Check the status. If the NameNode and DataNode services are initiated successfully, you should see these four processes
    > ~~~
    > Jps
    > DataNode
    > NameNode
    > SecondaryNameNode
    > ~~~
    > Browse any web browser for the NameNode, by default, and it is available at URL **http://localhost:9870/**

14. Start the Yet Another Resource Negotiator (YARN) service
    ~~~bash
    hduser@MyPC:~$ ~/hadoop3/sbin/start-yarn.sh
    hduser@MyPC:~$ jps
    ~~~
    > Check the status. If the Yarn services are initiated successfully, you should see a total of six processes (included these two).
    > ~~~
    > ResourceManager
    > NodeManager
    > ~~~
    > Browse any web browser for the ResourceManager, by default, and it is available at URL **http://localhost:8088/**

15. Create HDFS directories required to execute MapReduce jobs for all created users, e.g. hduser and student
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ hdfs dfs -mkdir /user
    hduser@MyPC:~$ hdfs dfs -mkdir /user/hduser
    hduser@MyPC:~$ hdfs dfs -mkdir /user/student
    ~~~

## E8. Run a sample MapReduce Job in Hadoop [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Ensure that you are login with the **hduser** 

2. Copy the input files into the distributed file system
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ hdfs dfs -mkdir input
   hduser@MyPC:~$ hdfs dfs -put etc/hadoop/*.xml input
   ~~~

3. Run a MapReduce job from an example
   ~~~bash
   hduser@MyPC:~$ ~/hadoop3/bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar grep input output 'dfs[a-z.]+'
   ~~~

4. View the output files on the distributed system
   ~~~bash
   hduser@MyPC:~$ hdfs dfs -cat output/*
   Output:
   1      dfsadmin
   1      dfs.replication
   1      dfs.namenode.name.dir
   1      dfs.datanode.data.dir
   ~~~

5. Stop all the daemons
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ ~/hadoop3/sbin/stop-yarn.sh
   hduser@MyPC:~$ ~/hadoop3/sbin/stop-dfs.sh
   hduser@MyPC:~$ jps
   ~~~

6. Logout from the hduser account and your tarumt account.



## E9. Attention: At the beginning of all future practical [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Login as **hduser** or switch account to **hduser**
   ~~~bash
   tarumt@MyPC:~$ su - hduser
   ~~~

2. Start ssh,
   ~~~bash
   hduser@MyPC:~$ sudo service ssh start
   ~~~

3. Start the HDFS service
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ ~/hadoop3/sbin/start-dfs.sh
   hduser@MyPC:~$ jps
   ~~~
   > Suppose you need to observe at least four (4) services, including both NameNode and DataNode, as stated in step 12 of G7. Otherwise, you may need to reformat the HDFS NameNode. Wait for the format process to complete without errors before proceeding. Note that formatting the NameNode will result in loss of all data files in HDFS. You also need to recreate the directory /user and its sub-directory /user/hduser after starting the HDFS service and before moving on to the next steps.
   >  ~~~bash
   > $ cd ~
   > $ ~/hadoop3/bin/hdfs namenode -format
   > $ ~/hadoop3/sbin/start-dfs.sh
   > $ jps
   > $ hdfs dfs -mkdir /user
   > $ hdfs dfs -mkdir /user/hduser
   > ~~~

4. Start the YARN service
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ ~/hadoop3/sbin/start-yarn.sh
   hduser@MyPC:~$ jps
   ~~~
   > Suppose you need to observe at least six (6) services in the total, refer steps 12 and 13 of G7.

## E10. Attention: At the end of all future practical [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Ensue that you have login as **hduser** or switch account to **hduser**
   ~~~bash
   $ su - hduser
   ~~~

2. Stop the YARN service
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ ~/hadoop3/sbin/stop-yarn.sh
   ~~~

3. Stop the HDFS service
   ~~~bash
   hduser@MyPC:~$ ~/hadoop3/sbin/stop-dfs.sh
   ~~~
   > Issue command top to examine all expected services terminated, and use Ctrl-c to exit from command top

4. Exit from your user account(s) 
   ~~~bash
   $ exit
   ~~~

