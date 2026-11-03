import pandas as pd

students={"name":["John","Smith","Alice","Bob"],
            "age":[20,22,21,23],
            "email":["john@example.com","smith@example.com","alice@example.com","bob@example.com"],
            "tamil":[99,67,88,91],
            "english":[85,90,78,92],
            "maths":[75,80,85,90],
            "science":[80,85,90,95],
            "social":[70,75,80,85]
            }

# //Add Index to the DataFrame
df=pd.DataFrame(students,index=["s1","s2","s3","s4"])
print(df)

# Adding a new column
df["total"] = df["tamil"] + df["english"] + df["maths"] + df["science"] + df["social"]
df["average"] = df["total"] / 5
print("\nDataFrame after adding total and average columns:\n", df)

# Dataframe attributes
print("DataFrame shape:", df.shape)
print("DataFrame size:", df.size)
print("DataFrame columns:", df.columns)
print("DataFrame index:", df.index)
print("DataFrame dtypes:", df.dtypes)
print("DataFrame ndim:", df.ndim)

# Accessing Row
print("\nFirst row:\n", df.iloc[0])
print("\nSecond row:\n", df.iloc[1])
print("\nRows 2 to 3:\n", df.iloc[2:4])  # Accessing rows from index 2 to 3 

