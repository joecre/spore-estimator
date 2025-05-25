import streamlit as st

# App title
st.title("PriorityLab Daily Bonus Target Calculator")

# Description
st.write("Use this tool to find out how many samples you need to process today to stay on track for a performance bonus.")

# Dropdown for employment type (defaults to Full-Time)
employment_type = st.selectbox("Select your employment type:", ["Part-Time", "Full-Time"], index=1)

# Slider for daily hours, allowing quarter-hour increments
hours = st.slider("How many hours are you working today?", 
                  min_value=1.0, 
                  max_value=12.0, 
                  value=8.0, 
                  step=0.25)

# Display the results
st.subheader("Sample Targets for Today")

if employment_type == "Part-Time":
    st.write("**Part-Time Bonus Tiers**")
    st.write(f"- $100 bonus: **{7 * hours:.1f} samples** today (7/hr)")
    st.write(f"- $150 bonus: **{8 * hours:.1f} samples** today (8/hr)")

elif employment_type == "Full-Time":
    st.write("**Full-Time Bonus Tiers**")
    st.write(f"- $200 bonus: **{7 * hours:.1f} samples** today (7/hr)")
    st.write(f"- $300 bonus: **{8 * hours:.1f} samples** today (8/hr)")

# Footer note
st.markdown("---")
st.caption("Note: You must work at least 80 hours per month to qualify for any bonus.")
