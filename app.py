import streamlit as st
import pickle
import numpy as np

# Configure the page
def config_page():
    st.set_page_config(
                        page_title='Sales Prediction App',
                        page_icon='📊',
                        layout="wide",
                        initial_sidebar_state="auto",
                        menu_items={'About': 'dzakyrafliansyah@gmail.com'}
                        )

def display_page():
    st.title("Welcome to the Sales Prediction App!")
    st.write("❓ What you can do here?")
    st.write("✅ You can automatically adjust your TV budget plan to see how it may affect sales :)")
    st.write('---'*5)
    st.write('  ')
    st.write("You should input your TV budget plan")
    st.write("(remember, the unit is million dollar 😃)") 

# Load regression model
def load_model():
    with open('regression_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load model and data
model_data = load_model()
regressor = model_data['model']
tv_budget = model_data['tv_budget']
sales = model_data['sales']

def user_input():
    return st.number_input('Input here',
                            min_value=0, max_value=None,
                            key='st57981ts',
                            placeholder='Type any number'
                            )

def main():
    '''
        This function mainly to run all of functions above. I did this to make 
        the code more neat.
    '''
    # Re-call functions to configure the page
    config_page()
    display_page()

    # Store value of what user wants to input
    user_input_value = user_input()  

    # Create the calculate sales button
    calculate_sales_button = st.button('Calculate sales')

    # If users press the calculate sales button, the model will run immediately 
    if calculate_sales_button:
        X = np.array(user_input_value).reshape(-1,1)
        X = X.astype(float)
        sales_predicted_array = regressor.predict(X)
        sales_predicted = sales_predicted_array.flatten()[0].astype(float)
        st.write(f"Your predicted sales is ${sales_predicted.round(2)} (million)")

if __name__ == "__main__":
    main()
    
