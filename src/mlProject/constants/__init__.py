#To read my yml file 

"""from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")


# Now we need to import this into notebook, navigate to the 01_data ingestion notebook 


# To read my yml file 

#from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

# Check if paths exist
if not CONFIG_FILE_PATH.exists():
    raise FileNotFoundError(f"Config file not found at {CONFIG_FILE_PATH}")

if not PARAMS_FILE_PATH.exists():
    raise FileNotFoundError(f"Params file not found at {PARAMS_FILE_PATH}")

if not SCHEMA_FILE_PATH.exists():
    raise FileNotFoundError(f"Schema file not found at {SCHEMA_FILE_PATH}")

print("All files exist.")
print(f"Config file path: {CONFIG_FILE_PATH.resolve()}")"""


# To read my yml file 

from pathlib import Path

CONFIG_FILE_PATH = Path("/Users/hymaroshinigompa/Downloads/Data_Science_End_To_End_with_ML/config/config.yaml")
PARAMS_FILE_PATH = Path("/Users/hymaroshinigompa/Downloads/Data_Science_End_To_End_with_ML/params.yaml")
SCHEMA_FILE_PATH = Path("/Users/hymaroshinigompa/Downloads/Data_Science_End_To_End_with_ML/schema.yaml")

# Check if paths exist
if not CONFIG_FILE_PATH.exists():
    raise FileNotFoundError(f"Config file not found at {CONFIG_FILE_PATH}")

if not PARAMS_FILE_PATH.exists():
    raise FileNotFoundError(f"Params file not found at {PARAMS_FILE_PATH}")

if not SCHEMA_FILE_PATH.exists():
    raise FileNotFoundError(f"Schema file not found at {SCHEMA_FILE_PATH}")

print("All files exist.")
# print(f"Config file path: {CONFIG_FILE_PATH.resolve()}")

