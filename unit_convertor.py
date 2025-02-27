import streamlit as st
import pandas as pd
from pint import UnitRegistry


ureg = UnitRegistry()

dark_mode = st.toggle("🌙 Dark Mode", value=True)

if dark_mode:
    st.markdown(
        """
        <style>
            body { background-color: #000000; color: white; }
            .stApp { background-color: #000000; }
            .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
                background-color: white; color: black; border-radius: 8px; border: 1px solid #444;
            }
            .stButton>button:hover { background-color: #ddd; }
        </style>
        """,
        unsafe_allow_html=True
    )
    heading_text = "✨ Advanced Unit Converter "
    text_color = "white"
    subtext_color = "pink"
else:
    st.markdown(
        """
        <style>
            body { background-color: #FFFFFF; color: black; }
            .stApp { background-color: #FFFFFF; }
            .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
                background-color: #f0f0f0; color: black; border-radius: 8px; border: 1px solid #ccc;
            }
            .stButton>button:hover { background-color: #ddd; }
        </style>
        """,
        unsafe_allow_html=True
    )
    heading_text = "✨ Advanced Unit Converter "
    text_color = "black"
    subtext_color = "blue"

st.markdown(f"<h1 style='color: {text_color};'>{heading_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color: {subtext_color};'>Convert units across various categories with ease!</p>", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)

units = {
    "📏 Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter"],
    "⚖️ Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "⏳ Time": ["second", "minute", "hour", "day"],
    "🧪 Volume": ["liter", "milliliter", "gallon", "cup", "fluid_ounce"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "🚀 Speed": ["meter/second", "kilometer/hour", "mile/hour", "foot/second"],
    "⚡ Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour"],
    "🌬️ Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "💾 Data Size": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "📐 Angle": ["degree", "radian"],
}

category = st.selectbox("📌 Select a category:", list(units.keys()))

from_unit = st.selectbox("🔄 Convert from:", units[category])
to = st.selectbox("🔁 Convert to:", units[category])

result = None  

if st.button("🚀 Convert Now"):
    try:
        if category == "🌡️ Temperature":
            if from_unit == "celsius" and to == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  
        else:
            result = (value * ureg(from_unit)).to(to).magnitude

        st.markdown(f"<p style='color: {'pink' if dark_mode else 'blue'}; font-size: 20px; font-weight: bold;'>✅ {value} {from_unit} = {result:.2f} {to}</p>", unsafe_allow_html=True)
        
        st.session_state.history.append({"Value": value, "From": from_unit, "Converted Value": result, "To": to})

    except Exception as e:
        st.error("⚠️ Invalid unit conversion! Please check your inputs.")

if st.session_state.history:
    st.markdown("<h3 style='color: purple;'>📜 Conversion History</h3>", unsafe_allow_html=True)
    df = pd.DataFrame(st.session_state.history[-40:])  
    st.dataframe(df.style.set_properties(**{
        "background-color": "#222" if dark_mode else "#FFF",
        "color": "pink" if dark_mode else "blue",
        "border": "1px solid gray",
    }))
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: pink;'>
        🚀 Advanced Unit Converter | Built with ❤️ using Streamlit  
        <br>© 2025 | Mehak Akram 
    </p>
    """,
    unsafe_allow_html=True
)
