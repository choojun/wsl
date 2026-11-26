![hadoop](https://github.com/choojun/choojun.github.io/assets/6356054/0233d690-e03c-4699-a0e9-e9f932139de3)

# F. HDFS File Operations and MapReduce [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. This practical introduces the basic Hadoop Distributed File System (HDFS) operations.
2. Login as **hduser**, and the HDFS shell can be invoked using 
~~~bash
$ hdfs dfs <args>  
~~~

3. To see the available commands in the shell
~~~bash
$ hdfs dfs -help
~~~


## F1. Basic File Operations [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login as **hduser**, download a remote file from Google Drive
~~~bash
$ cd ~
$ wget --no-check-certificate 'https://drive.google.com/file/d/1qjxR3xLs6MVidyO5TRxBtI4zMVdeDdz2/view' -O shakespeare.txt
~~~

2.	Copy the downloaded file shakespeare.txt to the distributed file system
~~~bash
$ hdfs dfs -put shakespeare.txt shakespeare.txt
~~~
> You may apply the option -f to force overwrite the destination file in the distributed file system, e.g.
> ~~~bash
> $ hdfs dfs -put -f shakespeare.txt shakespeare.txt
> ~~~~

3.	Make a directory named corpora in the HDFS file system
~~~bash
$ hdfs dfs -mkdir corpora
~~~

4.	Read the contents of the file using the cat command, and then pipe the output to less in order to view the contents of the remote file
~~~bash
$ hdfs dfs -cat shakespeare.txt | less
~~~
> Use the arrow keys to navigate the file. Type q to quit.

5.	Copy a file from the distributed file system to the local file system
~~~bash
$ hdfs dfs -get shakespeare.txt ./shakespeare-dfs.txt
~~~
> You may apply the option -f to force overwrite the destination file in the local file system, e.g.
> ~~~bash
> $ hdfs dfs -get -f shakespeare.txt ./shakespeare-dfs.txt
> ~~~~

6.	To change the permission of the file shakespeare.txt to 664
~~~bash
$ hdfs dfs -ls shakespeare.txt 
$ hdfs dfs -chmod 664 shakespeare.txt
$ hdfs dfs -ls shakespeare.txt 
~~~
> Note that 664 is an octal representation of the flags to set for the permission triple. The above statement  changes the permissions to -rw-rw-r--.  
> 6 is 110, which means read and write, but not execute.  
> 7 is 111, which means complete permissions.  
> 4 is 100, which means read-only.  

7.	Download the following two remote files from Google Drive and repeat Steps 2 through 6 as an exercise
~~~bash
$ cd ~
$ wget --no-check-certificate 'https://drive.google.com/file/d/1skRa_0NTu-XmthVsot3NtHL8SYYaLzkD/view' -O HarryPotter1.txt
$ wget --no-check-certificate 'https://drive.google.com/file/d/155Sra6cu3AmSQ1oyh8kLAl_KdPzY7PrY/view' -O HarryPotter2.txt
~~~

## F2. Advanced File Operations [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login as **hduser**, and to view the contents of your current directory
~~~bash
$ hdfs dfs -ls
~~~

2.	To view the contents of a non-empty directory
~~~bash
$ hdfs dfs -ls /user
~~~

3.	To create a test directory, e.g., testHDFS. Note that it will appear within the HDFS.
~~~bash
$ hdfs dfs -mkdir testHDFS
~~~

4.	Now you must verify that the created directory by listing your HDFS. You should see the testHDFS directory listed, if it is created at the home directory of hduser.
~~~bash
$ hdfs dfs -ls /user/hduser
~~~

5.	Create a file, which you wish to copy from local file system to HDFS
~~~bash
$ echo "HDFS test file" >> testFile
~~~

6.	Note that that is going to create a new file named testFile, including the characters HDFS test file. To verify this, input:
~~~bash
$ ls
~~~

7.	To verify that the file was created
~~~bash
$ cat testFile
~~~

8.	To copy the file to HDFS from Linux local file system into HDFS
~~~bash
$ hdfs dfs -copyFromLocal testFile
~~~
> To copy files from your local machine to HDFS, use the command -copyFromLocal. The command -cp is only used to copy files within HDFS. For more options and flexibility in copying files or directories to your desired destination within HDFS, consider using the alternative command shown below
> ~~~bash
> hdfs dfs -put <Linux local file system> <distributed file system>
> ~~~

9.	Now you need to confirm that the file has been copied over correctly
~~~bash
$ hdfs dfs -ls
$ hdfs dfs -cat testFile
~~~

10.	Now you can move it into the testHDFS directory you have already created
~~~bash
$ hdfs dfs -mv testFile testHDFS
$ hdfs dfs -ls
$ hdfs dfs -ls testHDFS/
~~~
> The first command moved your testFile from the HDFS home directory into the test one you created. The second command of this command then shows us that it's no longer in the HDFS home directory, and the third command confirms that it's now been moved to the test HDFS directory.

11.	To copy a file
~~~bash
$ hdfs dfs -cp testHDFS/testFile testHDFS/testFile2
$ hdfs dfs -ls testHDFS/
~~~

12.	Checking disk space is useful when you're using HDFS. It can be identified with the following command
~~~bash
$ hdfs dfs -du
~~~

13.	To view how much space is available in HDFS across the Hadoop cluster
~~~bash
$ hdfs dfs -df
~~~

14.	To to delete a file or directory in the HDFS
~~~bash
$ hdfs dfs -rm testHDFS/testFile
$ hdfs dfs -ls testHDFS/
~~~

15.	You will observe that you still have the testHDFS directory and testFile2 leftover that you created. Remove the directory with the following command
~~~bash
$ hdfs dfs -rm -r testHDFS
$ hdfs dfs -ls
~~~
> In addition to the above commands, there are a number of POSIX-like commands (https://en.wikipedia.org/wiki/List_of_POSIX_commands) which include chgrp, chown, cp, du, mkdir, stat, tail


## F3. MapReduce with Java - Word Count [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner. A MapReduce job splits the input data-set into independent chunks which are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks. The MapReduce framework operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job, conceivably of different types.
2.	Input and Output types of a MapReduce job:
> (input) <k1, v1> -> map -> <k2, v2> -> combine -> <k2, v2> -> reduce -> <k3, v3> (output)

3.	Read more on MapReduce at URLs https://hadoop.apache.org/docs/r3.4.3/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html , https://en.wikipedia.org/wiki/MapReduce and download file [WordCount.zip](https://github.com/choojun/choojun.github.io/files/14274971/WordCount.zip) for exercise as follows.

4.	Login as **hduser**, and make a copy of the C:\de\WordCount folder in the local hduser’s home directory
~~~bash
$ cd ~
$ sudo cp -r /mnt/c/de/WordCount /home/hduser
$ ls
$ sudo chown hduser:hduser -R /home/hduser/WordCount
$ ls
~~~

5. Change directory to the WordCount directory
~~~bash
$ cd WordCount
~~~

6.  Review and understand the code in WordCount.java. Compile WordCount.java and create a jar file. Check the contents of the directory after each of the following statements
~~~bash
$ cat ~/WordCount/WordCount.java
$ hadoop com.sun.tools.javac.Main WordCount.java
$ jar cf wc.jar WordCount*.class
$ ls ~/WordCount
~~~

7. To use the MapReduce, make sure file shakespeare.txt exist in the distributed file system before submitting the job to the Hadoop cluster 
~~~bash
$ hdfs dfs -ls /user/hduser
$ hadoop jar wc.jar WordCount shakespeare.txt wordcounts
~~~
> You may copy the Linux local system to the distributed system using the following command
> ~~~
> $ hdfs dfs -put ~/WordCount/shakespeare.txt /user/hduser
> ~~~

8. Examine result of the job by running cat on the part file from the distributed file system and pipe it with the less 
~~~bash
$ hdfs dfs -cat wordcounts/part-r-00000 | less
~~~
> Exit the piped environment using Ctrl-z

9. List all current running jobs (while and before the running job completed)
~~~
$ mapred job -list
~~~

10. Repeat the Steps 7 to 9 with the two downloaded files, HarryPotter1.txt and HarryPotter2.txt, as an exercise.

## F4. MapReduce with Python - On-time Performance of Flights [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login as **hduser**, download file [StreamingOn-time.zip](https://github.com/choojun/choojun.github.io/files/14274973/StreamingOn-time.zip) , and make a copy of the C:\de\StreamingOn-time folder in the local hduser’s home directory
~~~bash
$ sudo cp -r /mnt/c/de/StreamingOn-time /home/hduser
$ sudo chown hduser:hduser -R /home/hduser/StreamingOn-time
~~~

2. Change directory to the StreamingOn-time directory. Test the scripts without the Hadoop overhead by simulating the MapReduce pipeline using Linux pipes and the sort command. 
~~~bash
$ cd StreamingOn-time
$ cat flights.csv | ./mapper.py | sort | ./reducer.py
~~~
> Suppose that you may issue the following commands **if you have observed the error of /usr/bin/env: ‘python’: No such file or directory**. Re-execute the same command to retrying
> ~~~bash
> $ sudo apt update
> $ sudo apt install python-is-python3
> ~~~

3. Create a required directory in the distributed file system, and you may review the created directory before copying the required file flights.csv to the destination directory
~~~bash
$ hdfs dfs -ls /user/hduser
$ hdfs dfs -mkdir /user/hduser/StreamingOn-time
$ hdfs dfs -ls /user/hduser
$ hdfs dfs -ls /user/hduser/StreamingOn-time
$ hdfs dfs -put /home/hduser/StreamingOn-time/flights.csv /user/hduser/StreamingOn-time
$ hdfs dfs -ls /user/hduser/StreamingOn-time
~~~

4. Execute the Streaming job in the hadoop cluster, and examine the new created directory as well as output
~~~bash
$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input StreamingOn-time/flights.csv -output StreamingOn-time/average_delay -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py
$ hdfs dfs -ls /user/hduser/StreamingOn-time
$ hdfs dfs -ls /user/hduser/StreamingOn-time/average_delay
~~~

5. Copy the HDFS’ StreamingOn-time/average_delay directory to your Linux local directory, and list the contents of the local system’s directory to check if the folder from HDFS was copied successfully
~~~
$ hdfs dfs -copyToLocal /user/hduser/StreamingOn-time/average_delay
$ ls /home/hduser/StreamingOn-time/average_delay
~~~

6. Check the contents of the average_delay folder by viewing the content of the beginning of the part-00000 file
~~~
$ head /home/hduser/StreamingOn-time/average_delay/part-00000
~~~

