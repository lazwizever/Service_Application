import streamlit as st
# Display the app name as a title
title_text = "<h1 style='color: #1B9C85;'>BestMatch</h1>"
st.markdown(title_text, unsafe_allow_html=True)

def sign_up():
    # Add your sign-up logic here
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

    if topic == "As a service provider":
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


def sign_in():
    # Add your sign-in logic here
    st.write("Sign-in button clicked!")

def main():
   
    if st.button("Sign Up"):
        sign_up()

    if st.button("Sign In"):
        sign_in()


if __name__ == "__main__":
    main()
