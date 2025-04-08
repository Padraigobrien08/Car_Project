# Car Price Rating & Market Comparison Project

This project is an experimental attempt to recreate a pricing feature inspired by a second-hand car website. The original feature rated the price of a car relative to the market, helping users quickly assess whether a listed price was competitive. In this project, I combine web scraping, data exploration, preprocessing, feature engineering, and machine learning to build a similar pricing comparison tool.

> **Note:** A screenshot of the original feature is included in the repository to give context to the inspiration behind this project.

## Project Structure

- **WebScraping.py**  
  This Python script uses Selenium and BeautifulSoup to scrape HTML content from a second-hand car website. It navigates to the target URL, waits for the page elements to load, and extracts specific content (e.g., header elements) for further processing.

- **EDA.ipynb**  
  A Jupyter Notebook dedicated to Exploratory Data Analysis (EDA) on the car dataset. It:
  - Loads the CSV file containing car data.
  - Explores data shape, data types, and missing values.
  - Generates statistical summaries and various visualizations (e.g., histograms, scatter plots, box plots) to understand distributions and relationships (like mileage, year, and price).

- **Preprocessing.ipynb**  
  This Notebook cleans and preprocesses the raw dataset. Key steps include:
  - Extracting relevant columns and handling missing values.
  - Converting currency symbols and mileage units into numerical values.
  - Restructuring and normalizing the dataset for subsequent analysis.

- **Feature Encoding.ipynb**  
  Here, feature engineering is performed on the cleaned dataset:
  - Filtering records (e.g., price above a certain threshold).
  - Calculating new features such as **Depreciation** (based on normalized average price per make) and **Wear** (mileage per year).
  - Normalizing numerical columns using techniques like MinMax Scaling.
  - Mapping and encoding categorical features to prepare the data for modeling.
  - The processed data is exported as a CSV file for modeling.

- **FS_MF.ipynb**  
  This Notebook focuses on the machine learning modeling aspect:
  - Uses regression techniques (linear regression with hyperparameter tuning, random forest regression, polynomial regression, and XGBoost) to predict car prices.
  - Evaluates model performance with metrics such as RMSE (Root Mean Squared Error) and R-squared.
  - Demonstrates both simple and more advanced models to show how the pricing prediction can be optimized.

- **Screenshot/Image of the Feature**  
  A screenshot is provided (not as code) showing the original pricing comparison feature from the second-hand car website that inspired this project.

## Requirements

Ensure that you have Python 3.7+ installed. The following Python packages are required:

- **Web Scraping & Automation:**  
  `selenium`, `webdriver_manager`, `beautifulsoup4`
- **Data Handling & Visualization:**  
  `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Machine Learning:**  
  `scikit-learn`, `xgboost`
- **Other Dependencies:**  
  Any additional packages installed through pip, as needed.

You can install the required packages using a command like:

```bash
pip install selenium webdriver_manager beautifulsoup4 pandas numpy matplotlib seaborn scikit-learn xgboost
```

## Setup & Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YourUsername/YourCarProjectRepo.git
   cd YourCarProjectRepo
   ```

2. **Web Scraping:**

   - Configure the **WebScraping.py** script with the correct path to your ChromeDriver.
   - Run the script to scrape data from the target car website:

     ```bash
     python WebScraping.py
     ```

3. **Exploratory Data Analysis (EDA):**

   - Open the `EDA.ipynb` notebook in Jupyter Notebook or JupyterLab:
   
     ```bash
     jupyter notebook EDA.ipynb
     ```

   - Explore the data, review visualizations, and gain insights into the dataset.

4. **Data Preprocessing & Feature Engineering:**

   - Run **Preprocessing.ipynb** to clean and transform the raw car dataset.
   - Proceed with **Feature Encoding.ipynb** to engineer new features (such as depreciation and wear) and export the processed data (`Features_included.csv`).

5. **Modeling:**

   - Use **FS_MF.ipynb** to train various regression models that predict car prices.
   - This Notebook shows hyperparameter tuning with linear regression, as well as implementations of random forest, polynomial regression, and XGBoost to compare model performance.

## Project Goals

- **Price Comparison:** Provide users with a tool to evaluate whether a car's listed price is competitive when compared to the broader market.
- **Data-Driven Insights:** Use comprehensive EDA and feature engineering to understand the factors affecting car prices.
- **Machine Learning Application:** Apply several regression models to predict car prices based on various features, achieving high accuracy in estimating whether a car is over- or under-priced.

## Acknowledgments

- Inspired by features on second-hand car websites that dynamically rate car prices against current market trends.
- Thanks to the developers and contributors of the various open-source tools and libraries used in this project (e.g., Selenium, scikit-learn, XGBoost).
