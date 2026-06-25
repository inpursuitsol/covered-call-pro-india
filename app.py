import streamlit as st

from services.market_service import market_service


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="CoveredCall Pro India",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------------------------
# Load Market Data
# -----------------------------------------------------

market = market_service.get_snapshot()


# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

st.sidebar.title("📈 CoveredCall Pro India")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "💼 Portfolio",
        "📊 Market",
        "📈 Option Chain",
        "📝 Paper Trades",
        "⚙ Settings"
    ]
)


# -----------------------------------------------------
# Dashboard
# -----------------------------------------------------

if page == "🏠 Dashboard":

    st.title("📈 CoveredCall Pro India")

    st.caption("Professional Options Income Platform")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Opportunity Score",
        f'{market["opportunity_score"]}/100'
    )

    col2.metric(
        "Market Mood",
        market["market_status"]
    )

    col3.metric(
        "Risk",
        market["risk"]
    )

    col4.metric(
        "Expected Income",
        f'₹{market["expected_income"]:,}'
    )

    st.divider()

    st.subheader("ATHENA Recommendation")

    st.success("SELL NIFTY CALL (Paper Trade)")

    st.info(
        f"""
**Market Status :** {market["market_status"]}

**India VIX :** {market["vix"]}

**Expected Income :** ₹{market["expected_income"]:,}

**Last Updated :**

{market["last_updated"]}
"""
    )


elif page == "💼 Portfolio":

    st.title("Portfolio")

    st.info("Coming in Version 0.3")


elif page == "📊 Market":

    st.title("Market")

    st.info("Coming in Version 0.3")


elif page == "📈 Option Chain":

    st.title("Option Chain")

    st.info("Coming in Version 0.4")


elif page == "📝 Paper Trades":

    st.title("Paper Trades")

    st.info("Coming in Version 0.5")


elif page == "⚙ Settings":

    st.title("Settings")

    st.info("Coming in Version 0.5")