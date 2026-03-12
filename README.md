# tabtools
This repository contains an open source CLI for a quick pandas analysis on a dataset.

## About

This is a small project intended for the general audience and for myself to try out the pypi packaging.

## Usage

Basic information about a tabular file:

    tabtool example.csv

All information about a tabular file (includes all columns):

    tabtool example.parquet --all

Information about specific columns:

    tabtool example.orc --col A -c B -c C

Compression and performance information about a specific file (this is an experiment, the file will be converted into the most used formats, and iterative timing will be used to measure the memory and cpu time usage of each):

    tabtool example.csv.gz --perf

## Current progress:

All functionalities are implemented except for --perf.