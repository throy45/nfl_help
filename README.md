# nfl_help : Helps you decide which game is worth watching

## Overview

(Work in progress, idea from 2021)

nfl_help is a Python/Django application that allows you to pull NFL game data and rank the games based on the number of turnovers (interceptions and fumbles). This app uses the nfl_data_py library to fetch NFL play-by-play data and then calculates the turnover count for each game. The ranked games are presented in descending order of turnovers.

## Features

- Pulls NFL play-by-play data for analysis.
- Ranks NFL games by the number of turnovers.
- Organizes the rankings by week.

## Prerequisites

Before you can run the app, make sure you have the following prerequisites installed:

- Python (version 3.x)
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/throy45/nfl_help.git
```


2. Change to the project directory:

```bash
cd nfl_help
```

3. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the app by executing the following command in your terminal:

```bash
python nfl_help.py
```

2. The app will fetch NFL play-by-play data, calculate turnovers, and rank the games by week.

3. The ranked games will be displayed, showing the games with the most turnovers at the top.

## Example Output

Here is an example of what the (initial) output might look like:

```yaml

Week 1:
1. Game: 2023_01_ARI_WAS, Turnovers: 5
2. Game: 2023_01_DET_SF, Turnovers: 4
3. Game: 2023_01_LV_CIN, Turnovers: 3

Week 2:
1. Game: 2023_02_CLE_PIT, Turnovers: 6
2. Game: 2023_02_NYJ_MIA, Turnovers: 5
3. Game: 2023_02_NE_NYG, Turnovers: 4

...
```

## License

This app is open-source and available under the MIT License.
Author

Thomas Roy

## Acknowledgments

Thanks to the developers of the nfl_data_py library for providing access to NFL data.
