#!/bin/bash

# set parameters
iteration="500"
city="51"
dim="2"
neighbor="7"
temperature="1000"
rate="0.95"

python src/HillClimbing.py $iteration $city $dim &
python src/SimulatedAnnealing.py $iteration $city $dim $neighbor $temperature $rate