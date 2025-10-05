import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 🧩 1. configuration
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🧠 2. Load data 
@st.cache_data # Cache the data loading function (run faster on reruns - 
# Streamlit normally runs your whole script from top to bottom every time something changes - that`s why caching is important)
def load_data():
    df = pd.read_csv("superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df

df = load_data()

# 🎛️ 3. sidebar filters
st.sidebar.header("🔍 Filters")
selected_year = st.sidebar.multiselect(
    "Select Year", options=df["Year"].unique(), default=df["Year"].unique()
)
selected_region = st.sidebar.multiselect(
    "Select Region", options=df["Region"].unique(), default=df["Region"].unique()
)

filtered_df = df.query("Year in @selected_year and Region in @selected_region")

# 💡 4. KPI 
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
avg_margin = total_profit / total_sales
num_customers = filtered_df["Customer ID"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💵 Total Sales", f"${total_sales:,.0f}")
col2.metric("💰 Total Profit", f"${total_profit:,.0f}")
col3.metric("📈 Profit Margin", f"{avg_margin:.1%}")
col4.metric("👥 Unique Customers", num_customers)

st.markdown("---")

# 📊 5. monthly sales trends
# Monthly sales & margin
sales_trend = (
    filtered_df.groupby("Month")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)
sales_trend["Profit Margin"] = sales_trend["Profit"] / sales_trend["Sales"]

# Create figure object
fig_trend = go.Figure()

# 1️⃣ Add monthly sales line
fig_trend.add_trace(
    go.Bar(
        x=sales_trend["Month"],
        y=sales_trend["Sales"],
        name="Sales ($)",
        marker_color="#1f77b4",
        yaxis="y1"
    )
)

# 2️⃣ Add monthly margin line
fig_trend.add_trace(
    go.Scatter(
        x=sales_trend["Month"],
        y=sales_trend["Profit Margin"],
        name="Profit Margin (%)",
        mode="lines+markers",
        marker_color="#ff7f0e",
        yaxis="y2"
    )
)

# 3️⃣ Layout customization
fig_trend.update_layout(
    title="📅 Monthly Sales & Profit Margin",
    xaxis=dict(title="Month", categoryorder="array", categoryarray=sales_trend["Month"]),
    yaxis=dict(title="Sales ($)", side="left", showgrid=False),
    yaxis2=dict(
        title="Profit Margin (%)",
        overlaying="y",
        side="right",
        tickformat=".0%",
        showgrid=False
    ),
    legend=dict(x=0.02, y=1.1, orientation="h"),
    hovermode="x unified",
    bargap=0.2,
    template="plotly_white"
)

st.plotly_chart(fig_trend, use_container_width=True)


# 🛍️ 6. Sales & Profit by Category
category_perf = (
    filtered_df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
)
category_perf["Profit Margin"] = category_perf["Profit"] / category_perf["Sales"]

fig_cat = px.bar(
    category_perf,
    x="Category", y=["Sales", "Profit"],
    barmode="group", title="📦 Sales & Profit by Category"
)
st.plotly_chart(fig_cat, use_container_width=True)

# 💹 Profit Margin by Category
fig_margin = px.bar(
    category_perf,
    x="Category",
    y="Profit Margin",
    color="Category",
    text=category_perf["Profit Margin"].apply(lambda x: f"{x:.1%}"),
    title="💹 Profit Margin by Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig_margin.update_layout(yaxis_tickformat=".0%", yaxis_title="Profit Margin (%)")
st.plotly_chart(fig_margin, use_container_width=True)


# Create discount buckets
filtered_df['Discount Bin'] = pd.cut(
    filtered_df['Discount'],
    bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 1],
    labels=['0–10%', '10–20%', '20–30%', '30–40%', '40–50%', '50%+']
)

avg_profit = (
    filtered_df.groupby(['Discount Bin', 'Category'])
            .agg(Avg_Profit=('Profit','mean'))
            .reset_index()
)

fig_bar = px.bar(
    avg_profit,
    x='Discount Bin',
    y='Avg_Profit',
    color='Category',
    barmode='group',
    title='💸 Average Profit by Discount Range (per Category)',
    text_auto='.2f'
)
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")
st.caption("📊 Data source: Sample Superstore Dataset | Built with Streamlit + Plotly")
