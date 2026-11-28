![spark](https://github.com/choojun/choojun.github.io/assets/6356054/ed7bd2cd-1ce6-43db-8ebd-18d56f351a43)

# H. Spark and Machine Learning [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. Spark has two machine learning libraries with different APIs, but including implementations of similar algorithms. These machine learning algorithms and utilities have been designed to scale across a cluster by way of inclusion of parallel algorithms in which operations can be applied in parallel across nodes.

|                            	| spark.mllib                                                                                                                                                     	| spark.ml                                                                                                                                                                                                                                                                                                                       	|
|----------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Data Abstraction           	| Operates on the original Resilient Distributed Datasets (RDDs). RDDs lack structural optimization schemas, making data transformations more manual and verbose. 	| Built on top of DataFrames and Datasets. This allows the library to leverage the Catalyst Optimizer and Tungsten execution engine, which dynamically optimize queries, manage memory efficiently, and result in significantly faster execution times.                                                                          	|
| Workflow Pipelines         	| Provides standalone algorithms. It leaves data cleaning, feature engineering, and cross-validation tracking entirely up to the user to write manually.          	| Introduces the concept of ML Pipelines (heavily inspired by Python's scikit-learn). It provides uniform abstractions like Transformers (for feature engineering), Estimators (for training algorithms), and Evaluators (for checking metrics). This allows you to construct and save clean, reproducible end-to-end workflows. 	|
| Cross-Language Consistency 	| Historically had separate, fragmented APIs across Scala, Java, and Python, with some features lacking parity.                                                   	| Historically had separate, fragmented APIs across Scala, Java, and Python, with some features lacking parity.                                                                                                                                                                                                                  	|
| Spark Connect Compatible   	| No                                                                                                                                                              	| Yes (Native support optimized in Spark 4)                                                                                                                                                                                                                                                                                      	|

Spark (including RDDs and DataFrames) and its machine learning-based APIs are available at the URL https://spark.apache.org/docs/4.0.5/ 

File for exercise: [mllib.zip](https://github.com/choojun/choojun.github.io/files/14240398/mllib.zip)


## H1. Recommender Systems with spark.mllib [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	This example uses Alternating Least Squares (ALS) algorithm to obtain potential matches for an online dating service.

2. Login using **hduser**, activate the venv, and make a copy of the C:\de\mllib folder in the local hduser’s home directory.
~~~bash
hduser@MyPC:~$ cd ~
hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
(de-test-venv) hduserMyPC@MyPC:~$ sudo cp -r /mnt/c/de/mllib /home/hduser
(de-test-venv) hduserMyPC@MyPC:~$ sudo chown hduser:hduser -R /home/hduser/mllib
~~~

3. Edit the file matchmaker.py. Copy all data files in the mllib directory, including its sub-directory mllib/data, to the data directory in the distributed file system. You may review the contents of the mllib and mllib/data directories before proceeding to the next step.
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ nano /home/hduser/mllib/matchmaker.py
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -put mllib /user/hduser
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/mllib
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/mllib/data
~~~
> Note that you need change the correct file paths inside the matchmaker.py, e.g. from **data/\*.dat** to **hdfs://localhost:9000/user/hduser/mllib/data/\*.dat**

4. Review and understand the code in matchmaker.py before submitting the matchmaker.py job to Spark and piping the output to a file.
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -cat /user/hduser/mllib/matchmaker.py | more
(de-test-venv) hduserMyPC@MyPC:~$ spark-submit mllib/matchmaker.py 1 M > matchmaking_recs.txt
~~~

5. Examine the output in the file matchmaking_recs.txt

## H2. Clustering with spark.mllib [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1.	This example uses k-means clustering to determine which areas in the US have been most hit by earthquakes.

2. Remain login using user **hduser** and activated venv. Ensure that the data file earthquakes.csv exists in HDFS’ data directory. You may review the contents of the mllib/data directory before proceeding to the next step.
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/mllib/data
~~~

3. Review and understand the code in earthquakes_clustering.py before submitting the earthquakes_clustering.py job to Spark and piping the output to a file
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -cat /user/hduser/mllib/earthquakes_clustering.py | more
(de-test-venv) hduserMyPC@MyPC:~$ spark-submit mllib/earthquakes_clustering.py hdfs://localhost:9000/user/hduser/mllib/data/earthquakes.csv 6 > clusters.txt
~~~
> Note that this exercise takes the data file name, located in the distributed file system, as a parameter.

4. Examine the output in the file cluster.txt.

## H3. Multi-class Classification with spark.ml [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. This example uses the Naive Bayes classifier to perform multiclass classification.

2. Remain login using user **hduser** and activated venv. Ensure that the data file sample_libsvm_data.txt exists in HDFS’ data directory. You may review the contents of the mllib/data directory before proceeding to the next step.
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/mllib/data
~~~

3. Review and understand the code in naive_bayes_example.py before submitting the naive_bayes_example.py job to Spark
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -cat /user/hduser/mllib/naive_bayes_example.py | more
(de-test-venv) hduserMyPC@MyPC:~$ spark-submit mllib/naive_bayes_example.py
~~~
> Note that you need change the correct file path inside the naive_bayes_example.py, e.g.
> from **data/\*.txt** to **hdfs://localhost:9000/user/hduser/mllib/data/\*.txt**

4. Examine the output in the terminal

## H4. Recommender (Regression based) with spark.ml [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()

1. This example uses Alternating Least Squares (ALS) algorithm for movie recommendations

2. Remain login using user **hduser** and activated venv. Ensure that the data file sample_movielens_ratings.txt exists in HDFS’ data directory. You may review the contents of the mllib/data directory before proceeding to the next step
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -ls /user/hduser/mllib/data
~~~

3. Review and understand the code in als_example.py before submitting the naive_bayes_example.py job to Spark
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ hdfs dfs -cat /user/hduser/mllib/als_example.py | more
(de-test-venv) hduserMyPC@MyPC:~$ spark-submit mllib/als_example.py
~~~
> Note that you need change the correct file path inside the als_example.py, e.g.
> from **data/\*.txt** to **hdfs://localhost:9000/user/hduser/mllib/data/\*.txt**

4. Examine the output in the terminal

5 **Important: Remember to deactivate the venv**. Once you no longer need to work in the environment, you may deactivate the environment to return to your normal shell.
~~~bash
(de-test-venv) hduserMyPC@MyPC:~$ deactivate
hduserMyPC@MyPC:~$ 
~~~

## Remember to stop all services at the end of every practical [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()
