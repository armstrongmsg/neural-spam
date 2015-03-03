#!/bin/bash

ham_directory=$1
spam_directory=$2

HAM=-1
SPAM=1

ham_files="`find "$ham_directory"/*`"

for file in $ham_files
do
	echo "`python extract_attributes.py "$file" $HAM`,$HAM"
done

spam_files="`find "$spam_directory"/*`"

for file in $spam_files
do
	echo "`python extract_attributes.py "$file" $SPAM`,$SPAM"
done
