import os
import pandas as pd

# Use environment variables for the data
data = {
    "Text": [
        os.getenv("TEXT1"),
        os.getenv("TEXT2"),
        os.getenv("TEXT3"),
        os.getenv("TEXT4"),
        os.getenv("TEXT5")
    ]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
