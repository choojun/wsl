## Data Engineering with Distributed Environment for Data Analytics in the Microsoft Windows Subsystem for Linux (WSL)

### Summary and Tested Version

| Requirement\Section |  [E](https://choojun.github.io/wsl_hadoop)  |  [F](https://choojun.github.io/wsl_hdfs) |  [G](https://choojun.github.io/wsl_pyspark) | [H](https://choojun.github.io/wsl_pyspark_ml)  |  [I](https://choojun.github.io/wsl_pyspark_viz)  |  [J](https://choojun.github.io/wsl_kafka)  |  [K](https://choojun.github.io/wsl_hbase)  |  [L](https://choojun.github.io/wsl_happybase)  |  [M](https://choojun.github.io/wsl_hive) |
|---------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| Hadoop              | 3.3.6 | *1 | *1                  | *1 | *1 | *1     | *1                   | *1    | *1        |
| Spark               |       |    | 3.5.1               | *1 | *1 |        | *1                   |       | *1        |
| Scala               |       |    | Targeted on 2.13.x  |    |    | 2.13.x |  Targeted on 2.13.x  |       |           |
| Jupyter Notebook    |       |    | 6.4.8               |    | *1 |        |                      |       |           |
| Kafka               |       |    |                     |    |    | 3.7.0  | *1                   | *1    |           |
| HBase               |       |    |                     |    |    |        | 2.5.7                | *1    |           |
| HappyBase           |       |    |                     |    |    |        |                      | 1.2.0 |           |
| Derby               |       |    |                     |    |    |        |                      |       | 10.14.2.0 |
| Hive                |       |    |                     |    |    |        |                      |       | 2.3.9     |
| Web Browser         | *1 |    | *1 |    | *1 |    |    |    |    |
| SSH and PDSH        | *1 | *1 | *1 | *1 | *1 | *1 | *1 | *1 | *1 |
| Internet            | *2 | *2 | *2 | *2 | *2 | *2 | *2 | *2 | *2 |
| WSL                 | *3 | *3 | *3 | *3 | *3 | *3 | *3 | *3 | *3 |

> *1 Needed
> 
> *2 Constant access
>
> *3 WSL Version 2 with distro Ubuntu 22.04

Data engineering involves building systems to collect and utilize data. This data typically supports subsequent analysis and data science, often incorporating machine learning. Making data usable generally requires significant computational resources, storage, and processing. In essence, data engineering is the design and development of systems that allow individuals to gather and analyze raw data from diverse sources and formats. This website provides a one-stop setup and configuration for the system using Microsoft WSL. Hereby, the website has also incorporated a suite of distributed-ready open source software and guided exploration through selected application samples in sections.

Read more details at URL https://choojun.github.io/wsl 
