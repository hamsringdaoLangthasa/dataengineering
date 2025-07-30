from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("DEV").getOrCreate()

print(spark)

import pandas as pd
df_local = pd.read_csv("test.csv")

# Convert to Spark DataFrame
df_spark = spark.createDataFrame(df_local)
df_spark.show()