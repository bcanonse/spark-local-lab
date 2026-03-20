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

olimpians_teams.take(15)

# %% Map, Distinct and Count
olimpians_teams.map(lambda x : (x[2])).distinct().count()
# %% GroupByKey and Count
olimpians_teams.map(lambda x : (x[2], 1)).groupByKey().mapValues(len).takeOrdered(10, key=lambda x: -x[1])
# %% Filter and Count
teams_of_arg = olimpians_teams.filter(lambda x : "ARG" in x)
teams_of_arg.count()

# Cuando son subconjuntos se puede usar collect
teams_of_arg.collect()

# %% Count Aproximate before counting 20 seconds
olimpians_teams.countApprox(20)

# %%
