import pickle
from pathlib import Path
import os
import sys

# Importing necessary list of datasets and preprocessing classes
from datasets import ALL_DATASETS
from preprocessing import Parser, SrcPreprocessing, ReportPreprocessing



def run_all():
    """
    Iterates through all defined datasets, processes bug reports and source files,
    stores the results, and saves the data to individual binary files.
    """
    
    # Dictionary to hold all processed data (optional, but good for summary)
    all_processed_data = {}

    for dataset in ALL_DATASETS:
        print(f"Starting preprocessing for dataset: {dataset.name.upper()}")

        # 2. Initialize Parser for the current dataset
        parser = Parser(dataset)

        processed_src = None
        processed_reports = None
        
        # --- Process Source Files (SRC) ---
        print(f"[SRC] Parsing source files from: {parser.src}")
        src_file = parser.src_parser()
        # Preprocess source files
        src_prep = SrcPreprocessing(src_file)
        src_prep.preprocess()
        processed_src = src_prep.src_files
        print(f"[SRC] Successfully processed {len(processed_src)} source files.")

        # --- Process Bug Reports (BUG) ---
        print(f"[BUG] Parsing bug reports from: {parser.bug_repo}")
        bug_reports = parser.report_parser()
        # Preprocess bug reports
        report_prep = ReportPreprocessing(bug_reports)
        report_prep.preprocess()
        processed_reports = report_prep.bug_reports
        print(f"[BUG] Successfully processed {len(processed_reports)} bug reports.")


        # 3. Store processed data for the current dataset in a dictionary
        dataset_data = {
            'source': processed_src,
            'report': processed_reports
        }
        all_processed_data[dataset.name] = dataset_data
            
        print("\n")

    # 5. save the aggregated data for all datasets
    aggregate_filename = 'all_datasets.pkl'
    print("Saving aggregated data for ALL datasets...")
    with open(aggregate_filename, 'wb') as f:
        pickle.dump(all_processed_data, f)
    print(f"-> All aggregated data saved successfully to: {aggregate_filename}")


if __name__ == '__main__':
    run_all()