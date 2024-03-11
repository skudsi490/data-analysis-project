# Data Analysis Project

## **Project Structure**

data-analysis-project/
│
├── data_structure_analysis.py
│   ├── Import statements
│   ├── Data generation and manipulation
│   ├── Data analysis
│   └── Results presentation
│
└── temperature_analysis.py
├── Import statements
├── Data loading and preprocessing
├── Data analysis and visualization
└── Results presentation

# **Data Structure Analysis Documentation**

## **Overview**

**`data_structure_analysis.py`** is designed to analyze customer transaction data. It involves data generation, manipulation, and presentation of various analytical results, such as highest addition, lowest number of days, transactions with one person, transactions above a certain value before VAT, and the average price before VAT.

## **Dependencies**

- **pandas**: For data manipulation and analysis.
- **random**: For generating random data points.
- **prettytable**: For formatting tabular data in a visually appealing ASCII table format.
- **colorama**: For adding color to terminal output, enhancing readability.

## **Main Features**

1. **Data Generation**: Simulates a dataset of 20 transactions, including customer identifiers, number of persons involved, duration (in days), extra charges, total charges before VAT, and total payable amount after applying VAT.
2. **Data Presentation**: Utilizes **`PrettyTable`** to display the generated data in a table format in the console.
3. **Analytical Insights**:
    - Identifies the transaction with the highest additional charges.
    - Finds the transaction with the minimum number of days.
    - Counts transactions involving just one person.
    - Lists transactions where the total charges before VAT exceed 4000, along with customer identifiers and the number of persons.
    - Calculates the average charge before VAT across all transactions.
4. **Color-Coded Output**: Uses **`colorama`** to color-code the analytical results, improving distinction and readability.

# **Temperature Analysis Documentation**

## **Overview**

**`temperature_analysis.py`** focuses on analyzing temperature data across various months, loaded from an Excel file. It includes data preprocessing, statistical analysis, and both tabular and graphical presentation of results.

## **Dependencies**

- **pandas**: For loading, manipulating, and analyzing the Excel data.
- **matplotlib.pyplot**: For creating visualizations such as bar graphs and pie charts.
- **prettytable**: For creating ASCII tables to display average and maximum temperatures.
- **colorama**: For enhancing output readability through colored terminal text.

## **Main Features**

1. **Data Loading**: Imports temperature data from an Excel file into a pandas DataFrame.
2. **Data Preprocessing**: Excludes non-numeric columns to focus on temperature data.
3. **Statistical Analysis**: Computes average and maximum temperatures for each month.
4. **Tabular Presentation**: Uses **`PrettyTable`** to display average and maximum temperatures for each month in a clear, tabular format.
5. **Graphical Visualization**:
    - Presents average and maximum temperatures using bar graphs for an intuitive, visual comparison across months.
    - Displays the distribution of temperature ranges (0-10°C, 10-20°C, 20-30°C) in a pie chart, highlighting the proportion of temperatures falling within each range.
6. **Data Insights**: Provides a count of total temperature entries and a detailed analysis of temperature distribution across defined ranges.

## **Visualization Details**

- **Bar Graphs**: Different colors are used for average (skyblue) and maximum (orange) temperatures to facilitate distinction.
- **Pie Chart**: Utilizes color coding and explosion effect for the 0-10°C range to draw attention to the distribution of temperature ranges.