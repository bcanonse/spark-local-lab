# %%
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .config("spark.driver.host", "127.0.0.1")
    .appName("devcontainer-test")
    .getOrCreate()
)

spark.range(10).show()
# %%
