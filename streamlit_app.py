import streamlit as st

st.title("Rainfall-Runoff Calculator (SCS CN Method)")

# User input
precip = st.number_input("Rainfall (mm)", min_value=0.0, value=50.0, step=1.0)
curve_number = st.number_input("Curve Number (CN)", min_value=30, max_value=100, value=75, step=1)

# SCS CN runoff calculation
def calculate_runoff(P, CN):
    S = (25400 / CN) - 254  # in mm
    Ia = 0.2 * S            # initial abstraction
    if P <= Ia:
        return 0.0
    else:
        Q = ((P - Ia) ** 2) / (P - Ia + S)
        return Q

# Runoff calculation
runoff = calculate_runoff(precip, curve_number)

# Display result
st.subheader("Results")
st.write(f"Estimated Runoff: **{runoff:.2f} mm**")
