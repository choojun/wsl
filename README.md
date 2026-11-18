# Data Engineering with Distributed Environment for Data Analytics: 
## An One-Stop of Setup and Configuration in the Microsoft Windows Subsystem for Linux (WSL) - UBuntu 24.04 LTS

Data engineering involves building systems to collect and utilize data. This data typically supports subsequent analysis and data science, often incorporating machine learning. Making data usable generally requires significant computational resources, storage, and processing. In essence, data engineering is the design and development of systems that allow individuals to gather and analyze raw data from diverse sources and formats. This website provides a one-stop setup and configuration for the system using Microsoft WSL. Hereby, the website has also incorporated a suite of distributed-ready open source software and guided exploration through selected application samples in the following setup sections.

| Section (Tested with WSL2 and [Ubuntu](https://ubuntu.com/) 24.04 - LTS) | Windows 7 | Windows 10 | Windows 11 |
|---|---|---|---|
| A. [Remove/Setup WSL with Ubuntu](wsl_setup.md) | ❌ | ✔ | ✔ |
| B. [Running Ubuntu on WSL](wsl_ubuntu.md) | ❌ | ✔ | ✔ |
| C. [Backup the Distro on WSL](wsl_backup.md) | ❌ | ✔ | ✔ |
| D. [Restore (Import) the Distro on WSL](wsl_restore.md) | ❌ | ✔ | ✔ |

#### Note for Apple MacOS users
If you are using Apple machines (MacBooks and iMacs with Intel/Apple Silicon processor), you may need to install [VMware Fusion Pro](https://blogs.vmware.com/cloud-foundation/tag/desktop-hypervisor/) (Free for educational and personal use) to virtualize Ubuntu 24.04.x. You can find the specific 24.04.x installer at https://ubuntu.com/download/alternative-downloads. After completing the Ubuntu setup, follow the same instructions in Sections E to Z to set up the required environment.

| Setup Section (Tested with [OpenJDK](https://openjdk.org/) 17 LTS) | Required Framework and Software Combinations |
|---|---|
| E. [Hadoop](wsl_hadoop.md) <br>&nbsp;&nbsp;Self-check: <br>  DFS 123 | [Apache Hadoop](https://hadoop.apache.org/) 3.4.1 or 3.4.3 ? E5-2, E8-3| 
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
### Hints: To start all services at the beginning of future practical


### Hints: To stop all services at the end of future practical

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


