
"""
WEEK 3: NumPy and Pandas for Data Manipulation
Dataset: Iris Flower Dataset
CSV columns:
id, sepal_length, sepal_width, petal_length, petal_width, Species
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------
# COMMON DATA LOADER
# ---------------------------------------------------------------
def load_iris_data():
    df = pd.read_csv("iris.csv")

    # Standardize column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    # Support alternative column names
    aliases = {
        "class": "species",
        "variety": "species",
        "iris_species": "species",
    }
    df = df.rename(columns=aliases)

    required_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species",
    ]

    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing columns: {sorted(missing)}. "
            f"Available columns: {df.columns.tolist()}"
        )

    # Standardize species labels: Iris-setosa -> setosa
    df["species"] = (
        df["species"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.replace("iris-", "", regex=False)
    )

    # ID is an identifier, not a flower measurement.
    # Keep only the columns needed for analysis.
    df = df[required_cols].copy()

    return df


# ---------------------------------------------------------------
# NUMPY DEMONSTRATION
# ---------------------------------------------------------------
def numpy_demo():
    print("=" * 60)
    print("NUMPY DEMONSTRATION")
    print("=" * 60)

    df = load_iris_data()

    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    # Convert the four measurements into a NumPy array
    arr = df[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    ).to_numpy(dtype=float)

    # Exclude rows with invalid measurements
    arr = arr[~np.isnan(arr).any(axis=1)]

    print("\nFirst 5 flowers:\n", arr[:5])

    print("\nMean of each measurement:")
    print(np.mean(arr, axis=0).round(2))

    print("\nStandard deviation:")
    print(np.std(arr, axis=0).round(2))

    print("\nSum of each measurement:")
    print(np.sum(arr, axis=0).round(2))

    print("\nFirst flower measurements multiplied by 2:")
    print(arr[0] * 2)

    # Petal length is the third column (index 2)
    petal_lengths = arr[:, 2]

    print("\nPetal lengths greater than 5 cm:")
    print(petal_lengths[petal_lengths > 5])

    # Matrix operations
    matrix = np.arange(1, 10).reshape(3, 3)

    print("\nMatrix:\n", matrix)
    print("\nTranspose:\n", matrix.T)
    print("\nRow sums:", matrix.sum(axis=1))
    print("Column sums:", matrix.sum(axis=0))
    print("\nMatrix product:\n", matrix @ matrix)

    # Broadcasting
    row = np.array([1, 2, 3])
    print("\nMatrix + row:\n", matrix + row)

    col = np.array([[1], [2], [3]])
    print("\nMatrix * column:\n", matrix * col)

    # NumPy creation functions
    print("\nZeros:", np.zeros(3))
    print("Ones:", np.ones(3))
    print("Linspace:", np.linspace(0, 1, 5))

    np.random.seed(42)
    print("Random integers:", np.random.randint(1, 100, size=5))


# ---------------------------------------------------------------
# PANDAS BASICS
# ---------------------------------------------------------------
def pandas_demo():
    print("\n" + "=" * 60)
    print("PANDAS BASICS")
    print("=" * 60)

    df = load_iris_data()

    # Series
    s = pd.Series(
        [5.1, 4.9, 4.7],
        index=["Flower 1", "Flower 2", "Flower 3"],
    )

    print("\nSeries:\n", s)
    print("Flower 1 sepal length:", s["Flower 1"])

    # DataFrame
    print("\nFirst 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())

    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)

    print("\nDataFrame information:")
    df.info()

    print("\nStatistical summary:\n", df.describe())

    # Indexing
    print("\nSepal length column:\n", df["sepal_length"].head())
    print("\nFirst row using loc:\n", df.loc[0])
    print("\nFirst 3 rows and first 2 columns:\n",
          df.iloc[0:3, 0:2])

    # Convert measurements to numeric
    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Filtering
    print("\nFlowers with petal length > 5 cm:")
    print(df[df["petal_length"] > 5])

    print("\nSetosa flowers with sepal length < 5 cm:")
    print(
        df[
            (df["species"] == "setosa")
            & (df["sepal_length"] < 5)
        ]
    )

    # Feature engineering
    df["petal_area_approx"] = (
        df["petal_length"] * df["petal_width"]
    )

    print("\nTop 5 flowers by petal length:")
    print(
        df.sort_values(
            "petal_length", ascending=False
        ).head()
    )

    # Grouping and aggregation
    print("\nAverage measurements by species:")
    print(df.groupby("species")[numeric_cols].mean().round(2))

    print("\nMultiple aggregations:")
    print(
        df.groupby("species").agg(
            avg_petal_length=("petal_length", "mean"),
            max_petal_width=("petal_width", "max"),
            flower_count=("species", "count"),
        ).round(2)
    )


# ---------------------------------------------------------------
# CLIENT PROJECT: CLEAN AND AGGREGATE IRIS DATA
# ---------------------------------------------------------------
def client_project():
    print("\n" + "=" * 60)
    print("CLIENT PROJECT: IRIS DATA CLEANING AND ANALYSIS")
    print("=" * 60)

    df = load_iris_data()

    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    print("\nRaw dataset shape:", df.shape)
    print("\nFirst 5 rows:\n", df.head())

    # Data inspection
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    # Data cleaning
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["species"])
    df = df[df["species"].str.strip() != ""]

    # Fill missing measurements using the species median
    for col in numeric_cols:
        df[col] = df.groupby("species")[col].transform(
            lambda values: values.fillna(values.median())
        )

    # Remove rows that still have missing measurements
    df = df.dropna(subset=numeric_cols)

    # Remove exact duplicate observations
    df = df.drop_duplicates().reset_index(drop=True)

    print("\nClean dataset shape:", df.shape)
    print("Remaining missing values:",
          int(df.isnull().sum().sum()))
    print("Remaining duplicates:", df.duplicated().sum())

    # Feature engineering
    df["sepal_area_approx"] = (
        df["sepal_length"] * df["sepal_width"]
    )
    df["petal_area_approx"] = (
        df["petal_length"] * df["petal_width"]
    )

    # Overall analysis
    print("\nOverall average measurements:")
    print(df[numeric_cols].mean().round(2))

    print("\nStatistical summary:")
    print(df[numeric_cols].describe().round(2))

    # Species-wise aggregation
    species_summary = df.groupby("species").agg(
        avg_sepal_length=("sepal_length", "mean"),
        avg_sepal_width=("sepal_width", "mean"),
        avg_petal_length=("petal_length", "mean"),
        avg_petal_width=("petal_width", "mean"),
        avg_petal_area=("petal_area_approx", "mean"),
        flower_count=("species", "count"),
    ).round(2)

    print("\nSpecies-wise summary:\n", species_summary)

    # Find the species with the largest average petal length
    largest_species = species_summary[
        "avg_petal_length"
    ].idxmax()

    print(
        "\nLargest average petal length:",
        largest_species
    )

    # Pivot table
    pivot = df.pivot_table(
        values="petal_length",
        index="species",
        aggfunc=["mean", "min", "max"],
        observed=True,
    ).round(2)

    print("\nPetal length pivot table:\n", pivot)

    # Save outputs
    df.to_csv("cleaned_iris_data.csv", index=False)
    species_summary.to_csv("iris_species_summary.csv")

    print("\nSaved: cleaned_iris_data.csv")
    print("Saved: iris_species_summary.csv")



if __name__ == "__main__":
    try:
        numpy_demo()
        pandas_demo()
        client_project()

    except FileNotFoundError:
        print(
            "\nERROR: iris.csv not found.\n"
            "Place iris.csv in the same folder as this Python script."
        )

    except (ValueError, pd.errors.ParserError) as error:
        print("\nERROR:", error)
