from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FraudBatch").getOrCreate()

df = spark.read.csv(
    "data/raw/creditcard.csv",
    header=True,
    inferSchema=True
)

df.groupBy("Class").count().show()
stream_df = spark.readStream \
    .option("header", True) \
    .csv("data/raw")

query = stream_df.writeStream \
    .format("console") \
    .start()

query.awaitTermination()