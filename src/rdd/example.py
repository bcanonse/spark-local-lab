# %% Initializing Context
from pyspark import SparkContext

sc = SparkContext(master='local', appName='transformAndActions')

rddl = sc.parallelize([1,2,3])

type(rddl)

rddl.collect()

# %% List content files

path = "../../files/"

olimpians_teams = (
    sc.textFile(path + "paises.csv")
    .map(lambda line : line.split(","))
)

olimpians_teams.take(5)
# %% Stopping the context
sc.stop()

# %%
