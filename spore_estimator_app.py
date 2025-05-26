import streamlit as st

# Default multipliers
default_multipliers = {
    "Air": {"40X": 80.6, "60X": 185},
    "Surface": {"40X": 3290, "60X": 7550}
}

st.title("Spore Count Estimator")

# User input
sample_type = st.selectbox("Select sample type:", ["Air", "Surface"])
objective = st.selectbox("Select objective lens:", ["40X", "60X"])
spores = st.number_input("Enter number of spores counted:", min_value=0, step=1)
fields_of_view = st.number_input("Enter number of fields of view:", min_value=1, step=1)

# Default multiplier display
default_multiplier = default_multipliers[sample_type][objective]
use_default = st.checkbox(f"Use default multiplier ({default_multiplier})?", value=True)

if use_default:
    multiplier = default_multiplier
else:
    multiplier = st.number_input("Enter custom multiplier:", value=default_multiplier)

# Calculate and display result
if fields_of_view > 0:
    spores_per_fov = spores / fields_of_view
    estimated_spores = spores_per_fov * multiplier
    st.markdown(f"### Estimated spore count: **{estimated_spores:.2f}**")
