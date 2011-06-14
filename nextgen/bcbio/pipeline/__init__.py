"""High level code for driving a next-gen analysis pipeline.

This structures processing steps into the following modules:

  - lane.py: Analyze a single fastq file.
    - demultiplex.py: Split file by barcodes, if required.
    - alignment.py: Align to a reference genome.

  - sample.py: Analyze a sample, which may consist of multiple lanes or
               barcoded samples on a lane.
    - merge.py: Merge and convert multiple sample files.
    - variation.py: Calculate SNP/indel variations for a sample.
    - qcsummary.py: Quality control, alignment metrics and summary information.
"""
