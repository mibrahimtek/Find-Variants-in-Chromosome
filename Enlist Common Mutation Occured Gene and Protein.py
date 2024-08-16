import pandas as pd
from tabulate import tabulate

# Concert Variant Frequency > 95% to Numeric
def filter_mutations_adjusted(df):
    df['Variant Frequency Numeric'] = pd.to_numeric(df['Variant Frequency'].str.split(' -> ').str[0].str.rstrip('%'), errors='coerce')
    return set(df[df['Variant Frequency Numeric'] > 95]['Minimum'])

def load_and_process_data(chromosome_number):
    # Load the datasets
    m3_9_path = f'Chromosome 1 M3.9 Filtered.tsv.tsv'
    m3_15_path = f'Chromosome 1 M3.15 Filtered.tsv'
    ebr3_path = f'Chromosome 1 EBR3 Filtered.tsv.tsv'

    # Reading the TSV files
    m3_9_df = pd.read_csv(m3_9_path, sep='\t')
    m3_15_df = pd.read_csv(m3_15_path, sep='\t')
    ebr3_df = pd.read_csv(ebr3_path, sep='\t')

    # Extract Homozygous and filter the positions
    m3_9_mutations = filter_mutations_adjusted(m3_9_df)
    m3_15_mutations = filter_mutations_adjusted(m3_15_df)
    ebr3_mutations = filter_mutations_adjusted(ebr3_df)

    # Determine the common mutations between M3.9 and M3.15 but not in EBR3
    common_mutations = (m3_9_mutations & m3_15_mutations) - ebr3_mutations

    # Filtering the original datasets to get the detailed information for these positions
    common_m3_9_m3_15_not_ebr3 = pd.concat([
        m3_9_df[m3_9_df['Minimum'].isin(common_mutations)],
        m3_15_df[m3_15_df['Minimum'].isin(common_mutations)]
    ])

    # Removing duplicates in case there are any, based on 'Minimum' column for "Position Range" to ensure unique mutations are listed
    common_m3_9_m3_15_not_ebr3_unique = common_m3_9_m3_15_not_ebr3.drop_duplicates(subset=['Minimum'])

    # Add a column that indicates the position range (Minimum-Maximum)
    common_m3_9_m3_15_not_ebr3_unique['Position Range'] = common_m3_9_m3_15_not_ebr3_unique.apply(lambda row: f"{row['Minimum']}-{row['Maximum']}", axis=1)

    # Enlist Info regarding mutations
    requested_columns = ['gene', 'Position Range', 'Change', 'CDS Position', 'Codon Change', 'Amino Acid Change', 'Protein Effect', 'product']
    common_mutations_info = common_m3_9_m3_15_not_ebr3_unique[requested_columns].reset_index(drop=True)

    return common_mutations_info

# Example usage:
chromosome_number = 4  # Change the chromosome number here for each analysis
common_mutations_info_ch4 = load_and_process_data(chromosome_number)

print(tabulate(common_mutations_info_ch4, headers='keys', tablefmt='psql', showindex=False))
