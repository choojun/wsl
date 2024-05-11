# wsl
## Data Engineering with Distributed Environment for Data Analytics in the Microsoft Windows Subsystem for Linux (WSL)

### Summary and Tested Version

| Requirement\Section |  [E](wsl_hadoop)  |  [F](wsl_hdfs) |  [G](wsl_pyspark) | [H](wsl_pyspark_ml)  |  [I](wsl_pyspark_viz)  |  [J](wsl_kafka)  |  [K](wsl_hbase)  |  [L](wsl_happybase)  |  [M](wsl_hive) |
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

Read more details at URL https://choojun.github.io/wsl 
