import streamlit as st
import pandas as pd
import uuid
import os
from datetime import datetime

DATA_FILE = "game_data.csv"

# Initialize CSV
def load_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Entry ID", "Timestamp", "Game Name", "Region/State", "Rules/Steps", "Variations", "Contributor Name"])
        df.to_csv(DATA_FILE, index=False)
    else:
        df = pd.read_csv(DATA_FILE)
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_entry(data):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    save_data(df)

def delete_entry(entry_id):
    df = load_data()
    df = df[df["Entry ID"] != entry_id]
    save_data(df)

# App UI
st.set_page_config(page_title="Desi Game Rules Encyclopedia", layout="centered")
st.title("🎮 Desi Game Rules Encyclopedia")
st.markdown("Document and preserve traditional Indian games – rules, variations, and regional gems!")

# Form to add entry
with st.form("game_form"):
    game_name = st.text_input("Game Name (e.g., Pittu, Kabaddi, Kho-Kho)")
    region = st.text_input("Region/State (e.g., Andhra Pradesh, Punjab)")
    rules = st.text_area("Rules / Steps to Play")
    variations = st.text_area("Any Local Variations or Stories", "")
    contributor = st.text_input("Your Name (optional)", "")
    
    submitted = st.form_submit_button("➕ Submit Game")
    if submitted:
        if game_name.strip() and region.strip() and rules.strip():
            new_entry = {
                "Entry ID": str(uuid.uuid4()),
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Game Name": game_name.strip(),
                "Region/State": region.strip(),
                "Rules/Steps": rules.strip(),
                "Variations": variations.strip(),
                "Contributor Name": contributor.strip()
            }
            add_entry(new_entry)
            st.success("✅ Game added successfully!")
        else:
            st.error("❌ Please fill in the required fields: Game Name, Region, and Rules.")

# Load data
df = load_data()

# Button to remove duplicates
with st.expander("🧹 Clean Duplicate Entries"):
    if st.button("Remove duplicates"):
        before = len(df)
        df = df.sort_values(by="Timestamp")  # Keep the latest entry
        df = df.drop_duplicates(subset=['Game Name', 'Region/State'], keep='last')
        save_data(df)
        st.success(f"✅ Removed {before - len(df)} duplicate entries.")
        st.experimental_rerun()

# Display entries
st.subheader("📜 Encyclopedia Entries")
if df.empty:
    st.info("No entries yet. Be the first to contribute!")
else:
    for _, row in df.iterrows():
        with st.expander(f"🎲 {row['Game Name']} — {row['Region/State']}"):
            st.markdown(f"*How to Play:* {row['Rules/Steps']}")
            if row['Variations']:
                st.markdown(f"*Local Variations:* {row['Variations']}")
            if row['Contributor Name']:
                st.caption(f"👤 Contributed by: {row['Contributor Name']}")
            # Delete option
            if st.checkbox(f"Delete '{row['Game Name']}' from {row['Region/State']}", key=row["Entry ID"]):
                if st.button("Confirm Delete", key="del" + row["Entry ID"]):
                    delete_entry(row["Entry ID"])
                    st.success("✅ Entry deleted.")
                    st.experimental_rerun()