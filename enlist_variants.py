import pandas as pd
from tabulate import tabulate

# Variant Frequency > 95% to Numeric
def filter_mutations_adjusted(df):
    df['Variant Frequency Numeric'] = pd.to_numeric(df['Variant Frequency'].str.split(' -> ').str[0].str.rstrip('%'), errors='coerce')
    return set(df[df['Variant Frequency Numeric'] > 95]['Minimum'])

def load_and_process_data(chromosome_number):
    # Load the datasets
    Sample_A = f'Sample A File Path Here.tsv'
    Sample_B = f'Sample B File Path Here.tsv'
    Sample_C = f'Sample C File Path Here.tsv'

    # Reading the .tsv from Geneious Prime at Step 4
    Sample_A_df = pd.read_csv(Sample_A, sep='\t')
    Sample_B_df = pd.read_csv(Sample_B, sep='\t')
    Sample_C_df = pd.read_csv(Sample_C, sep='\t')

    # Call Homozygous and filter mutation positions
    Sample_A_mutations = filter_mutations_adjusted(Sample_A_df)
    Sample_B_mutations = filter_mutations_adjusted(Sample_B_df)
    Sample_C_mutations = filter_mutations_adjusted(Sample_C_df)

    # Determine the common mutations between Sample A and Sample B but not in Sample C
    common_mutations = (Sample_A_mutations & Sample_B_mutations) - Sample_C_mutations

    # Filtering the original datasets to get the detailed information for these positions
    common_Sample_A_Sample_B_not_Sample_C = pd.concat([
        Sample_A_df[Sample_A_df['Minimum'].isin(common_mutations)],
        Sample_B_df[Sample_B_df['Minimum'].isin(common_mutations)]
    ])

    # Removing duplicates in case there are any, based on 'Minimum' column for "Position Range" to ensure unique mutations are listed
    common_Sample_A_Sample_B_not_Sample_C_unique = common_Sample_A_Sample_B_not_Sample_C.drop_duplicates(subset=['Minimum'])

    # Add a column that indicates the position range (Minimum-Maximum)
    common_Sample_A_Sample_B_not_Sample_C_unique['Position Range'] = common_Sample_A_Sample_B_not_Sample_C_unique.apply(lambda row: f"{row['Minimum']}-{row['Maximum']}", axis=1)

    # Enlist Mutations with desired column
    requested_columns = ['gene', 'Position Range', 'Change', 'CDS Position', 'Codon Change', 'Amino Acid Change', 'Protein Effect', 'product']
    common_mutations_info = common_Sample_A_Sample_B_not_Sample_C_unique[requested_columns].reset_index(drop=True)

    return common_mutations_info

# run
chromosome_number = 1  # Change the chromosome number here for each analysis
common_mutations_info_ch = load_and_process_data(chromosome_number)

print(tabulate(common_mutations_info_ch, headers='keys', tablefmt='psql', showindex=False))
