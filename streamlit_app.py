import streamlit as st
import math 

def calculate_behaviour_index(fear_greed_stock, fear_greed_bitcoin):
  """Calculates the Behaviour Index based on stock and Bitcoin fear and greed indices.

  Args:
    fear_greed_stock: The Fear and Greed index for the American stock market.
    fear_greed_bitcoin: The Fear and Greed index for Bitcoin.

  Returns:
    The calculated Behaviour Index.
  """
  behaviour_index = (math.log(fear_greed_stock) + math.log(fear_greed_bitcoin)) / 8
  return behaviour_index

st.title("Behaviour Index Calculator")
st.write("Enter the Fear and Greed indices below:")
st.write("---")

fear_greed_stock = st.number_input("American stock market Fear and Greed index:", format="%.2f")
fear_greed_bitcoin = st.number_input("Bitcoin Fear and Greed index:", format="%.2f")

st.write("---")

if st.button("Calculate Behaviour Index"):
  if fear_greed_stock is not None and fear_greed_bitcoin is not None:
    behaviour_index = calculate_behaviour_index(fear_greed_stock, fear_greed_bitcoin)
    st.write(f"The Behaviour Index is: **{behaviour_index:.2f}**")
  else:
    st.warning("Please enter values for both Fear and Greed indices.")