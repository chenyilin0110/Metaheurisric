#!/bin/bash

# set parameters
iteration="50000"
city="51"
dim="2"

rm result/HC/HC*.txt

for i in $(seq 1 30)
do
	python src/HillClimbing.py $iteration $city $dim >> result/HC/HC-$i.txt
done