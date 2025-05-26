import streamlit as st

st.title("Spore Count Estimator")

# Initialize multipliers in session_state if not already stored
if "multipliers" not in st.session_state:
    st.session_state["multipliers"] = {
        "Air": {"40X": 80.6, "60X": 185.0},
        "Surface": {"40X": 3290, "60X": 7550}
    }

# Sidebar configuration for setting multipliers
st.sidebar.header("🔧 Set Multipliers")

# Load current multipliers from session state
air_40x = st.sidebar.number_input(
    "Air - 40X Multiplier", value=st.session_state["multipliers"]["Air"]["40X"]
)
air_60x = st.sidebar.number_input(
    "Air - 60X Multiplier", value=st.session_state["multipliers"]["Air"]["60X"]
)
surface_40x = st.sidebar.number_input(
    "Surface - 40X Multiplier", value=st.session_state["multipliers"]["Surface"]["40X"]
)
surface_60x = st.sidebar.number_input(
    "Surface - 60X Multiplier", value=st.session_state["multipliers"]["Surface"]["60X"]
)

# Update session state with any changes
st.session_state["multipliers"]["Air"]["40X"] = air_40x
st.session_state["multipliers"]["Air"]["60X"] = air_60x
st.session_state["multipliers"]["Surface"]["40X"] = surface_40x
st.session_state["multipliers"]["Surface"]["60X"] = surface_60x

# Main input section
sample_type = st.selectbox("Select sample type:", ["Air", "Surface"])
objective = st.selectbox("Select objective lens:", ["40X", "60X"])
spores = st.number_input("Enter number of spores counted:", min_value=0, step=1)
fields_of_view = st.number_input("Enter number of fields of view:", min_value=1, step=1)

# Get default multiplier based on user’s saved values
default_multiplier = st.session_state["multipliers"][sample_type][objective]
use_default = st.checkbox(f"Use selected multiplier ({default_multiplier})?", value=True)

# Allow override
if use_default:
    multiplier = default_multiplier
else:
    multiplier = st.number_input("Enter custom multiplier:", value=default_multiplier)

# Perform and display calculation
if fields_of_view > 0:
    spores_per_fov = spores / fields_of_view
    estimated_spores = spores_per_fov * multiplier
    st.markdown(f"### Estimated spore count: **{estimated_spores:.2f}**")
