from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Incremental Load") \
    .master("local[*]") \
    .getOrCreate()

# MySQL configuration
myconf = {
    "url": "jdbc:mysql://<MYSQL_HOST>:<MYSQL_PORT>/<MYSQL_DATABASE>?useSSL=false",
    "user": "<MYSQL_USER>",
    "password": "<MYSQL_PASSWORD>",
    "driver": "com.mysql.cj.jdbc.Driver"  # Updated driver class for newer versions of MySQL Connector
}

# Snowflake configuration
mysfconf = {
    "sfURL": "<SNOWFLAKE_URL>",
    "sfUser": "<SNOWFLAKE_USER>",
    "sfPassword": "<SNOWFLAKE_PASSWORD>",
    "sfDatabase": "<SNOWFLAKE_DATABASE>",
    "sfSchema": "<SNOWFLAKE_SCHEMA>",
    "sfWarehouse": "<SNOWFLAKE_WAREHOUSE>"
}

# Read data from MySQL
df = spark.read.format("jdbc").options(**myconf).option("dbtable", "dept").load()

# Add timestamp column
ndf = df.withColumn("Time_Stamp", current_timestamp())

# Write data to Snowflake
ndf.write.mode("overwrite").format("net.snowflake.spark.snowflake") \
    .options(**mysfconf) \
    .option("dbtable", "mysql2sfdept") \
    .save()
