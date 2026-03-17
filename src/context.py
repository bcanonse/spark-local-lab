# %% Context
from pyspark import SparkContext

# %% Context Session
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .master("local")
    .config("spark.driver.host", "127.0.0.1")
    .appName('myFirstSession')
    .getOrCreate()
)

spark.stop()

# %% Context session

sc = SparkContext(master='local', appName='myFirstContext')

spark2 = SparkSession(sc)

spark2.range(10).show()

# %%
