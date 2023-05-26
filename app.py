import streamlit as st

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
    
    # Get the username and password from the user
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Check if the login button is clicked
    if st.button('Login'):
        # Perform login authentication and user validation here
        # Replace the condition with your actual login logic
        if username == 'admin' and password == 'password':
            st.success('Logged in successfully!')
        else:
            st.error('Invalid credentials')

    st.write('Don\'t have an account?')
    if st.button('Sign up'):
        # Perform sign up action or navigate to sign up page
        topic = st.radio("Select your profile", ("As a customer", "As a service provider"))

        if topic == "As a customer":
            st.subheader("Customer Info")
            st.text_input("Customer Name")
            st.text_input("NIC")
            st.text_input("Address")
            st.text_input("Mobile Number")

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
    if st.button("Save"):
        # Perform save operation or store the input values
        # You can access the values entered in the input fields and perform necessary actions here
        pass

def clear_button():
    if st.button("Clear"):
        # Clear the input fields or reset the values
        # You can reset the input field values or perform necessary actions here
        pass


# Run the login form
login_form()