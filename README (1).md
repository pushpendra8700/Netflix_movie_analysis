
# 📊 Netflix Genre Analysis

This project explores and analyzes a Netflix dataset to uncover insights into genre distribution, content trends, and more. It utilizes data cleaning, visualization, and exploratory data analysis (EDA) techniques using Python libraries.

## 🧠 Objectives

- Analyze the distribution of content across various genres.
- Visualize trends in Netflix content over the years.
- Understand the popularity and characteristics of genres.
- Extract useful business insights to support content strategy.

## 🗃️ Dataset

The dataset includes information about:

- Title, type (Movie/TV Show)
- Director, cast, country
- Release year, rating
- Duration, genres (listed as “listed_in”)
- Description and more

> Note: Unnecessary columns were removed during preprocessing for better analysis.

## 🛠️ Tools & Technologies

- **Python** (Pandas, NumPy)
- **Matplotlib** & **Seaborn** (for data visualization)
- **Jupyter Notebook** (for analysis workflow)

## 📈 Key Steps

1. **Data Cleaning**
   - Dropped columns such as `show_id`, `description`, etc.
   - Renamed columns for readability (e.g., `listed_in` to `Genres`)
   - Managed missing values and duplicates

2. **Exploratory Data Analysis**
   - Analyzed type-wise content distribution
   - Examined content trends over time
   - Identified most common genres and top contributing countries

3. **Visualizations**
   - Bar plots, heatmaps, pie charts, and time-series graphs

## 🔍 Insights

- "Dramas" and "International Movies" are among the most frequent genres on Netflix.
- The United States leads in content production, followed by India and the United Kingdom.
- There has been a noticeable rise in TV Show releases over the past decade.

## 📁 File Structure

```
Netflix_Genre_Analysis/
│
├── Netflix_Genre_Analysis.ipynb   # Jupyter Notebook with full analysis
├── README.md                      # Project documentation
```

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/netflix-genre-analysis.git
   ```
2. Open the notebook in Jupyter:
   ```bash
   jupyter notebook Netflix_Genre_Analysis.ipynb
   ```
3. Run all cells to see the full analysis and visualizations.

## 🙋‍♂️ Author

**PUSHPENDRA**  
📧 Email: ak422979@gmail.com  
🔗 LinkedIn: [https://www.linkedin.com/in/pushpendra87/](https://www.linkedin.com/in/pushpendra87/)
