from pyspark.sql.functions import col, desc, to_timestamp, year, month, dayofweek, hour

def calculate_mode(df, column):
    """
    Calculates the mode (most frequent value) for a specific column.
    """
    mode_df = df.groupBy(column).count().orderBy(desc("count")).limit(1)
    if mode_df.count() > 0:
        return mode_df.collect()[0][0]
    return None

def drop_location_coordinates(df):
    """
    Drops coordinates and spatial features from the dataframe.
    """
    return df.drop("X Coordinate", "Y Coordinate", "Latitude", "Longitude")

def fill_missing_values(df):
    """
    Fills missing values in specific columns with their mode or a default placeholder.
    """
    ward_mode = calculate_mode(df.filter(col("Ward").isNotNull()), "Ward")
    community_area_mode = calculate_mode(df.filter(col("Community Area").isNotNull()), "Community Area")
    location_description_mode = calculate_mode(df.filter(col("Location Description").isNotNull()), "Location Description")
    location_mode = calculate_mode(df.filter(col("Location").isNotNull()), "Location")

    return df.na.fill({
        "Ward": ward_mode if ward_mode is not None else 0,
        "Community Area": community_area_mode if community_area_mode is not None else 0,
        "Location Description": location_description_mode if location_description_mode is not None else "Unknown",
        "Location": location_mode if location_mode is not None else "Unknown",
        "Case Number": "Unknown"
    })

def extract_datetime_features(df):
    """
    Converts Date column to timestamp and extracts Year, Month, DayOfWeek, and Hour features.
    """
    df = df.withColumn("Date", to_timestamp("Date", "MM/dd/yyyy hh:mm:ss a"))
    return df.withColumn("Year", year("Date")) \
             .withColumn("Month", month("Date")) \
             .withColumn("DayOfWeek", dayofweek("Date")) \
             .withColumn("Hour", hour("Date"))

def clean_data(df):
    """
    Performs full standardized cleaning workflow on the dataframe.
    """
    df = drop_location_coordinates(df)
    df = fill_missing_values(df)
    df = extract_datetime_features(df)
    return df
