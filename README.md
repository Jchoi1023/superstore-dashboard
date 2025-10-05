 # 🛒 Superstore Sales Dashboard

### Overview  
An interactive dashboard analyzing sales performance, profitability, and discount impacts using the **Sample Superstore** dataset.  
Built with **Python, Streamlit, and Plotly**, it allows users to filter by year and region to uncover key business insights.

## Tech Stack
**Python (pandas)**: Data cleaning, aggregation, and KPA computation
**Plotly**: Interactive charts and dual-axis visualizations
**Streamlit**: Wen app interface and live dashboard
**GitHub + Streamlit Cloud**: Version control and public deployment

## Key Insights

### 1. Overall Performance
![Overall Performance] (image/overview.png)
- **Total Sales:** \$2.3M  
- **Total Profit:** \$286K  
- **Average Profit Margin:** **12.5%**  
- **Unique Customers:** 793  

The business generates solid revenue with moderate profitability, suggesting a balanced but improvable pricing structure.

### 2. Monthly Sales & Profit Margin Trends
![Monthly Trends] (image/margin.png)
- Sales fluctuate seasonally — peaks around **Q4**, dips in early Q1.  
- Profit margin moves **inversely** to sales at times, implying **heavy discounting** affects profitability.  
- Some months even show **negative margins**, indicating over-discounted campaigns.  

**Recommendation:** Adjust promotions during peak seasons; prioritize profitability over raw sales volume.

### 3. Category Performance
![Sales] (image/sales.png)
| Category | Sales Share | Profit Margin | Observation |
|-----------|--------------|----------------|--------------|
| **Furniture** | High | **2.5%** | Strong revenue but extremely low margin — likely due to high shipping or heavy discounting. |
| **Office Supplies** | Moderate | **17.0%** | Balanced performance; reliable profit generator. |
| **Technology** | High | **17.4%** | Most profitable category with sustainable margins. |

 **Recommendation:** Focus marketing on **Technology & Office Supplies**, and reassess Furniture pricing or logistics.

### 4. Discount Impact
![Discount Impact] (image/discount.png)
- Profit drops sharply as discounts rise beyond **20%**.  
- **High-discount ranges (40–50% and above)** generate **negative profits**, especially for Technology products.  
- Small discounts (≤10%) are sustainable and sometimes drive healthy returns.  

**Recommendation:** Cap discounts below **20%** and use targeted promotions instead of blanket markdowns.
