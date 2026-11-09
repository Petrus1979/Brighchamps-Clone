import streamlit as st
import pandas as pd
from datetime import datetime, date, time

# App layout setup
st.set_page_config(page_title="BrightChamps Clone - Booking & Payments", page_icon="🚀", layout="wide")

# Initialize session state for tracking bookings
if "bookings" not in st.session_state:
    st.session_state.bookings = []

st.title("🚀 BrightChamps Style Online Academy")
st.write("Book Next-Gen Coding, AI, and Mathematics Classes Instantly.")
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📚 Browse Courses & Book", "💳 My Bookings & Payments", "🎓 Virtual Classroom"])

# ================= TAB 1: COURSE BROWSING & BOOKING =================
with tab1:
    st.header("Select a Premium Live Course")
    
    # Mock Course Data
    courses = {
        "Next-Gen Coding (Ages 6-16)": {"price": 49.99, "desc": "Learn Python, Scratch, and Game Development with 1-on-1 mentors.", "emoji": "💻"},
        "Artificial Intelligence & Robotics": {"price": 79.99, "desc": "Dive deep into Neural Networks, Computer Vision, and smart tech.", "emoji": "🤖"},
        "Financial Literacy for Kids": {"price": 39.99, "desc": "Master money management, budgeting, and basic economics early.", "emoji": "💰"}
    }
    
    # Display Courses side-by-side
    cols = st.columns(3)
    for i, (course_name, details) in enumerate(courses.items()):
        with cols[i]:
            st.markdown(f"### {details['emoji']} {course_name}")
            st.markdown(f"**Price:** ${details['price']} per session")
            st.write(details['desc'])
            st.markdown("---")

    # Booking Form Section
    st.subheader("📆 Schedule Your Session")
    
    col_form1, col_form2 = st.columns(2)
    with col_form1:
        selected_course = st.selectbox("Choose your course:", list(courses.keys()))
        student_name = st.text_input("Student Full Name:", placeholder="e.g. John Doe")
        parent_email = st.text_input("Parent Email Address:")
        
    with col_form2:
        booking_date = st.date_input("Select Date:", min_value=date.today())
        booking_time = st.time_input("Select Time Slot (Available hourly):", value=time(14, 0))
    
    # Payment Gateway Integration Simulator
    st.markdown("### 💳 Secure Checkout")
    st.caption("Payments secured via Stripe integration placeholder.")
    
    card_name = st.text_input("Name on Card")
    col_card1, col_card2 = st.columns(2)
    with col_card1:
        card_num = st.text_input("Card Number", max_chars=16, type="password", placeholder="XXXX XXXX XXXX XXXX")
    with col_card2:
        card_cvv = st.text_input("CVV", max_chars=3, type="password", placeholder="123")

    if st.button("Confirm Appointment & Pay"):
        if not student_name or not parent_email or not card_num:
            st.error("Please complete all student information and payment fields.")
        else:
            # Record booking entry
            new_booking = {
                "course": selected_course,
                "student": student_name,
                "date": str(booking_date),
                "time": str(booking_time),
                "amount": courses[selected_course]["price"],
                "status": "Paid Successfully ✅"
            }
            st.session_state.bookings.append(new_booking)
            st.balloons()
            st.success(f"Success! ${courses[selected_course]['price']} processed. Class booked for {booking_date} at {booking_time}.")

# ================= TAB 2: MY BOOKINGS & PAYMENTS =================
with tab2:
    st.header("📋 Your Dashboard")
    if not st.session_state.bookings:
        st.info("No active bookings found. Browse courses to schedule your first session.")
    else:
        df_bookings = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df_bookings, use_container_width=True)
        st.caption("A confirmation email and classroom invitation link have been sent to the registered parent email address.")

# ================= TAB 3: VIRTUAL CLASSROOM =================
with tab3:
    st.header("📹 Enter Live Classroom")
    st.write("When it is time for your scheduled class, log into your live mentor panel below:")
    
    live_cols = st.columns([2, 1])
    with live_cols[0]:
        st.subheader("Live Interaction Panel")
        st.video("https://youtube.com") # Replace with live WebRTC or Zoom Web SDK embed
    with live_cols[1]:
        st.subheader("Classroom Chat")
        st.text_area("Chat with Mentor:", value="Mentor: Welcome to class!\nStudent: Hi, ready to learn python!", height=250)
        st.text_input("Type message...", key="live_chat_input")
        st.button("Send", key="send_live_chat")
