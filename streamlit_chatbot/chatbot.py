import streamlit as st
import pandas as pd 
import random
import time
import numpy as np
import datetime

from datetime import date

st.title("Study Buddy")

  
st.header("Welcome to the dashboard")

  
st.write("plan your studies and stay productive")

  
def setup_page():
    st.set_page_config(page_title = "Study Planner" , layout = "wide")

def display_header():
    st.title("Student Study Planner")
    st.write("Create a weekly study schedule easily")

def sidebar_settings():
    st.sidebar.header("Settings")

    name = st.sidebar.text_input("Your name")

    study_hours = st.sidebar.slider("Study hours per day", 1, 12, 3)
    
    return name, study_hours


def select_subjects():

    subjects = ["maths", "Add Maths", "chemistry", "physics", "biology", "english", "accounting", "econimics", "ICT"]

    selected_subjects = st.multiselect("Select Your Subjects", subjects)

    return selected_subjects

def create_weekly_plan(subjects):

    st.header("1 Weekly Study Planner")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    plan = []

    for day in days:

        st.subheader(day)

        subject = st.selectbox(f"Choose subject for {day}", subjects, key=day)

        time = st.time_input(f"Study time for {day}", key=f"time_{day}")

        plan.append({"Day": day, "Subject": subject, "Time": str(time)})

    return pd.DataFrame(plan)

def study_goals():

    st.header("Study goals")

    goal = st.text_area("Write your study goals")

    if st.button("Save Goals"):
        st.success("Goals Saved!")

    return goal

def progress_tracker(subjects):

    st.header("Progress Tracker")

    for subject in subjects:

        progress = st.slider(f"{subject} Progress", 0, 100, 50)

        st.progress(progress/100)


def motivation_quote():

    st.header("Quote of the day")

    quotes = ["Small progress every day leads to big results.",
        "Discipline beats motivation.",
        "Consistency creates success.",
        "Focus on improving daily."]

    import random

    quote = random.choice(quotes)

    st.info(quote)

def exam_countdown():

    st.header("Exam Countdown Timer")

    exam_date = st.date_input("Select your exam date")

    today = date.today()

    days_left = (exam_date - today).days

    st.info(f"{days_left} days left unitl your exam")

def ai_recommendations(subjects):

    st.header("AI Study Recommendations")

    for subject in subjects:

        if subject == "Mathematics":

            st.success("Practice 10 math questions daily.")

        elif subject == "Biology":

            st.success("Use diagrams and active recall.")

        elif subject == "Physics":

            st.success("Focus on formulas and problem solving.")

        elif subject == "Chemistry":

            st.success("Memorize reactions and practice calculations.")

        else:

            st.success(f"Revise {subject} consistently.")   

def study_calendar():

    st.header("Study Calendar")

    selected_date = st.date_input("Choose a study date")

    task = st.text_input("Enter task for this date")

    if st.button("Add To Calendar"):

        st.success(f"{task} added for {selected_date}")


def study_reminders():

    st.header("Study Reminders")

    reminder_subject = st.text_input("Reminder Subject")

    reminder_time = st.time_input("Reminder Time")

    if st.button("Set Reminder"):

        st.success(f"Reminder set for {reminder_subject} at {reminder_time}")

def study_analytics(subjects):

    st.header("Study Analytics")

    progress_data = {}

    for subject in subjects:

        progress = st.slider(f"{subject} Completion %",0,100,50,key=f"analytics_{subject}")

        progress_data[subject] = progress

    chart_data = pd.DataFrame({"Subject": list(progress_data.keys()),"Progress": list(progress_data.values())})

    st.bar_chart(chart_data.set_index("Subject"))


