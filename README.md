## Project objective 🎯
The main objective here is creating inference application (predict sales by TV budget). 
However, I also done the descriptive statistics in Google Colab. 

<a href="https://colab.research.google.com/drive/14k-y52PVv_2SAlYnuMg7BrXbSRfNcOBw#scrollTo=RrPDYdx9BD1T"><img align="left" src="https://github.com/raflidzaky/2024-March-stock_market_analysis/assets/104545005/3827e863-b0f8-437d-b29e-979c034f1350" alt="Google Colab Project" width="21px"/></a>  [**Google Colab Notebook**](https://colab.research.google.com/drive/14k-y52PVv_2SAlYnuMg7BrXbSRfNcOBw#scrollTo=RrPDYdx9BD1T)

This colab notebook contains detailed thought process, descriptive statistics, and modelling process (such as feature engineering). 
Streamlit link below will interactively predict sales based off model created on Colab notebook

<a href="https://sales-pred-app.streamlit.app/"><img align="left" src="https://github.com/raflidzaky/2024-March-stock_market_analysis/assets/104545005/81af49e7-1a07-4e61-8404-3b864343b6e3" alt="Google Colab Project" width="21px"/></a>  [**Streamlit Dashboard**](https://sales-pred-app.streamlit.app/)

## Tech stacks
![](https://img.shields.io/badge/Language-Python-informational?style=flat&logo=Python&color=FFD700)
</br>
![](https://img.shields.io/badge/Lib-Pandas-informational?style=flat&logo=Pandas&color=FFA500)
![](https://img.shields.io/badge/Lib-Matplotlib-informational?style=flat&logo=Plotly&color=FFC0CB)
![](https://img.shields.io/badge/Lib-Streamlit-informational?style=flat&logo=Streamlit&color=FF0000)
</br>

## Settings
### Configuration
First to do, you could clone this project **using Git**. This is how:
```
$git config --local user.name "your-display-name"
$git clone https://github.com/raflidzaky/2024-May-Kaggle-sales-analysis
$dir 
$cd 2024-May-Kaggle-sales-analysis
```

If you yet to install Streamlit, you could install and run it on the virtual environment. 
```
cd .venv\streamlit_app_management

pip install poetry

poetry shell
```

You are not required to do re-configuration from scratch (such as re-creating the ```pyproject.toml```), since the existing pyproject.toml will help you to keep up with dependencies I used.

### Run Streamlit on local
If you wanna run Streamlit on local, you just change direction to parent folder and do a command
```
cd \streamlit_app

streamlit run app.py
```
