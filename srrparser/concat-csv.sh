#!/bin/bash

cat *.csv | awk 'NR > 1' | awk 'BEGIN{FS=OFS=","}{$1="";sub(",","")}1' > output/gsm_srx_srr_ids.csv

