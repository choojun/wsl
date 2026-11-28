![happybase](https://github.com/choojun/choojun.github.io/assets/6356054/b4fa6fea-61a0-44e4-b62e-a97584cfe798)

# L. HappyBase with HBase Thrift [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)

1. HappyBase is a developer-friendly Python library to interact with Apache HBase. Note that Apache HBase is written in Java and natively provides a Java client API. However, if our application is written in a non-Java language (like Python, C++, or Node.js) and we want to read or write data to HBase without using Java, we use the HBase Thrift.
2. To explore the HappyBase and its API, read more at URLs https://happybase.readthedocs.io/en/latest/ and https://happybase.readthedocs.io/en/latest/user.html . They should provide you with enough information to get you started.


## L1. Setup HappyBase and HBase Thrift [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)

1. Login as **hduser**, and we may access Hbase using Python. We use the HappyBase’ Python library, which accesses Hbase using a Thrift gateway. Then, Install HappyBase, and verify the installed packages with the following commands
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
   (de-test-venv) hduser@MyPC:~$ pip install happybase
   (de-test-venv) hduser@MyPC:~$ python -c 'import happybase'
   ~~~

2. Ensure the following services started sequentially, and check them with command jps
   - SSH
   - HDFS
   - YARN
   - Kafka
   - HBase
   - Then, HBase Thrift
   > Note that a total of eleven (11) services can be observed.

3. Start up the **Thrift** service at port 9090 to run at the background
   ~~~bash
   hduser@MyPC:~$ cd ~
   hduser@MyPC:~$ ~/hbase/bin/hbase thrift start -p 9090 &
   ~~~
   > Find the pid for the Thrift service, and a total of eleven (11) services can be observed eventually.
   > 
   > Stop the Thrift service using the identified pid
   ~~~bash
   hduser@MyPC:~$ ps -aux | grep 9090
   hduser    9441  1.5  3.1 2928716 152960 pts/2  Sl   07:46   0:05
   hduser@MyPC:~$ kill 9441
   ~~~
   Or,
   ~~~bash
   hduser@MyPC:~$ jps
     6849 NodeManager
     9441 ThriftServer
     7233 QuorumPeerMain
     8321 HMaster
     6227 DataNode
     6451 SecondaryNameNode
     6053 NameNode
     9735 Jps
     8539 HRegionServer
     6700 ResourceManager
     7613 Kafka
   hduser@MyPC:~$ kill 9441
   ~~~

## L2. Using HappyBase [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)
1.	Open another session in terminal, login as **hduser**, and activate the venv. Then, launch the python command-line interpreter
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduser@MyPC:~$ python
    ~~~
    > When you want to exit the python command-line interpreter, type
    ~~~bash
    >>> exit()
    ~~~

2. Creating connection to the HBase by importing HappyBase. Then, create connection to localhost
   ~~~bash
   >>> import happybase
   >>> connection = happybase.Connection(port=9090)
   ~~~

3. List all the available HBase tables
   ~~~bash
   >>> print(connection.tables())
   ~~~

4. Display all the rows in one of the HBase tables
   ~~~bash
   >>> t = connection.table('linkshare')
   >>> rs = t.scan()
   >>> for r in rs:
   ...     print(r)
   ~~~


## L3. Creating Tables in HBase [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)

1.	Open another session in terminal, login as hduser, and activate the venv. Then, launch the python command-line interpreter
    ~~~bash
    hduser@MyPC:~$ cd ~
    hduser@MyPC:~$ source de-test/de-test-venv/bin/activate
    (de-test-venv) hduser@MyPC:~$ python
    ~~~

2. Create a new HBase table with a single column-family
   ~~~bash
   >>> import happybase
   >>> connection = happybase.Connection(port=9090)
   >>> connection.create_table('mytable', {'cf1':dict()})
   ~~~
   > If you encounter the following exception,
   >> **thriftpy2.transport.base.TTransportException:
   >> TTransportException(type=4, message='TSocket read 0 bytes')**
   >> 
   > Run the statement to create a connection to the localhost again and then the statement to create the table once again. List all the available HBase tables to confirm that the table has been successfully created.

3. Create a HBase table with 3 column families as described below
   - cf1	:	maximum 10 columns
   - cf2	:	maximum 2 columns with the data blocks resident in memory after they are read
   - cf3	:	no setting of columns/attributes.
   ~~~bash
   >>> connection.create_table('mytable2', {'cf1':dict(max_versions=10),'cf2':dict(max_versions=2, block_cache_enabled=False), 'cf3':dict()})
   ~~~
   > List all the available HBase tables to confirm that the table has been successfully created.

4. Create a tables with table namespace
   ~~~bash
   >>> connection2 = happybase.Connection(host='localhost', port=9090, table_prefix='prj_pfx')
   >>> connection2.create_table('mytable3', {'cf1':dict(max_versions=5),'cf2':dict(max_versions=2)})
   ~~~
   > List all the available HBase tables to confirm that the table has been successfully created.

5. Invoke the HBase shell to check the tables that were created using HappyBase
   ~~~bash
   $ cd ~
   $ ~/hbase/bin/hbase shell
   ~~~

6. List all the HBase tables
   ~~~bash
   hbase(main):001:0> list
   ~~~

7. Show the description of the newly created tables
   ~~~bash
   hbase(main):002:0> describe 'mytable'
   hbase(main):003:0> describe 'mytable2'
   hbase(main):004:0> describe 'prj_pfx_mytable3'
   ~~~


## L4. Inserting Values into the HBase Table [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)

1.	Identify a table instance, i.e. mytable, for data insertion after the required connection
    ~~~bash
    >>> c = happybase.Connection(host='localhost', port=9090)
    >>> t = c.table('mytable') # get a Table instance
    ~~~

2.	Insert values into mytable cell by cell
    ~~~bash
    >>> t.put('k1', {'cf1:c1':'v1'})
    >>> t.put('k1', {'cf1:c2':'v2'})
    >>> t.put('k1', {'cf1:c3':'v3'})
    >>> t.put('k2', {'cf1:c1':'vv1', 'cf1:c2':'vv2', 'cf1:c3':'vv3'})
    ~~~

3.	Insert values into table with the namespace prefix
    ~~~bash
    >>> c = happybase.Connection(port=9090)
    >>> t3 = c.table('prj_pfx_mytable3')
    >>> t3.put('rk1', {'cf1:country':'UK'})
    >>> t3.put('rk1', {'cf1:city':'London'})
    >>> t3.put('rk1', {'cf1:industry':'Manufacturing'})
    >>> t3.put('rk1', {'cf2:department':'Production', 'cf2:title':'Senior Manager'})
    >>> t3.put('rk2', {'cf1:country':'Malaysia', 'cf1:city':'KL', 'cf1:industry':'Software Development', 'cf2:department':'QA', 'cf2:title':'Test Engineer'})
    ~~~
    > If you encounter a socket.error: [Errno 32] Broken pipe error, make sure that you have obtained the Table instance. If the error still exists, then kill the Thrift process and re-start it.




## L5. Retrieving Values from the HBase Tables [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)

1.	Retrieve values by individual data fields of row-key
    ~~~bash
    >>> row = t3.row(b'rk1')
    >>> print(row[b'cf1:industry'])
    >>> print(row[b'cf1:country'])
    >>> print(row[b'cf1:city'])
    >>> print(row[b'cf2:department'])
    >>> print(row[b'cf2:title'])
    >>> row = t3.row(b'rk2')
    >>> print(row[b'cf1:country'])
    >>> print(row[b'cf1:city'])
    >>> print(row[b'cf1:industry'])
    >>> print(row[b'cf2:department'])
    >>> print(row[b'cf2:title'])
    ~~~

2.	Retrieve all the data fields of row-key 'rk2'
    ~~~bash
    >>> print("data for row-key 'rk2':\n", row)
    ~~~

3.	Process multiple rows
    ~~~bash
    >>> m_rows = t3.rows(['rk1', 'rk2'])
    >>> for r in m_rows:
    ...     print("data in current row: ", r)
    ~~~

4.	Extract the column-families of each row as a dictionary
    ~~~bash
    >>> for r in m_rows:
    ...     r_as_dict = dict(r[1])
    ...     print("\nr: ", r)
    ...     print("\tAs dict: ", r_as_dict)
    ~~~

5.	Extract all the cities from the rows
    ~~~bash
    >>> city_list = []
    >>> for r in m_rows:
    ...     r_as_dict = dict(r[1])
    ...     city_list.append(r_as_dict[b'cf1:city'])
    ...
    >>> print(city_list)
    ~~~

6.	Fine-grained selections - multiple cell retrieval
    ~~~bash
    >>> c = happybase.Connection(port=9090)
    >>> t3 = c.table('prj_pfx_mytable3')
    >>> row = t3.row(b'rk1', columns=[b'cf1:country', b'cf2:title'])
    >>> print(row)
    >>> print(row[b'cf1:country'])
    >>> print(row[b'cf2:title'])
    ~~~

7.	Fine-grained selections - all columns belonging to a column-family
    ~~~bash
    >>> c = happybase.Connection(port=9090)
    >>> t3 = c.table('prj_pfx_mytable3')
    >>> row = t3.row(b'rk1', columns=[b'cf1'])
    >>> print(row)
    ~~~

8.	Retrieve with timestamps
    ~~~bash
    >>> c = happybase.Connection(port=9090)
    >>> t3 = c.table('prj_pfx_mytable3')
    >>> row = t3.row(b'rk1', columns=[b'cf1:country'], include_timestamp=True)
    >>> value, timestamp = row[b'cf1:country']
    >>> print(value)
    >>> print(timestamp)
    ~~~

9.	Retrieve cells based on versions
    ~~~bash
    >>> cells = t3.cells(b'rk1', b'cf1:country', versions=3, include_timestamp=True)
    >>> for value, timestamp in cells:
    ...  print("Cell data at {}:{}".format(timestamp, value))
    ~~~

10. Iterating through rows and extracting data fields
    ~~~bash
    >>> for key, data in t3.scan():
    ...    print("\nCompany record key: ", key.decode())
    ...    print("\tCompany info:")
    ...    print("\t\tLocation: {}, {}".format(data[b'cf1:city'].decode(), data[b'cf1:country'].decode()))
    ...    print("\t\tIndustry: {}".format(data[b'cf1:industry'].decode()))
    ...    print("\tContact person info:")
    ...    print("\t\tTitle & Department: {}, {}".format(data[b'cf2:title'].decode(), data[b'cf2:department'].decode()))
    ...
    ~~~

11. Select range of rows starting from row_start
    ~~~bash
    >>> for key, data in t3.scan(row_start=b'rk2'):
    ...     print(key, data)
    ~~~

12. Select range of rows up to row_stop
    ~~~bash
    >>> for key, data in t3.scan(row_stop=b'rk2'):
    ...     print(key, data)
    ~~~

13. Select range based on specified key range
    ~~~bash
    >>> for key, data in t3.scan(row_start=b'rk1', row_stop=b'rk3'):
    ...     print(key, data)
    ...
    ~~~
    > Have a look from hbase shell
    ~~~bash
    hbase> scan 'prj_pfx_mytable3'
    ~~~

14. Select range based on key prefix
    ~~~bash
    >>> t3.put('kr4', {'cf1:country':'Australia', 'cf1:city':'Sydney', 'cf1:industry':'Tourism', 'cf2:department':'Human Resource', 'cf2:title':'Manager'})
    >>> for key, data in t3.scan(row_prefix=b'k'):
    ...     print(key, data)
    ...
    ~~~




## L6. Deleting Values from the HBase Tables [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)](wsl)
1.	Delete a row
    ~~~bash
    >>> t3.delete(b'rk2')
    ~~~

2.	Delete specific cells of a row
    ~~~bash
    >>> t3.delete(b'rk1', columns=[b'cf1:city', b'cf2:title'])
    ~~~


## Remember to stop all services at the end of every practical [![home](https://github.com/choojun/choojun.github.io/assets/6356054/947da4b4-f259-4b82-8961-07ca48b2811a)]()