def ai_flashcard_generator(subjects):

    st.header("🧠 AI Flashcard Generator")

    selected_subject = st.selectbox(
        "Choose subject for flashcards",
        subjects)

    if st.button("Generate AI Flashcards"):

        flashcards = []

        
        if selected_subject == "Mathematics":

            flashcards = [{"question": "What is Pythagoras theorem?","answer": "a² + b² = c²"},{"question": "Formula for area of a circle?","answer": "πr²"}]

        
        elif selected_subject == "Biology":

            flashcards = [{"question": "What is photosynthesis?","answer": "Plants make food using sunlight."},{"question": "What organ pumps blood?","answer": "Heart"}]

        
        elif selected_subject == "Chemistry":

            flashcards = [{"question": "What is H2O?","answer": "Water"},{"question": "What is the pH of acids?","answer": "Less than 7"}]

        
        else:

            flashcards = [{"question": f"What is important in {selected_subject}?","answer": "Review your notes regularly."}]

        
        for card in flashcards:

            st.subheader(card["question"])

            st.success(card["answer"])


def revision_tracker(subjects):

    st.header("Exam Revision Tracker")

    for subject in subjects:

        completed = st.checkbox(f"{subject} Revision Completed")

        if completed:

            st.success(f"{subject} revision completed!")

def pomodoro_timer():

    st.header("🍅 Real Pomodoro Timer")

    minutes = st.slider("Select study duration (minutes)",1,60,25)

    start_button = st.button("Start Pomodoro")

    if start_button:

        total_seconds = minutes * 60

        timer_placeholder = st.empty()

        progress_bar = st.progress(0)

        for seconds_left in range(total_seconds,0,-1):

            mins = seconds_left // 60

            secs = seconds_left % 60

            timer_placeholder.subheader(f"⏰ Time Left: {mins:02d}:{secs:02d}")

            progress = (total_seconds - seconds_left)/ (total_seconds)

            progress_bar.progress(progress)

            time.sleep(1)

        timer_placeholder.subheader("✅ Pomodoro Session Complete!")

        st.balloons()





def daily_streak():

    st.header("🔥 Daily Study Streak")

    if "streak" not in st.session_state:

        st.session_state.streak = 1

    if st.button("I studied today"):

       st.session_state.streak += 1

    st.success(f"current study streak: {st.session_state.streak} days")


def task_checklist():

    st.header("✅ Study Checklist")

    tasks = [ "Revise Notes","Complete Homework","Practice Questions","Watch Tutorial","Review Flashcards"]

    for task in tasks:

        completed = st.checkbox(task)

        if completed:

            st.success(f"{task} completed!")


def study_history():

    st.header("📜 Study Session History")

    if "history" not in st.session_state:

        st.session_state.history = []

    subject = st.text_input(
        "Subject Studied"
    )

    duration = st.number_input(
        "Study Duration (minutes)",
        1,
        500
    )

    if st.button("Save Session"):

        session = {
            "Subject": subject,
            "Duration": duration,
            "Date": str(datetime.date.today())
        }

        st.session_state.history.append(
            session
        )

    if st.session_state.history:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(history_df)


def weakness_detection(subjects):

    st.header("📉 Subject Weakness Detection")

    weak_subjects = []

    for subject in subjects:

        score = st.slider(
            f"{subject} Confidence Level",
            0,
            100,
            50,
            key=f"weak_{subject}"
        )

        if score < 40:

            weak_subjects.append(subject)

    if weak_subjects:

        st.error(
            f"You should focus more on: {', '.join(weak_subjects)}"
        )

    else:

        st.success(
            "No major weak subjects detected!"
        )





def main():
    setup_page()

    display_header()

    

    name, study_hours = sidebar_settings()

    if name:
        st.success(f"Welcome, {name}!")

    st.write(f"You plan to study {study_hours} hours daily.")

    daily_streak()

    task_checklist()

    study_history()

    selected_subjects = select_subjects()

    exam_countdown()

    pomodoro_timer()

    study_calendar()

    study_reminders()

    



    if selected_subjects:

        plan_df = create_weekly_plan(selected_subjects)

        st.header("Your Schedule")

        st.dataframe(plan_df)

        progress_tracker(selected_subjects)

        study_analytics(selected_subjects)

        revision_tracker(selected_subjects)

        ai_recommendations(selected_subjects)

        ai_flashcard_generator(selected_subjects)

        weakness_detection(selected_subjects)
        
        


    study_goals()

    motivation_quote()
main()

      