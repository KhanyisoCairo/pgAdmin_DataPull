import psycopg2
import pandas as pd
from datetime import datetime

# Define the database connection parameters
host = 's3a-prod-vm-1.southafricanorth.cloudapp.azure.com'
port = '5432'
database = 's3datastore'
user = 'postgres'
password = '6]]~-.VP1s@Vl35060"QN'

def retrieve_and_process_data(start_date, end_date, table_name):
    # Establish a database connection
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
        connect_timeout=1200  # Adjust the timeout value as needed
    )

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Initialize an empty list to store the results
        results = []

        # Generate and execute the SQL query
        sql_query = f"""
        SELECT
            *
        FROM
            {table_name}
        WHERE
            when_captured >= '{start_date}'
            AND
            when_captured < '{end_date}'
        """

        cursor.execute(sql_query)

        # Fetch and store the results
        results.extend(cursor.fetchall())

        # Process the results as needed
        for row in results:
            print(row)

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

    # Create a DataFrame from the results
    # df = pd.DataFrame(results, columns=["ore_detector_duration_0", "ore_segmenter_duration_0", "total_duration_0", "when_captured"])
    df = pd.DataFrame(results)
    # Convert datetime values to timezone-unaware
    df["when_captured"] = pd.to_datetime(df["when_captured"]).dt.tz_localize(None)

    # Save the DataFrame to an Excel file
    excel_file = f"{table_name}.xlsx"
    df.to_excel(excel_file, index=False)
