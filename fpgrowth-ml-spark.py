import sys

from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import Row

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: wordcount <file> <min_support> <min_confidence>", file=sys.stderr)
        exit(-1)

    # Start a spark session
    sc = SparkContext(appName="FPGrowth")
    spark = SparkSession(sc)

    # Create DataFrame from raw RDD
    # Read text file into RDD
    raw_rdd = sc.textFile(sys.argv[1])

    # Split each itemset into items
    transactions = raw_rdd.map(lambda l: l.strip().split(' '))

    # Rename the column so that later we can refer it in the FPGrowth model
    transform_rdd = transactions.map(lambda p: Row(value=p))

    # Convert PipelineRDD into DataFrame
    df = transform_rdd.toDF()

    # Fit the created DataFrame into FPGrowth model
    fpGrowth = FPGrowth(itemsCol="value", minSupport=float(sys.argv[2]), minConfidence=float(sys.argv[3]))
    model = fpGrowth.fit(df)

    # Display generated association rules
    model.associationRules.show()

    # Stop spark session
    spark.stop()