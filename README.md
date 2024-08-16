# Find-Variants-in-Chromosome

SNP Mapping with Illumina Data which mapped in GeneiousPrime and Python
 
**1. Before the starting**
1. Download all plugins in Geneious Prime (Tools → Plugin)
2. Download the reference genome chromosome by chromosome in the NCBI Tab.

**2. Processing Raw Data**
3. Move to raw sequence files “.fastqsanger” into the Geneious Prime. For example, sequence file names can be EBR3-[R1.fastq.gz].fastqsanger and EBR3-[R2.fastq.gz].fastqsanger for individual
4. Select the file and click Trim using BBDuk in the search tab after the find.
5. Adjust the settings (most probably default) like below
6. It will give your_file_name (trimmed) file. Select this file and search Error Correct & Normalize Reads. Set the adjustments
7. It will give your_file_name **(trimmed)(normalized & error corrected)** file. In the # Sequences column, you should see fewer sequences number in the normalized file than original file.

**3. Map with the Reference**
1. Select two files that are your_filename_1 (trimmed)(normalized & error corrected) and your_filename_2 (trimmed)(normalized & error corrected) by pressing Ctrl
2. Click the Align/Assemble tab and find Map to References
3. Select your first chromosome from downloaded reference genomes in the chosen tab and set adjustment.
4. The process can be monitored in Operation Tab
5. After the running of the mapping, this file appears
6. This process is repeated for each chromosome

**4. Find SNPs and Export File**
1. Select a derived file from Map to reference and search Find Variations/SNPs
2. Adjust the settings below and run.
3. After the running, the annotations of variants should be seen in the viewer.;
4. After that, click the annotations click Track, and select Variants. Click the columns and enable them by clicking below that are recommended
Document Name
Minimum
Maximum
Length
Change
Polymorphism Type
Amino Acid Change
CDS Position
Codon Change
gene
product
Protein Effect
Variant Frequency
according to order from left to right. Click the minimum to order from start to end of the positions in the chromosome.
5. Export the table in .tsv format



**5. Find the Distributions of Mutation**
1. Move the exported .tsv file into the IDLE project files
2. Copy the file name with the extension and paste it into the code available under the Distribution_SNP_from_csv 
3. The results which can be copied & pasted into the .xlsx (excel file) for further analysis appear in the console

**6. Construct Venn Diagram**
1. Use extracted `.tsv` files which are extracted in "Step 4 Find SNPs and Export File"
2. Run the code -two_samples_venn- or -two_samples_venn- for each chromosome and save Venn diagram 

**7. Enlist the Common Genes from Venn Diagram**
1. Use extracted `.tsv` files which are extracted in Step 4 "Find SNPs and Export File"
2. Run the code -enlist_variants-for each chromosome 


