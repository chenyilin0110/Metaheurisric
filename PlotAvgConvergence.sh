#!/bin/bash

# set parameters
iteration="5000"
city="51"
dim="2"
neighbor="7"
temperature="1000"
rate="0.95"

rm result/Avg/*.txt
rm result/HC/HC*.txt
rm result/SA/SA*.txt

for i in $(seq 1 30)
do
	python src/HillClimbing.py $iteration $city $dim >> result/HC/HC-$i.txt
	python src/SimulatedAnnealing.py $iteration $city $dim $neighbor $temperature $rate >> result/SA/SA-$i.txt
done

run="30"
which_algo="HC"
python src/CalculateAvg.py $which_algo $run $iteration >> result/Avg/$which_algo.txt

which_algo="SA"
python src/CalculateAvg.py $which_algo $run $iteration >> result/Avg/$which_algo.txt

gnuplot src/draw/plot.plt