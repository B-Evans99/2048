# 2048: a puzzle, not a game

To run the Jupyter notebook, navigate to the `jupyter notebook` directory and run the command: `jupyter-lab readme.md`

To run the experiments, run either `python3 trainControl.py` or `python3 trainVariation.py`. The number of overall generations has been set to 10 for your convenience; it takes at most 30 seconds to run either file.

`trainControl.py` and `trainVariation.py` both create a `.pkl` file. This file can be loaded during any future experiments, allowing you to train a model for many generations in multiple sittings. It can also be used to find the best solution for every generation.

To convert a `.pkl` file to a `.csv` of the best solution score for every generation, run `python3 loadData.py [filename]`

