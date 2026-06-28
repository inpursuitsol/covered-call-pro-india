import streamlit as st

from services.market_service import market_service
from services.recommendation_service import recommendation_service
from services.paper_trade_service import paper_trade_service


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
# Load Data
# -----------------------------------------------------

market = market_service.get_snapshot()

trade = recommendation_service.get_recommendation()

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

        "⚙ Settings",

    ]

)

# -----------------------------------------------------
# Dashboard
# -----------------------------------------------------

if page == "🏠 Dashboard":

    st.title("📈 CoveredCall Pro India")

    st.caption(
        "Professional Covered Call Decision Platform"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            "NIFTY",
            f"{market['nifty']:,.2f}"
        )

    with c2:
        st.metric(
            "India VIX",
            market["vix"]
        )

    with c3:
        st.metric(
            "Opportunity",
            f"{market['opportunity_score']}/100"
        )

    with c4:
        st.metric(
            "Expected Income",
            f"₹{market['expected_income']:,.0f}"
        )

    with c5:
        st.metric(
            "Risk",
            market["risk"]
        )

    st.divider()

    st.subheader("ATHENA Recommendation")

    if trade is None:

        st.warning(
            "No recommendation available."
        )

    else:

        st.success(
            f"{trade.action} {trade.strike} CE"
        )

        left, right = st.columns([2, 1])

        with left:

            st.markdown(f"""

### Recommendation

**Action**

{trade.action}

**Strike**

{trade.strike}

**Premium**

₹{trade.premium}

**Expected Monthly Income**

₹{trade.monthly_income:,.0f}

**Reason**

{trade.reason}

""")

        with right:

            st.metric(
                "Confidence",
                f"{trade.confidence}%"
            )

            st.metric(
                "Risk",
                trade.risk
            )

            st.metric(
                "Expiry",
                trade.expiry.strftime("%d %b %Y")
                if hasattr(trade.expiry, "strftime")
                else str(trade.expiry)
                    )

    st.divider()

    st.subheader("Market Snapshot")

    st.info(f"""

Live NIFTY : **{market['nifty']:,.2f}**

India VIX : **{market['vix']}**

Market Status : **{market['market_status']}**

Last Updated :

{market['last_updated']}

""")

# -----------------------------------------------------
# Portfolio
# -----------------------------------------------------

elif page == "💼 Portfolio":

    st.title("💼 Portfolio")

    st.metric("NIFTYBeES Holdings", "1200")

    st.metric("Covered Call Lots", "5")

    st.info("Portfolio management will be enhanced in Version 1.1")


# -----------------------------------------------------
# Market
# -----------------------------------------------------

elif page == "📊 Market":

    st.title("📊 Live Market")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "NIFTY",
            f"{market['nifty']:,.2f}"
        )

    with c2:

        st.metric(
            "India VIX",
            market["vix"]
        )

    st.write("")

    st.write("Weekly Expiry :", market["expiry"])

    st.write("Market Status :", market["market_status"])

    st.write("Last Updated :", market["last_updated"])


# -----------------------------------------------------
# Option Chain
# -----------------------------------------------------

# -----------------------------------------------------
# Option Chain
# -----------------------------------------------------

elif page == "📈 Option Chain":

    from providers.nse_option_chain_provider import (
        nse_option_chain_provider
    )

    st.title("📈 Live NSE Option Chain")

    calls = nse_option_chain_provider.get_calls()

    if not calls:

        st.error("Unable to fetch NSE Option Chain.")

    else:

        data = []

        for option in calls:

            data.append({

                "Strike": option.strike,

                "Premium": option.premium,

                "Bid": option.bid,

                "Ask": option.ask,

                "OI": option.open_interest,

                "Volume": option.volume,

                "IV": option.implied_volatility

            })

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )

        if st.button("💾 Save Paper Trade"):

                paper_trade_service.save(trade)

                st.success("Paper trade saved successfully.")


# -----------------------------------------------------
# Paper Trades
# -----------------------------------------------------

elif page == "📝 Paper Trades":

    st.title("📝 Paper Trade Journal")

    trades = paper_trade_service.get_all()

    if len(trades) == 0:

        st.info("No paper trades available.")

    else:

        st.dataframe(
            trades,
            use_container_width=True
        )


# -----------------------------------------------------
# Settings
# -----------------------------------------------------

elif page == "⚙ Settings":

    st.title("⚙ Settings")

    st.write("Current Strategy Settings")

    st.write("---")

    st.write("Preferred OTM :", "2.5 %")

    st.write("Minimum VIX :", "15")

    st.write("Lots :", "5")

    st.write("Paper Trading :", "Enabled")

    st.info(
        "Settings page will become editable in Version 1.1"
    )