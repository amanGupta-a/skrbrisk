
"""
WEEK 4: Data Visualization with Matplotlib and Seaborn
Dataset: Iris Flower Dataset
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create folder for saving plots
os.makedirs("plots", exist_ok=True)

sns.set_theme(style="whitegrid", palette="Set2")


# ---------------------------------------------------------------
# LOAD IRIS DATASET
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

    # Support common alternative names
    df = df.rename(columns={
        "class": "species",
        "variety": "species",
    })

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

    # Keep only columns needed for visualization
    df = df[required_cols].copy()

    # Clean species names: Iris-setosa -> setosa
    df["species"] = (
        df["species"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.replace("iris-", "", regex=False)
    )

    # Convert measurements to numeric
    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with missing required data
    df = df.dropna(subset=required_cols).reset_index(drop=True)

    return df


# ---------------------------------------------------------------
# BASIC MATPLOTLIB PLOTS
# ---------------------------------------------------------------
def matplotlib_basics(df):

    # 1. Line plot: average petal length by species
    avg = df.groupby("species")["petal_length"].mean()

    plt.figure(figsize=(7, 4))
    plt.plot(avg.index, avg.values, marker="o", label="Petal Length")
    plt.title("Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/01_line_plot.png", dpi=150)
    plt.close()

    # 2. Bar plot: average sepal length by species
    avg_sepal = df.groupby("species")["sepal_length"].mean()

    plt.figure(figsize=(7, 4))
    plt.bar(avg_sepal.index, avg_sepal.values)
    plt.title("Average Sepal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Sepal Length (cm)")
    plt.tight_layout()
    plt.savefig("plots/02_bar_plot.png", dpi=150)
    plt.close()

    # 3. Pie chart: number of flowers in each species
    counts = df["species"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Distribution of Iris Species")
    plt.tight_layout()
    plt.savefig("plots/03_pie_chart.png", dpi=150)
    plt.close()

    print("Saved basic Matplotlib plots.")


# ---------------------------------------------------------------
# SEABORN PLOTS
# ---------------------------------------------------------------
def seaborn_analysis(df):

    # 4. Correlation heatmap
    plt.figure(figsize=(7, 5))

    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )

    plt.title("Correlation Between Flower Measurements")
    plt.tight_layout()
    plt.savefig("plots/04_heatmap.png", dpi=150)
    plt.close()

    # 5. Pairplot: relationships between measurements
    pair = sns.pairplot(
        df,
        vars=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ],
        hue="species",
        diag_kind="hist",
        corner=True,
    )

    pair.figure.suptitle(
        "Relationships Between Iris Measurements",
        y=1.02,
    )

    pair.savefig("plots/05_pairplot.png", dpi=120)
    plt.close("all")

    # 6. Boxplot: petal length distribution by species
    plt.figure(figsize=(7, 4))

    sns.boxplot(
        data=df,
        x="species",
        y="petal_length",
        hue="species",
        legend=False,
    )

    plt.title("Petal Length Distribution by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.tight_layout()
    plt.savefig("plots/06_boxplot.png", dpi=150)
    plt.close()

    print("Saved Seaborn plots.")


# ---------------------------------------------------------------
# CLIENT PROJECT: IRIS VISUALIZATION DASHBOARD
# ---------------------------------------------------------------
def build_dashboard(df):

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    fig.suptitle(
        "Iris Flower Analysis Dashboard",
        fontsize=18,
        fontweight="bold",
    )

    # 1. Scatter plot: sepal length vs petal length
    sns.scatterplot(
        data=df,
        x="sepal_length",
        y="petal_length",
        hue="species",
        alpha=0.7,
        ax=axes[0, 0],
    )

    axes[0, 0].set_title("Sepal Length vs Petal Length")

    # 2. Regression plot: petal width vs petal length
    sns.regplot(
        data=df,
        x="petal_width",
        y="petal_length",
        scatter_kws={"alpha": 0.4},
        line_kws={"color": "red"},
        ax=axes[0, 1],
    )

    axes[0, 1].set_title("Petal Width vs Petal Length")

    # 3. Histogram: petal length distribution
    sns.histplot(
        data=df,
        x="petal_length",
        bins=15,
        kde=True,
        ax=axes[0, 2],
    )

    axes[0, 2].set_title("Petal Length Distribution")

    # 4. Histogram: sepal length by species
    sns.histplot(
        data=df,
        x="sepal_length",
        hue="species",
        bins=15,
        multiple="stack",
        ax=axes[1, 0],
    )

    axes[1, 0].set_title("Sepal Length by Species")

    # 5. Correlation heatmap
    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        cbar=False,
        ax=axes[1, 1],
    )

    axes[1, 1].set_title("Feature Correlation")

    # 6. Average petal length by species
    avg = (
        df.groupby("species", as_index=False)["petal_length"]
        .mean()
    )

    sns.barplot(
        data=avg,
        x="species",
        y="petal_length",
        hue="species",
        legend=False,
        ax=axes[1, 2],
    )

    axes[1, 2].set_title("Average Petal Length by Species")

    for container in axes[1, 2].containers:
        axes[1, 2].bar_label(container, fmt="%.2f")

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    plt.savefig("plots/07_dashboard.png", dpi=150)
    plt.show()

    print("Saved dashboard -> plots/07_dashboard.png")


if __name__ == "__main__":

    try:
        data = load_iris_data()

        print("First 5 rows:")
        print(data.head())

        print("\nDataset shape:", data.shape)

        print("\nStatistical summary:")
        print(data.describe().round(2))

        print("\nSpecies counts:")
        print(data["species"].value_counts())

        matplotlib_basics(data)
        seaborn_analysis(data)
        build_dashboard(data)

        print("\nAll plots saved in the 'plots' folder.")

    except FileNotFoundError:
        print(
            "Error: iris.csv not found. "
            "Place it in the same folder as this Python script."
        )

    except (ValueError, pd.errors.ParserError) as error:
        print("Error:", error)
