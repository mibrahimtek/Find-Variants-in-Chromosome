import pandas as pd
import re
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Troubleshoot for % value in "Variant Frequency" by converting float
def extract_first_percentage(value):
    match = re.search(r"(\d+(\.\d+)?)%", value)
    return float(match.group(1)) if match else None

#  Calling homozygous by using"Variant Frequency" greater than 95%
def load_and_filter_data(file_path):
    data = pd.read_csv(file_path, sep='\t')
    data['Variant Frequency Numeric'] = data['Variant Frequency'].apply(lambda x: extract_first_percentage(x))
    filtered_data = data[data['Variant Frequency Numeric'] > 95]
    return filtered_data

# paths

Sample_A = 'File Path of Sample A'
Sample_B = 'File Path of Sample B'

# Load and filter data

data_Sample_A = load_and_filter_data(Sample_A)
data_Sample_B = load_and_filter_data(Sample_B)

# Extract unique positions from the "Minimum" column (position) for Venn diagram

positions_Sample_A = set(data_Sample_A['Minimum'])
positions_Sample_B = set(data_Sample_B['Minimum'])

# Construct Venn diagram
plt.figure(figsize=(10, 8))
venn2([positions_Sample_A, positions_Sample_B],
      ('Chromosome N Sample A', 'Chromosome N Sample B'))
plt.title("Venn Diagram of Mutations with Variant Frequency > 95% (Chromosome N)")
plt.show()
