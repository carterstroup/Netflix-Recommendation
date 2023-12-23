# Netflix Recommendation and Search Application

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/carterstroup/Netflix-Recommendation/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

## Features

- Search through nearly 10,000 different Netflix shows and movies (as of 2021).
- Find your favorite show by its name or get a list of shows in which you favorite actor appeared.
- In need of inspiration? Answer a few simple questions and the program will recommend the perfect show or movie based on your preferences.

## Getting Started

To run the program, simply follow the steps below in your terminal.

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/carterstroup/netflix-recommendation.git
    cd Netflix-Recommendation
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    cd Application
    python main.py
    ```

## Technical Details

The Netflix Search and Recommendation program is a multi-functional program that enables fast and simple searching across a CSV file containing information about Netflix shows and movies. In addition to the search functionality, the program also includes a recommendation feature, where it will sort the CSV file for the best matches after answering a few simple questions. 

This program showcases a thorough understanding of the Python language, especially pertaining to data structures and algorithms. The program uses the [Pandas](https://pandas.pydata.org/) package for file operations and includes many of its essential features. Additionally, the program utilizes memoization functionality and comprehensive for/while loops, dictionaries, lists, and input validation/management. The program runs in optimal linear time [O(n)] and is split across four fundamental scripts using modular functions.

**First Functional Date:** December 22, 2023

**Education Level at The Time of Development:** Junior in High School

## Credits

The data used in this program (last updated in 2021) was taken from the data science platform, [Kaggle](https://www.kaggle.com/), where it was created and maintained by [Shivam Bansal](https://www.kaggle.com/shivamb) under the [Public Domain License](https://creativecommons.org/publicdomain/zero/1.0/).

Find the database on the [Kaggle website here.](https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/carterstroup/Netflix-Recommendation/blob/main/LICENSE) file for details.