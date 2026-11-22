![spark](https://github.com/choojun/choojun.github.io/assets/6356054/ed7bd2cd-1ce6-43db-8ebd-18d56f351a43)

# G. Spark, PySpark Shell, Spark SQL and JupyterLab [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Apache Spark is an in-memory distributed computing engine especially designed for the Hadoop cluster. 
2. Read more on Spark at URLs https://spark.apache.org and https://en.wikipedia.org/wiki/Apache_Spark
3. [SparkApp.zip](https://github.com/choojun/choojun.github.io/files/14237887/SparkApp.zip)
4. [sparksql.zip](https://github.com/choojun/choojun.github.io/files/14238380/sparksql.zip)


## G1. Install and Configure Spark [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login as **hduser**. Ensure that the SSH, DFS, and YARN services are started sequentially. Then, examine them using the jps command

2.	Download the correct version of Spark from the Apache Spark downloads page (http://spark.apache.org/downloads.html), and check the compatible with your installed Hadoop
    ~~~bash
    $ cd ~
    $ wget https://archive.apache.org/dist/spark/spark-4.0.5/spark-4.0.5-bin-hadoop3-connect.tgz
    ~~~

3.	Uncompress the file
    ~~~bash
    $ tar -xvzf spark-4.0.5-bin-hadoop3-connect.tgz
    ~~~

4.	Rename the Spark folder as spark
    ~~~bash
    $ mv spark-4.0.5-bin-hadoop3-connect spark
    ~~~

5.	Edit the file ~/.bashrc with the the following lines
    ~~~bash
    export SPARK_HOME=/home/hduser/spark
    export PATH=$SPARK_HOME/bin:$PATH
    ~~~

6.	Re-load the environment
    ~~~bash
    source ~/.bashrc
    ~~~






## G2. Setup Python venv with JupyterLab for PySpark Interactive Shell (Pyspark Shell) [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

Python virtual environments (venv) create a self-contained and isolated environment for different Python projects. This would enable you to install a specific version of a module on a per project basis which will not affect your other Python projects.

1. Login as the user **hduser**, to create a venv.

    1.1 Create a project directory (e.g., de-test)
      ~~~bash
      hduser@MyPC:~$ mkdir de-test
      ~~~
      > It is advisable to utilize distinct directories for each project development.

    1.2 Create a venv for your project (e.g., de-test-venv):
      ~~~bash
      $ sudo apt update && sudo apt install python3-full jupyter-core
      $ python3 -m venv de-test/de-test-venv
      $ de-test/de-test-venv/bin/python -m pip install -U pip wheel setuptools ipykernel grpcio-status numpy pandas
      $ de-test/de-test-venv/bin/python -m pip install -U pyspark==4.0.5
      $ de-test/de-test-venv/bin/python -m pip install -U jupyterlab
      $ de-test/de-test-venv/bin/python -m ipykernel install --user --name "de-test-venv" --display-name  "de-test-venv"
      ~~~

2. Setup JupyterLab 

   JupyterLab is a highly extensible, feature-rich notebook authoring application and editing environment, and is a part of Project Jupyter, a large umbrella project centered around the goal of providing tools (and standards) for interactive computing with computational notebooks. It is a sibling to other notebook authoring applications under the Project Jupyter umbrella, like Jupyter Notebook and Jupyter Desktop. JupyterLab offers a more advanced, feature rich, customizable experience compared to Jupyter Notebook. Read more from URL https://jupyterlab.readthedocs.io/en/latest/

   2.1 Activate the venv, install python optional packages in created venv (e.g. scikit-learn and etc)), and run JupyterLab with commands
     ~~~bash
     hduser@MyPC:~$ cd ~
     hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
     (de-test-venv) hduser@MyPC:~$ pip install -U scikit-learn matplotlib seaborn
     (de-test-venv) hduser@MyPC:~$ jupyter lab
     ~~~
     > Note that you need to activate the venv in order to install python packages within the venv (preferable way), or
     > Run Python files from the command-line interface (CLI) using the environment's dependencies (not recommended).
     > Please be aware that the download and installation process will be time-consuming. Ensure the PySpark version corresponds with your Apache Spark installation.

   2.2 Access JupyterLab with Web borser
       From the output shown in your terminal, **copy and paste one of the URLs in a web browser**.

   * To create a jupyter notebook based on your venv, under the **Notebook**, just click on the kernel with your venv name, e.g., de-test-venv. **Note that new created jupyter notebook is ready with PySpark under the de-test-venv**.

   * To close a jupyter notebook and shut down the kernel (i.e., de-test-venv), under the jupyter notebook as the active tab, click **File** and then select **Close** and **Shut Down Notebook…**
     
     > Merely closing the tab does not shut down the notebook, and therefore it is still running in the background. Therefore, be sure to click Close and Shut Down Notebook as highlighted above.
   
   * To logout from JupyterLab, click **File** and then select **Log Out**

   * To shut down the jupyterlab server, which is used to host the JupyterLab, go to the terminal where you ran the command to start JupyterLab, i.e., in Step 3.1. Press Ctrl-C and type ‘y’ to confirm that you want to shut down the server.

   2.3 **To delete any unwanted venv**, if needed, try the command with Syntax: jupyter kernelspec uninstall unwanted-kernel. Examples:
      >
      > (my-venv) hduserMyPC:~$ jupyter kernelspec uninstall my-venv
      >
      > (de-prj-venv) hduserMyPC:~$ jupyter kernelspec uninstall de-prj-venv
      >
      > (de-test-venv) hduserMyPC:~$ jupyter kernelspec uninstall de-test-venv
      >
      Once the deletion is complete, you can check JupyterLab (under File -> New Launcher) to verify that the venv is no longer listed.


   2.4	Launch the PySpark Shell. 
      ~~~bash
      (de-test-venv) hduserMyPC@MyPC:~$ pyspark
      ~~~
      > To exit the pyspark shell with command exit()
      ~~~bash
      Welcome to
             ____              __
            / __/__  ___ _____/ /__
           _\ \/ _ \/ _ `/ __/  '_/
          /__ / .__/\_,_/_/ /_/\_\   version 4.0.5
             /_/
       
       Using Python version 3.12.3 (main, Aug 31 2026 10:18:26)
       Spark context Web UI available at http://172.31.77.100:4040
       Spark context available as 'sc' (master = local[*], app id = local-1795359497285).
       SparkSession available as 'spark'.
       >>>
       >>> exit()
       ~~~
       >
       > To minimize the verbosity of Spark , you need to configure the settings of log4j after duplicating the template file (optional).
       >
       > To visit the Web UI, paste the given URL, or http://localhost:4040/, in any web browser for previewing.
       ~~~bash
       $ cp $SPARK_HOME/conf/log4j2.properties.template $SPARK_HOME/conf/log4j2.properties
       ~~~
       > Edit the newly created log4j file, by replacing every occurrence of INFO with WARN, e.g.
       > 
       > rootLogger.level = warn  
       > rootLogger.appenderRef.stdout.ref = console  

    2.5 **Important: Remember to deactivate the venv**. Once you no longer need to work in the environment, you may deactivate the environment to return to your normal shell.
       ~~~bash
       (de-test-venv) hduserMyPC@MyPC:~$ deactivate
       hduserMyPC@MyPC:~$ 
       ~~~

## G3. Using the PySpark Shell for Word Count [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Launch PySpark Shell using user **hduser**
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduserMyPC@MyPC:~$ pyspark
    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 4.0.4
          /_/
    Using Python version 3.12.3 (main, Aug 31 2026 10:18:26)
    Spark context Web UI available at http://172.31.77.100:4040
    Spark context available as 'sc' (master = local[*], app id = local-1792576061544).
    SparkSession available as 'spark'.
    >>>
    ~~~

2.	Create an Resilient Distributed Dataset (RDD) with data from a text file. It transforms the RDD to implement the word count application using Spark.
    ~~~bash
    >>> text = sc.textFile("shakespeare.txt")
    >>> print(text)
    >>> from operator import add
    >>> def tokenize(text): return text.split()
    ...
    >>> words = text.flatMap(tokenize)
    ~~~

3.	Apply the map, and then apply the reduceByKey action to obtain the word counts before saving the results in file
    ~~~bash
    >>> wc = words.map(lambda x: (x, 1))
    >>> print(wc.toDebugString())
    >>> counts = wc.reduceByKey(add)
    >>> counts.saveAsTextFile("hdfs://localhost:9000/user/hduser/wc")
    ~~~
    > In certain occasion, Apache spark does not need to have the hdfs directory path (hdfs://localhost:9000/user/hduser/) explicitly indicated to write in the local path, i.e., /home/hduser. Example:
    > counts.saveAsTextFile("wc")

4.	Exit the Pyspark Shell. Then, check the HDFS current working directory for the newly created directory’s contents, and use the head command to view one of the part files. 
    ~~~bash
    >>> exit()
    (de-test-venv) hduserMyPC@MyPC:~$
    (de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/wc
    (de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -head /user/hduser/wc/part-00000
    ~~~

5. **Important**: Remember to deactivate the venv for ending the exercise.
    ~~~bash
    (de-test-venv) hduserMyPC@MyPC:~$ deactivate
    hduserMyPC@MyPC:~$
    ~~~

## G4. Using the PySpark Shell for Numerical Processing [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login using user **hduser**, activate your venv (e.g, de-test-venv), and launch PySpark Shell **with 4 CPU cores**.
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduserMyPC:~$ pyspark --executor-cores 4
    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 4.0.4
          /_/
    Using Python version 3.12.3 (main, Aug 31 2026 10:18:26)
    Spark context Web UI available at http://172.31.77.100:4040
    Spark context available as 'sc' (master = local[*], app id = local-1792576061544).
    SparkSession available as 'spark'.
    >>>
    ~~~

2.	Try the following codes. The codes generate a list of random integers and create an RDD by parallelizing num_list with library numpy.
    ~~~bash
    >>> import numpy as np
    >>> num_list = np.random.randint(0, 10, 20)
    >>> numbers_RDD = sc.parallelize(num_list)
    >>> numbers_RDD
    ~~~

3.	You may check the type for numbers_RDD, return all the elements of the RDD as an array, return an RDD created by consolidating all elements within **each partition** into a list
    ~~~bash
    >>> type(numbers_RDD)
    >>> numbers_RDD.collect()
    >>> numbers_RDD.glom().collect()
    ~~~

4.	You may extract various elements of the RDD and extract the unique values of the RDD
    ~~~bash
    >>> numbers_RDD.first()
    >>> numbers_RDD.take(3)
    >>> numbers_RDD.take(5)
    >>> numbers_RDD.take(8)
    >>> distinct_numbers_RDD = numbers_RDD.distinct()
    >>> distinct_numbers_RDD.collect()
    ~~~

5.	You may sum all the elements in numbers_RDD, and sum all the elements in numbers_RDD using **reduce**
    ~~~bash
    >>> numbers_RDD.collect()
    >>> numbers_RDD.sum()
    >>> numbers_RDD.reduce(lambda x, y: x+y)
    ~~~

6.	You may find the max value in numbers_RDD, and filter non-zero numbers that are divisible by 3
    ~~~bash
    >>> numbers_RDD.reduce(lambda x, y: x if x > y else y)
    >>> numbers_RDD.filter(lambda x:x%3==0 and x!=0).collect()
    ~~~

7.	Create a new RDD with the squares of all the elements in numbers_RDD
    ~~~bash
    >>> numbers_RDD.collect()
    >>> squares_RDD = numbers_RDD.map(lambda x:x*x)
    >>> squares_RDD.collect()
    ~~~

8.	Generate a histogram for the elements in squares_RDD and do mapping with a regular Python function
    ~~~bash
    >>> squares_RDD.histogram([x for x in range(0, 100, 10)])
    >>> def squareroot_if_odd(x):
    ...     if x%2==0:
    ...             return x*x
    ...     else:
    ...             return x
    ...
    >>> numbers_RDD.map(squareroot_if_odd).collect()
    ~~~

9. Extract the even and odd numbers from numbers_RDD. What is the type of the collection that is returned? Sort the resulting numbers for the odd and even numbers
   ~~~bash
   >>> results = numbers_RDD.groupBy(lambda x:x%2).collect()
   >>> results
   >>> type(results)
   >>> sorted([(x, sorted(y)) for (x, y) in results])
   ~~~

10. Prform the union(), intersection(), subtract(), cartesian()
    ~~~bash
    >>> squares_RDD.collect()
    >>> numbers_RDD.collect()
    >>> union_RDD = sc.union([numbers_RDD, squares_RDD])
    >>> union_RDD.collect()
    >>>
    >>> intersection_RDD = squares_RDD.intersection(numbers_RDD)
    >>> intersection_RDD.collect()
    >>>
    >>> subtract_RDD = squares_RDD.subtract(numbers_RDD)
    >>> subtract_RDD.collect()
    >>>
    >>> cartesian_RDD = squares_RDD.cartesian(numbers_RDD)
    >>> cartesian_RDD.collect()
    ~~~

11. Note that cartesian() generates a Cartesian product of two collections and returns all the possible combinations of pairs between the elements in both collections. Try it again.
    ~~~bash
    >>> numbers_RDD.cartesian(numbers_RDD).collect()
    ~~~

12. Exit the Pyspark Shell and deactivate the virtual environment for ending the exercise.
    ~~~bash
    >>> exit()
    (de-test-venv) hduserMyPC@MyPC:~$ deactivate
    hduserMyPC@MyPC:~$
    ~~~

## G5. Using the PySpark Shell for Text Processing [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login using user **hduser**, activate your venv (e.g, de-test-venv), and launch PySpark Shell with 4 CPU cores
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduserMyPC:~$ pyspark --executor-cores 4
    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 4.0.4
          /_/
    Using Python version 3.12.3 (main, Aug 31 2026 10:18:26)
    Spark context Web UI available at http://172.31.77.100:4040
    Spark context available as 'sc' (master = local[*], app id = local-1792576061544).
    SparkSession available as 'spark'.
    >>>
    ~~~

2.	Find the longest word in a sentence
    ~~~bash
    >>> words = 'It is not that I am so smart but I stay with the questions much longer Albert Einstein'.split()
    >>> print(words)
    >>> words_RDD = sc.parallelize(words)
    >>> words_RDD.reduce(lambda w, v: w if len(w) > len(v) else v)
    ~~~
    or
    ~~~bash
    >>> def findLongestWord(x, y):
    ...     if len(x) > len(y):
    ...             return x
    ...     else:
    ...             return y
    ...
    >>> words_RDD.reduce(findLongestWord)
    ~~~

3.	Find the lexicographically largest word in a sentence
    ~~~bash
    >>> def findLargestWord(x, y):
    ...     if x > y:
    ...             return x
    ...     else:
    ...             return y
    ...
    >>> words_RDD.reduce(findLargestWord)
    ~~~

4.	Find the lexicographically smallest word in a sentence using lambda expression
    ~~~bash
    >>> words_RDD.reduce(lambda w, v: w if w < v else v)
    ~~~

5.	Count the number of lines in a text file with certain letters. Note the cache() function pulls data sets into a cluster-wide in-memory cache, which is very useful when data is accessed repeatedly
    ~~~bash
    >>> logFile = "file:///home/hduser/shakespeare.txt"
    >>> logData = sc.textFile(logFile).cache()
    >>> number_of_w = logData.filter(lambda s:'w' in s).count()
    >>> number_of_c = logData.filter(lambda s:'c' in s).count()
    >>> print("Lines with 'c':{}, lines with 'w':{}".format(number_of_c, number_of_w))
    ~~~

6. Exit the Pyspark Shell and deactivate the virtual environment for ending the exercise.
   ~~~bash
   >>> exit()
   (de-test-venv) hduserMyPC@MyPC:~$ deactivate
   hduserMyPC@MyPC:~$
   ~~~


## G6. Using the spark-submit (an Spark Command-Line utility) with Python - Word Count (SparkApp) [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login using user **hduser**,, and make a copy of the C:\de\SparkApp folder in the local hduser’s home directory
    ~~~bash
    hduserMyPC@MyPC:~$ cd ~
    hduserMyPC@MyPC:~$ sudo cp -r /mnt/c/de/SparkApp /home/hduser
    hduserMyPC@MyPC:~$ sudo chown -r hduser:hduser /home/hduser/SparkApp
    ~~~

2.	Change directory to the SparkApp folder, and review the code in wordcount.py
    ~~~bash
    hduserMyPC@MyPC:~$ cd /home/hduser/SparkApp
    hduserMyPC@MyPC:~/SparkApp$ cat wordcount.py | more
    ~~~

3.	Submit the wordcount.py job to Spark (directly to the YARN resource manager)
    ~~~bash
    hduserMyPC@MyPC:~/SparkApp$ spark-submit wordcount.py shakespeare.txt hdfs://localhost:9000/user/hduser/spark_wc
    ~~~
> May always re-submit the same job by using different directory name, e.g. give a new name instead of **spark_wc**

4.	You may check the results directory in the HDFS system and view the beginning portion of the output file part-00000
    ~~~bash
    hduserMyPC@MyPC:~/SparkApp$ hdfs dfs -ls spark_wc
    hduserMyPC@MyPC:~/SparkApp$ hdfs dfs -head spark_wc/part-00000 
    ~~~


## G7. Using the spark-submit (an Spark Command-Line utility) with Python - Flight Delay ([SparkApp](https://github.com/choojun/choojun.github.io/files/14237887/SparkApp.zip)) [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Remain login using user **hduser**, make a copy of the C:\de\SparkApp folder in the local hduser’s home directory, change directory to the SparkApp directory, and review the code in app.py
    ~~~bash
    hduserMyPC@MyPC:~$ cd ~
    hduserMyPC@MyPC:~$ sudo cp -r /mnt/c/de/SparkApp /home/hduser
    hduserMyPC@MyPC:~$ sudo chown hduser:hduser -R /home/hduser/SparkApp
    hduserMyPC@MyPC:~$ cd /home/hduser/SparkApp
    hduserMyPC@MyPC:~/SparkApp$ cat app.py | more
    ~~~
    > To terminate the review of code with Ctrl-x

2.	Make a copy of the source file 
    ~~~bash
    hduserMyPC@MyPC:~$ cd /home/hduser/SparkApp
    hduserMyPC@MyPC:~/SparkApp$ cp app.py app2.py
    ~~~

3.	Modify the file path in app.py, which has the codes of loading the airlines lookup dictionary and reading the CSV data into an RDD, as follows
    ~~~bash
    airlines = dict(sc.textFile("file:///home/hduser/SparkApp/ontime/airlines.csv").map(split).collect())
    flights = sc.textFile("file:///home/hduser/SparkApp/ontime/flights.csv").map(split).map(parse)
    ~~~
    to
    ~~~bash
    airlines = dict(sc.textFile("ontime/airlines.csv").map(split).collect())
    flights = sc.textFile("ontime/flights.csv").map(split).map(parse)
    ~~~

4.	Submit the wordcount.py job to Spark (directly to the YARN resource manager)
    ~~~bash
    hduserMyPC@MyPC:~$ cd /home/hduser/SparkApp
    hduserMyPC@MyPC:~/SparkApp$ spark-submit app.py
    ~~~

5.	You may observe the print out results. 



## G8. Using the PySpark Shell with [Spark SQL](https://github.com/choojun/choojun.github.io/files/14238380/sparksql.zip) [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Spark SQL is a module in Apache Spark that provides a relational interface to work with structured data using SQL-based operations in Spark through either JDBC/ODBC connectors, a built-in interactive Hive console, or Spark SQL API. This practical covers the Spark SQL API, which runs as a library on top of Spark’s Core engine and APIs. The Spark SQL API may be accessed using the same programming interface that was used for Spark’s RDD APIs. Read more on Apache Spark at URLs https://spark.apache.org/sql/ and https://en.wikipedia.org/wiki/Apache_Spark#Spark_SQL
![sparksql](https://github.com/choojun/choojun.github.io/assets/6356054/538f24de-c002-44a0-8b57-e17b107ce1c8)


1.	Login using user **hduser**, and make a copy of the C:\de\sparksql folder in the local hduser’s home directory.
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ sudo cp -r /mnt/c/de/sparksql /home/hduser
    hduser@MyPC:~$ sudo chown -R hduser:hduser /home/hduser/sparksql
    ~~~

2.	Change directory to the sparksql folder, and review the code in wordcount.py
    ~~~bash
    hduser@MyPC:~$ cd ~/sparksql/data
    hduser@MyPC:~/sparksql/data$ hdfs dfs -mkdir data
    hduser@MyPC:~/sparksql/data$ hdfs dfs -put sf_parking_clean.json /user/hduser/data/
    ~~~

3.	Activate your venv (e.g, de-test-venv), and install reverse geocoder (https://pypi.org/project/reverse_geocoder/) package. Launch PySpark Shell
    ~~~bash
    hduser@MyPC:~/sparksql/data$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduserMyPC:~$ pip3 install -U reverse_geocoder
    (de-test-venv) hduserMyPC:~$ pyspark
    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 4.0.4
          /_/
    Using Python version 3.12.3 (main, Aug 31 2026 10:18:26)
    Spark context Web UI available at http://172.31.77.100:4040
    Spark context available as 'sc' (master = local[*], app id = local-1792576061544).
    SparkSession available as 'spark'.
    >>>
    ~~~

4.	Launch the PySpark Shell, and try the following codes
    ~~~bash
    >>> from pyspark.sql import SQLContext
    >>> sqlContext = SparkSession.builder.getOrCreate()
    >>> parking = sqlContext.read.json("hdfs://localhost:9000/user/hduser/data/sf_parking_clean.json")
    >>> parking.printSchema()
    >>> parking.first()
    >>> parking.createOrReplaceTempView("parking")
    >>> parking.show()
    >>> aggr_by_type = sqlContext.sql("SELECT primetype, secondtype, count(1) AS count, round(avg(regcap), 0) AS avg_spaces FROM parking GROUP BY primetype, secondtype HAVING trim(primetype) !='' ORDER BY count DESC")
    ~~~
    ~~~bash
    >>> aggr_by_type.show()
    >>> parking.describe("regcap", "valetcap", "mccap").show()
    >>> parking.stat.crosstab("owner", "primetype").show()
    >>> parking = parking.withColumnRenamed('regcap', 'regcap_old')
    >>> parking = parking.withColumn('regcap', parking['regcap_old'].cast('int'))
    >>> parking = parking.drop('regcap_old')
    >>> parking.printSchema()
    ~~~
    ~~~bash
    >>> def convert_column(df, col, new_type):
    ...     old_col = '%s_old' % col
    ...     df = df.withColumnRenamed(col, old_col)
    ...     df = df.withColumn(col, df[old_col].cast(new_type))
    ...     df = df.drop(old_col)
    ...     return df
    ...
    >>> parking = convert_column(parking, 'valetcap', 'int')
    >>> parking = convert_column(parking, 'mccap', 'int')
    >>> parking.printSchema()  
    ~~~
    ~~~bash
    >>> import reverse_geocoder as rg
    >>> def to_city(location):
    ...	name = 'N/A'
    ...	r = rg.search((location.latitude, location.longitude))
    ...	if r != None:
    ...		name = r[0]['name']
    ...	return name  
    >>> from pyspark.sql.functions import udf
    >>> from pyspark.sql.types import StringType
    >>> location_to_city=udf(to_city, StringType())
    >>> sfmta_parking = parking.filter(parking.owner == 'SFMTA') \
    ...	.select("location_1", "primetype", "landusetyp", "garorlot", "regcap", "valetcap", "mccap") \
    ...	.withColumn("location_1", location_to_city("location_1")) \
    ...	.sort("regcap", ascending=False)
    >>> sfmta_parking.show()
    >>> sfmta_pandas = sfmta_parking.filter(sfmta_parking.location_1 != 'N/A').toPandas()
    >>> sfmta_pandas.groupby(['location_1'])['regcap'].mean().nlargest(20)
    ~~~
    > Suppose that your installed Spark does not need to have the hdfs directory path (hdfs://localhost:9000/user/hduser/) explicitly indicated. Example, it may be run as: parking = sqlContext.read.json("data/sf_parking_clean.json")

5. Exit the Pyspark Shell and deactivate the virtual environment for ending the exercise.
   ~~~bash
   >>> exit()
   (de-test-venv) hduserMyPC@MyPC:~$ deactivate
   hduserMyPC@MyPC:~$
   ~~~

## G9. Exercise [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	Login using user **hduser**, and make a copy of the C:\de\sparksql folder in the local hduser’s home directory.
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ sudo cp -r /mnt/c/de/sparksql /home/hduser
    hduser@MyPC:~$ sudo chown -R hduser:hduser /home/hduser/sparksql
    ~~~

2.	Change directory to the sparksql folder, and review the code in wordcount.py
    ~~~bash
    hduser@MyPC:~$ cd ~/sparksql/data
    hduser@MyPC:~/sparksql/data$ hdfs dfs -mkdir data
    hduser@MyPC:~/sparksql/data$ hdfs dfs -put sf_parking_clean.json /user/hduser/data/
    ~~~

3.	Activate your venv (e.g, de-test-venv), and install Apache Arrow (https://arrow.apache.org/) package. Apache Arrow is a development platform for in-memory analytics. It contains a set of technologies that enable big data systems to store, process and move data fast. Pyarrow has integred with NumPy, pandas, and built-in Python objects. Read more from URL https://arrow.apache.org/docs/python/index.html 
    ~~~bash
    hduser@MyPC:~/sparksql/data$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduserMyPC:~$ pip3 install -U pyarrow
    ~~~

4. Access JupyterLab with Web borser. From the output shown in your terminal, **copy and paste one of the URLs in a web browser**.

5. Choose the created venv, and open up the Practical3c_SparkSQL_and_DataFrames.ipynb notebook. Do the Spark SQL exercises there. Suppose that you have learned some essential codes in G4 to G8 before attempting the G9.

