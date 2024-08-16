import pandas as pd
import re


# Function for calling homozygous by using variant frequency value
def extract_first_percentage(value):
    match = re.match(r"(\d+(\.\d+)?)%", value)
    return float(match.group(1)) if match else None


def analyze_variant_frequency(file_path):
    # upload tsv file
    data = pd.read_csv(file_path, sep='\t')

    # Converting "Variant Frequency" to numeric
    data['Variant Frequency Numeric'] = data['Variant Frequency'].apply(lambda x: extract_first_percentage(x))

    # Filtering homozygous
    filtered_data = data[data['Variant Frequency Numeric'] > 95]

    # Find Distributions
    polymorphism_type_distribution = filtered_data['Polymorphism Type'].value_counts()
    length_distribution = filtered_data['Length'].value_counts()
    protein_effect_distribution = filtered_data['Protein Effect'].value_counts()

    # distributions
    print("Polymorphism Type Distribution:\n", polymorphism_type_distribution)
    print("\nLength Distribution:\n", length_distribution)
    print("\nProtein Effect Distribution:\n", protein_effect_distribution)

    # Replace 'your_file_path_here.tsv' with the path to your TSV file


file_path = 'Exported File From Geneious.tsv'
analyze_variant_frequency(file_path)
