# Olympic Games Data Analysis Tool

## Overview
This project is a sophisticated analysis tool designed for delving into the rich history and statistics of the Olympic Games. It utilizes a Python-based web interface to offer users an interactive and intuitive way to explore various aspects of the Olympics, from medal tallies to athlete performance metrics. The tool leverages powerful libraries such as Pandas for data manipulation, Plotly and Seaborn for dynamic visualizations, and Streamlit for web application deployment.

## Features

### Country-wise Medal Tally and Performance Analysis
- Users can select any country to view its overall performance in the Olympic Games over the years.
- The feature displays a line chart of the country's medal tally over time and a heatmap showcasing the country's excellence in different sports.

### Athlete-wise Analysis
- This feature highlights the most successful athletes, allowing users to explore the top performers and their achievements.
- Users can filter athletes by sport to view specific insights.

### Distribution of Athlete Demographics
- Analyze the distribution of ages, weights, and heights of athletes, offering insights into the physical attributes that correlate with success in various sports.
- Includes comparative analysis of men's and women's participation over the years, showcasing trends and progress in gender diversity.

### Interactive Visualizations
- The tool provides interactive charts and graphs, such as line charts for medal tallies, heatmaps for country performance in sports, and scatter plots for analyzing athlete demographics.
- Users can interact with the visualizations to filter data and gain deeper insights.

## Technical Structure

### Web Application Interface (`app.py`)
- The front end of the tool, built with Streamlit, provides a user-friendly interface for interacting with the data analysis features.

### Helper Module (`helper.py`)
- Contains functions for data processing and analysis, supporting the web application with necessary data manipulation capabilities.
The Olympic Games data analysis project encompasses several key features designed to analyze and visualize data from the Olympic Games. Here's a summary of its main components and functionalities:

1. **Data Preprocessing**:
   - Merges athlete events and region data from CSV files.
   - Filters data for the Summer Olympics.
   - Removes duplicates and encodes the 'Medal' column into dummy variables for analysis.

2. **Interactive Web Application**:
   - Utilizes Streamlit for creating an interactive web application.
   - Offers a sidebar menu for selecting different types of analyses: Medal Tally, Overall Analysis, Country-wise Analysis, and Athlete Wise Analysis.

3. **Data Analysis and Visualization**:
   - **Medal Tally**: Allows users to view the medal tally for selected countries and years.
   - **Overall Analysis**: Displays top statistics such as the number of editions, host cities, sports, events, athletes, and participating nations. Includes visualizations for the participation of nations over time, the total number of events, and the total number of athletes.
   - **Country-wise Analysis**: Provides insights into the medal tally over years for a selected country and visualizes the sports in which the country excels.
   - **Athlete Wise Analysis**: Analyzes the distribution of athletes' ages, including comparisons based on medal type. Also, visualizes the distribution of athletes' weight and height, and compares male vs. female participation over the years.

4. **Visualization Tools**:
   - Employs Plotly for line charts and Seaborn for heatmaps to visualize trends, distributions, and other insights.

5. **Helper Functions**:
   - Contains functions to fetch medal tally, list countries and years, analyze participation over time, identify most successful athletes and countries in specific sports, and more.

This project leverages Python's powerful libraries such as Pandas for data manipulation, Plotly and Seaborn for visualization, and Streamlit for web application development, providing a comprehensive tool for Olympic Games data analysis.
## Getting Started


https://github.com/user-attachments/assets/53641e03-ce99-4847-9502-177b47676876

![image](https://github.com/user-attachments/assets/171ab5d2-e04d-4297-ba5b-e4da6c8c07b0)

### Prerequisites
- Python 3.8 or higher
- Libraries: Pandas, Plotly, Seaborn, Streamlit

### Installation
1. Clone the repository:git clone https://github.com/yourusername/olympic-games-analysis.git
2. 2. Install the required libraries:pip install pandas plotly seaborn streamlit
   3.3. Run the Streamlit application:streamlit run app.py
## Usage
After launching the application, navigate through the sidebar to access different analysis features. Select the desired country, sport, or athlete from the dropdown menus to display the corresponding data visualizations and insights.

## Contributing
Contributions to enhance the functionality or improve the codebase are welcome. Please follow the standard fork-and-pull request workflow.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
