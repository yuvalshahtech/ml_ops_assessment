import pandas as pd
#AFTER LOADING THE DATA, CHECK IF THE DATA ONLY HAS ONE ROW, IF SO CHECK IF IT HAS COMMAS, IF IT HAS COMMAS USE THEN AS SEPARATE COLUMNS, AND ALSO SPLIT THE DATA BASED ON THAT
def load_and_validate_data(input_file):
    if not input_file.lower().endswith('.csv'):
        raise ValueError(f"Input file '{input_file}' must have a .csv extension.")
    try:
        data = pd.read_csv(input_file)
        if len(data.columns) == 1 and "," in data.columns[0]:
            column_names = data.columns[0].split(",")
            split_data = data.iloc[:, 0].str.split(",", expand=True)
            split_data.columns = column_names
            data = split_data
    except FileNotFoundError:
        raise ValueError(f"Input file '{input_file}' not found.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"Input file '{input_file}' is empty.")
    except pd.errors.ParserError as e:
        raise ValueError(
            f"Invalid CSV format in '{input_file}'. "
            f"Please check the file formatting.\n\n"
            f"Details:\n{e}"
        ) from e
    except Exception as e:
        raise ValueError(
            f"Unexpected error while reading '{input_file}'. "
            f"Please check the file permissions and encoding.\n\n"
            f"Details:\n{e}"
        ) from e
    if data.empty:
        raise ValueError(f"Input file '{input_file}' contains no data rows.")
    data.columns = data.columns.str.lower()
    if "close" not in data.columns:
        raise ValueError(
            f"Missing required column 'close' in input file '{input_file}'."
        )
    return data