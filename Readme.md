# Find Association Rules using Spark ML Library

## Dataset
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 
30 31 32 
33 34 35 
...
```
Each line is an itemset, and our job is to generate association rules by providing the minimum support threshold and minimum confidence threshold to the FPGrowth model.

## Usage
Run the command below to install all the required packages.
```
pip install -r requirements.txt -y
```

To run the source code, type:
```
python fpgrowth-ml-spark.py /path/to/data min_support min_conf
```
where `/path/to/data` is the path to your data file, `min_support`is the minimum support threshold and `min_conf` is the minimum confidence threshold.

In my case, the command is:
```
python fpgrowth-ml-spark.py data 0.01 0.9
```

## References
* FPGrowth example code: https://github.com/apache/spark/blob/master/examples/src/main/python/ml/fpgrowth_example.py
* Transform RDD to DataFrames: https://spark.apache.org/docs/latest/sql-programming-guide.html#inferring-the-schema-using-reflection
