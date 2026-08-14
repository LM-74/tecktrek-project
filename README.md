# Delay Prediction Model for Deliveries
## Team 36's Project for Advanced Data Science & AI Level 1

**Team Members & ID**
- Baher Mohamed Attia - 2403247673
- Gharam Sadek - 23011402
- Heba Mohamed Hassan Mesbah - 2403241411
- Lina Ahmed Elsayed Ghazy - 2403244007
- Loay Mohamed Khalid Khalid - 23012117

**Links**
- [GitHub Repositiory]('https://github.com/LM-74/tecktrek-project')
- [LinkedIn Post]('https://google.com')

**How to use**
- To check analysis and complete workflow from loading and preprocessing to modeling and tuning, open `Notebooks/techtrek_project.ipynb`
- `Visuals/` folder contains all data/models analysis visualizations. 
- If you want to use the model and predict new data, run `Notebooks/prediction_use.py`
- Enter your data for each feature.
- Model will run the data through the pipeline and return the predicted label (Late or On Time / Early) and the probability of this prediction.

**Requirements**
- numpy
- pandas
- scikit-learn
- matplotlib
- plotly
- kaleido

*Note: if an error occurs with packages while running `techtrek_project.ipynb`, downgrade numpy to any version below 2.0.0 and upgrade kaleido and plotly.*

**Limitations**

Given more time, a streamlit dashboard would have been made to display results and visualizations neatly and give clean GUI to allow for more convenient prediction.