# astro-data-project
Analysis of Gaia DR3 stellar data with Python
# Astro Data Project

Analysis of 1000 stars from Gaia DR3 data using Python.

## What is this?

This project downloads and analyzes real astronomical data from the Gaia space telescope. It includes sky position plots, color-magnitude diagrams, and data filtering.

## Data

- Source: Gaia DR3 (gaiadr3.gaia_source)
- 1000 stars
- Columns: source_id, ra, dec, parallax, phot_g_mean_mag, bp_rp

## Tools

- Python 3.14
- pandas
- matplotlib

## What I did

1. Downloaded 1000 stars from Gaia Archive
2. Opened and explored the data with pandas
3. Plotted sky positions (RA vs Dec)
4. Plotted color-magnitude diagram (HR Diagram)
5. Filtered bright and nearby stars
