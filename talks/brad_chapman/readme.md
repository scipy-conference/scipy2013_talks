# Title: Quantifiable and scalable detection of genomic variants

## Authors:

- Brad Chapman, Bioinformatics Core, Harvard School of Public Health
- Rory Kirchner
- Oliver Hofmann
- Winston Hide

## Track: Bioinformatics

## Abstract:

bcbio-nextgen is an automated, scalable pipeline for detecting genomic variants
from large-scale next-generation sequencing data. It organizes multiple
best-practice tools for alignment, post-processing and variant calling into a
single, easily configurable pipeline. Users specify inputs and parameters in a
configuration file and the pipeline handles all aspects of software and data
management. Large-scale analysis run in parallel on compute clusters using
IPython and on cloud systems using StarCluster. The goal is to create a
validated and community maintained pipeline for automated variant calling,
allowing researchers to focus on answering biological questions.

Our talk will describe the practical challenges we face in scaling the system to
handle large whole genome data for thousands of samples. We will also discuss
current work to develop a variant reference panel and associated grading scheme
that ensures reproducibility in a research world with rapidly changing
algorithms and tools. Finally we details plans for integration with STORMseq, a
user-friendly Amazon front end, designed to make the pipeline available to
non-technical users.

The presentation will show how bringing together multiple open-source
communities provides infrastructure that bridges technical gaps and moves
analysis work to higher-level challenges.

## Materials:

- Talk slides: https://github.com/chapmanb/bcbb/tree/master/talks/scipy2013_bcbio_nextgen
- GitHub repository: https://github.com/chapmanb/bcbio-nextgen

