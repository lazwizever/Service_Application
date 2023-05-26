import streamlit as st
from flask import Flask
import mysql.connector
from PIL import Image

app = Flask(__name__)
#CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MYSQL_HOST'] = 'database-1.c3kt6gsj5iwk.ap-southeast-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'appleGaha'
app.config['MYSQL_DB'] = 'serviceApplication'

# connect mysql database
conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Add custom CSS to style the title
st.markdown(
    """
    <style>
    .green-title {
        color: green;
        font-size: 60px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the green color title
st.markdown('<h1 class="green-title">BestMatch</h1>', unsafe_allow_html=True)


# Add custom CSS to center-align the subheader
st.markdown(
    """
    <style>
    .center-subheader {
        text-align: center;
        font-size: 26px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the centered subheader
st.markdown('<h2 class="center-subheader">Login</h2>', unsafe_allow_html=True)


# Create the login form
def login_form():
    cursor = conn.cursor()
    # Get the username and password from the user
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')


    login = st.button("Login", use_container_width=True)

    # Check if the login button is clicked
    if login:
       query = 'SELECT * FROM Login WHERE username=%s AND password=%s'
       values = (username,password)
       cursor.execute(query, values)
       response = cursor.fetchone()
        # Perform login authentication and user validation here
        # Replace the condition with your actual login logic
       if response :
            st.success('Logged in successfully!')
       else:
            st.error('Invalid credentials')

    st.write('Don\'t have an account?')
    if st.button('Sign up'):
        # Perform sign up action or navigate to sign up page
        topic = st.radio("Select your profile", ("As a customer", "As a service provider"))

        if topic == "As a customer":
            st.subheader("Customer Info")
            input1 =st.text_input("Customer Name")
            input2 =st.text_input("NIC")
            input3 =st.text_input("Address")
            input4 =st.text_input("Mobile Number")

            col1, col2, col3 = st.columns(3)
            with col2:
                save_button()
            with col3:
                clear_button()

        # Add Topic A logic here

        elif topic == "As a service provider":
            st.subheader("Service Provider Info")
            st.text_input("Service Provider Name")
            selected_option = st.selectbox("Service Type", ["Vehicle repairing", "Electric repairing", "Repair broken pipes"])
            st.text_input("NIC")
            st.text_input("Address")
            st.text_input("Mobile Number")
                    # Add Topic B logic here

def save_button():
    if st.button("Save", use_container_width=True):
        # Perform save operation or store the input values
        # You can access the values entered in the input fields and perform necessary actions here
        
        cursor.execute('INSERT INTO Customer (customerName ,customerNIC , customerAddress , mobileNumber ) VALUES (%s, %s, %s, %s)', (customerName, customerNIC, customerAddress, mobileNumber))
        conn.commit()
        st.success('Customer added successfully')
        pass

def clear_button():
    if st.button("Cancel", use_container_width=True):
        # Clear the input fields or reset the values
        # You can reset the input field values or perform necessary actions here
        pass


# Run the login form
login_form()


st.markdown(
    """
    <style>
    .service provider {
        color: white;
        font-size: 40px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the green color title
st.markdown('<h1 class="service provider">Pick up your service type</h1>', unsafe_allow_html=True)

# Create a dropdown menu
option = st.selectbox('Pick up', ("Vehicle repairing", "Electric repairing", "Repair broken pipes"))


logo_url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
logo_url1 ="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
# Display the logo
logo = st.image(logo_url)
logo1 = st.image(logo_url1)

# Define the profiles and corresponding logos
profiles = {
    'Vehicle repairing': [logo1, logo1, logo1],
    'Electric repairing': [logo1, logo1, logo1],
    'Repair broken pipes': [logo1, logo1, logo1],
}

# Get the selected profiles based on the selected option
# Get the selected profiles based on the selected option
selected_profiles = profiles.get(option, [])

