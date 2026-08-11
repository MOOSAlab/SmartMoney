import streamlit as st
import random as rm
import string
import matplotlib.pyplot as plt
import numpy as np
import json
import os


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SmartMoney",
    page_icon='golo.png',
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# JSON DATA STORAGE
# ============================================================

DATA_FILE = "memory.json"


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except:
            return {}

    return {}


saved_data = load_data()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0,255,170,0.08),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(0,140,255,0.08),
            transparent 25%
        ),
        #070b12;

    color: white;
}


/* =========================================================
   MAIN TITLE
   ========================================================= */

.main-title {
    font-size: 58px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #00ff99,
        #00c8ff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0;
}


.subtitle {
    color: #9aa6b2;
    font-size: 18px;
    margin-top: -10px;
}


/* =========================================================
   CARDS
   ========================================================= */

.card {
    background: rgba(20, 27, 38, 0.75);

    border: 1px solid rgba(0,255,170,0.12);

    border-radius: 20px;

    padding: 25px;

    margin: 10px 0;

    box-shadow:
        0 10px 40px rgba(0,0,0,0.25);

    transition: 0.3s;
}


.card:hover {
    border-color: rgba(0,255,170,0.5);

    transform: translateY(-3px);
}


/* =========================================================
   METRIC CARDS
   ========================================================= */

.metric {
    background:
        linear-gradient(
            135deg,
            rgba(0,255,170,0.12),
            rgba(0,150,255,0.08)
        );

    border: 1px solid rgba(0,255,170,0.2);

    border-radius: 18px;

    padding: 22px;

    text-align: center;
}


.metric-title {
    color: #8f9baa;
    font-size: 14px;
}


.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #00ff99;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    font-size: 28px;
    font-weight: 700;

    margin-top: 35px;
    margin-bottom: 15px;
}


/* =========================================================
   PROGRESS BAR
   ========================================================= */

.progress-container {
    background: #151d28;

    border-radius: 20px;

    height: 16px;

    overflow: hidden;
}


.progress-bar {
    height: 100%;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #00ff99,
            #00c8ff
        );
}


/* =========================================================
   ADVICE
   ========================================================= */

.advice {
    background: rgba(0,255,170,0.08);

    border-left: 4px solid #00ff99;

    padding: 18px;

    border-radius: 10px;

    margin-top: 15px;
}


/* =========================================================
   GOAL
   ========================================================= */

.goal-card {
    background:
        linear-gradient(
            135deg,
            rgba(0,200,255,0.10),
            rgba(0,255,170,0.05)
        );

    border-radius: 18px;

    padding: 20px;

    border: 1px solid rgba(0,200,255,0.2);
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background: #080d15;

    border-right:
        1px solid rgba(0,255,170,0.1);
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {

    border-radius: 12px;

    border: 1px solid #00ff99;

    background: transparent;

    color: #00ff99;

    font-weight: 600;

    transition: 0.3s;
}


.stButton > button:hover {

    background: #00ff99;

    color: #06100c;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    text-align: center;

    color: #65717f;

    margin-top: 60px;

    padding: 25px;

    border-top:
        1px solid rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">SmartMoney</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your personal financial intelligence dashboard.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## ⚙️ SmartMoney Settings")


    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    name = st.text_input(
        "Your name",
        value=saved_data.get("name", ""),
        max_chars=50,
        placeholder="Enter your name..."
    )


    # ============================================================
    # CURRENCY
    # ============================================================

    currencies = [
        "$",
        "₨",
        "₹",
        "¥",
        "€",
        "£",
        "﷼",
        "¢",
        "₩",
        "₺",
        "Other"
    ]

    saved_currency = saved_data.get("currency", "₨")

    # Check whether saved currency is one of the normal currencies
    if saved_currency in currencies:
        currency_index = currencies.index(saved_currency)
    else:
        currency_index = currencies.index("Other")

    currency_option = st.selectbox(
        "Currency",
        currencies,
        index=currency_index
    )

    # ============================================================
    # CUSTOM CURRENCY
    # ============================================================

    if currency_option == "Other":

        custom_currency = st.text_input(
            "Enter your currency",
            value=saved_data.get("custom_currency", ""),
            max_chars=20,
            placeholder="e.g. Zimbabue Dollar, etc."
        )

        if custom_currency:
            currency = custom_currency
        else:
            currency = ""

    else:

        currency = currency_option
        custom_currency = ""


    # ========================================================
    # PASSWORD GENERATOR
    # ========================================================

    st.markdown("### 🔐 Password Generator")

    password_length = st.slider(
        "Password length",
        8,
        32,
        16
    )


    if st.button("Generate Password"):

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ''.join(
            rm.choice(characters)
            for _ in range(password_length)
        )

        st.code(password)


    st.divider()

    st.caption("SmartMoney v2.0")


# ============================================================
# WELCOME SCREEN
# ============================================================

if not name:

    st.markdown(
        """<div class="card">
<h2>👋 Welcome to SmartMoney</h2>
<p>
Start by entering your name in the sidebar.
Then enter your monthly financial information
to unlock your personal dashboard.
</p>
</div>""",
        unsafe_allow_html=True
    )

    st.stop()


st.success(
    f"Welcome back, {name}! Let's analyze your money."
)


# ============================================================
# FINANCIAL INPUT
# ============================================================

st.markdown(
    '<div class="section-title">'
    '💰 Your Financial Data'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


# ============================================================
# INCOME
# ============================================================

with col1:

    income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=float(
            saved_data.get(
                "income",
                50000
            )
        ),
        step=100.0
    )


# ============================================================
# SAVINGS
# ============================================================

with col2:

    savings = st.number_input(
        "Monthly Savings",
        min_value=0.0,
        value=float(
            saved_data.get(
                "savings",
                10000
            )
        ),
        step=100.0
    )


# ============================================================
# GOAL
# ============================================================

with col3:

    goal = st.text_input(
        "Financial Goal",
        value=saved_data.get(
            "goal",
            ""
        ),
        placeholder="e.g. Buy a laptop"
    )





# ============================================================
# VALIDATION
# ============================================================

if income <= 0:

    st.warning(
        "Please enter an income greater than 0."
    )

    st.stop()


if savings > income:

    st.error(
        "⚠️ Your savings cannot be greater than your income."
    )

    st.stop()


# ============================================================
# CALCULATIONS
# ============================================================

remaining = income - savings


savings_rate = (
    savings / income
) * 100


yearly_income = income * 12


yearly_savings = savings * 12


yearly_remaining = remaining * 12


# ============================================================
# FINANCIAL HEALTH SCORE
# ============================================================

if savings_rate >= 30:

    health_score = 100

elif savings_rate >= 20:

    health_score = 90

elif savings_rate >= 15:

    health_score = 80

elif savings_rate >= 10:

    health_score = 65

elif savings_rate >= 5:

    health_score = 45

else:

    health_score = 25


# ============================================================
# FINANCIAL OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">📊 Financial Overview</div>',
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)


# ============================================================
# MONTHLY INCOME
# ============================================================

with m1:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Monthly Income</div>
<div class="metric-value">{currency}{income:,.0f}</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# MONTHLY SAVINGS
# ============================================================

with m2:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Monthly Savings</div>
<div class="metric-value">{currency}{savings:,.0f}</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# SAVINGS RATE
# ============================================================

with m3:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Savings Rate</div>
<div class="metric-value">{savings_rate:.1f}%</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# HEALTH SCORE
# ============================================================

with m4:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Health Score</div>
<div class="metric-value">{health_score}/100</div>
</div>""",
        unsafe_allow_html=True
    )

# ============================================================
# FINANCIAL HEALTH
# ============================================================

st.markdown(
    '<div class="section-title">❤️ Financial Health</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""<div class="card">
<h3>Financial Health Score: {health_score}/100</h3>
<div class="progress-container">
<div class="progress-bar" style="width:{health_score}%;"></div>
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# SAVINGS RATE ADVICE
# ============================================================

if savings_rate < 10:

    st.warning(
        "Your savings rate is below 10%. "
        "Try reducing unnecessary expenses "
        "and gradually increase your savings."
    )

elif savings_rate < 20:

    st.info(
        "You're doing reasonably well. "
        "Try pushing your savings rate toward 20%."
    )

elif savings_rate < 30:

    st.success(
        "Excellent! You're saving a healthy "
        "portion of your income."
    )

else:

    st.success(
        "🔥 Outstanding! Your savings rate "
        "is extremely strong."
    )


# ============================================================
# MONEY DASHBOARD
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📈 Money Dashboard'
    '</div>',
    unsafe_allow_html=True
)


chart1, chart2 = st.columns(2)


# ============================================================
# BAR CHART
# ============================================================

with chart1:

    st.markdown(
        '<div class="card">'
        '<h3>💵 Income vs Savings</h3>',
        unsafe_allow_html=True
    )


    fig, ax = plt.subplots(
        figsize=(7, 4)
    )


    categories = [
        "Income",
        "Savings",
        "Remaining"
    ]


    values = [
        income,
        savings,
        remaining
    ]


    ax.bar(
        categories,
        values
    )


    ax.set_ylabel(
        f"Amount ({currency})"
    )


    ax.set_title(
        "Monthly Money Distribution"
    )


    ax.grid(
        axis="y",
        alpha=0.2
    )


    st.pyplot(
        fig,
        use_container_width=True
    )


    plt.close(fig)


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# PIE CHART
# ============================================================

with chart2:

    st.markdown(
        '<div class="card">'
        '<h3>🥧 Money Allocation</h3>',
        unsafe_allow_html=True
    )


    fig2, ax2 = plt.subplots(
        figsize=(7, 4)
    )


    labels = [
        "Savings",
        "Remaining"
    ]


    sizes = [
        savings,
        remaining
    ]


    ax2.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )


    ax2.set_title(
        "Monthly Allocation"
    )


    st.pyplot(
        fig2,
        use_container_width=True
    )


    plt.close(fig2)


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# 12-MONTH PROJECTION
# ============================================================

st.markdown(
    '<div class="section-title">🚀 12-Month Projection</div>',
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)


# ============================================================
# YEARLY INCOME
# ============================================================

with p1:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Yearly Income</div>
<div class="metric-value">{currency}{yearly_income:,.0f}</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# YEARLY SAVINGS
# ============================================================

with p2:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Yearly Savings</div>
<div class="metric-value">{currency}{yearly_savings:,.0f}</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# YEARLY REMAINING
# ============================================================

with p3:
    st.markdown(
        f"""<div class="metric">
<div class="metric-title">Yearly Remaining</div>
<div class="metric-value">{currency}{yearly_remaining:,.0f}</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# SAVINGS GROWTH
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📈 Savings Growth Projection'
    '</div>',
    unsafe_allow_html=True
)


months = np.arange(
    1,
    13
)


growth = savings * months


fig3, ax3 = plt.subplots(
    figsize=(12, 4)
)


ax3.plot(
    months,
    growth,
    marker="o",
    linewidth=3
)


ax3.fill_between(
    months,
    growth,
    alpha=0.1
)


ax3.set_title(
    "Projected Savings Over 12 Months"
)


ax3.set_xlabel(
    "Month"
)


ax3.set_ylabel(
    f"Savings ({currency})"
)


ax3.set_xticks(
    months
)


ax3.grid(
    alpha=0.2
)


st.pyplot(
    fig3,
    use_container_width=True
)


plt.close(fig3)


# ============================================================
# SAVE CURRENT DATA
# ============================================================

current_data = {
    "name": name,
    "income": income,
    "savings": savings,
    "currency": currency,
    "custom_currency": custom_currency,
    "goal": goal
}

save_data(current_data)


# ============================================================
# EXPENSE TRACKER
# ============================================================

st.markdown(
    '<div class="section-title">🧾 Expense Tracker</div>',
    unsafe_allow_html=True
)

st.write(
    "Add multiple expenses at once and keep track of where your money goes."
)


# ============================================================
# LOAD SAVED EXPENSES
# ============================================================

saved_expenses = saved_data.get("expenses", [])

expense_categories = [
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Bills",
    "Education",
    "Health",
    "Other"
]


# ============================================================
# CREATE TABLE
# ============================================================

if saved_expenses:

    expense_table = []

    for expense in saved_expenses:

        expense_table.append({
            "Expense": expense.get("name", ""),
            "Category": expense.get("category", "Other"),
            "Amount": float(expense.get("amount", 0))
        })

else:

    expense_table = [
        {
            "Expense": "",
            "Category": "Food",
            "Amount": 0.0
        }
    ]


# ============================================================
# EXPENSE EDITOR
# ============================================================

edited_expenses = st.data_editor(
    expense_table,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,

    column_config={

        "Expense": st.column_config.TextColumn(
            "Expense Name",
            help="Example: Lunch, Bus, Netflix",
            max_chars=50
        ),

        "Category": st.column_config.SelectboxColumn(
            "Category",
            options=expense_categories,
            required=True
        ),

        "Amount": st.column_config.NumberColumn(
            "Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )
    },

    key="expense_editor"
)


# ============================================================
# SAVE EXPENSES BUTTON
# ============================================================

if st.button("💾 Save Expenses"):

    cleaned_expenses = []

    for expense in edited_expenses:

        expense_name = str(
            expense.get("Expense", "")
        ).strip()

        category = expense.get(
            "Category",
            "Other"
        )

        amount = float(
            expense.get("Amount", 0)
        )


        # Ignore completely empty rows
        if not expense_name and amount <= 0:
            continue


        # Don't allow an expense without a name
        if not expense_name:

            st.warning(
                "Every expense must have a name."
            )

            st.stop()


        # Don't allow zero/negative expenses
        if amount <= 0:

            st.warning(
                f"Please enter a valid amount for '{expense_name}'."
            )

            st.stop()


        cleaned_expenses.append({
            "name": expense_name,
            "category": category,
            "amount": amount
        })


    # --------------------------------------------------------
    # SAVE TO JSON
    # --------------------------------------------------------

    current_data["expenses"] = cleaned_expenses

    save_data(current_data)

    st.success(
        f"✅ {len(cleaned_expenses)} expense(s) saved successfully!"
    )

    st.rerun()


# ============================================================
# EXPENSE SUMMARY
# ============================================================

expenses = saved_data.get("expenses", [])


if expenses:

    total_expenses = sum(
        float(expense["amount"])
        for expense in expenses
    )


    remaining_after_expenses = (
        income - total_expenses
    )


    if income > 0:

        expense_rate = (
            total_expenses / income
        ) * 100

    else:

        expense_rate = 0


    # ========================================================
    # EXPENSE METRICS
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Expense Summary</div>',
        unsafe_allow_html=True
    )


    e1, e2, e3 = st.columns(3)


    with e1:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Total Expenses</div>
<div class="metric-value">{currency}{total_expenses:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    with e2:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Money Remaining</div>
<div class="metric-value">{currency}{remaining_after_expenses:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    with e3:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Expense Rate</div>
<div class="metric-value">{expense_rate:.1f}%</div>
</div>""",
            unsafe_allow_html=True
        )


    # ========================================================
    # CATEGORY TOTALS
    # ========================================================

    category_totals = {}


    for expense in expenses:

        category = expense["category"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + float(expense["amount"])
        )


    # ========================================================
    # CHARTS
    # ========================================================

    st.markdown(
        '<div class="section-title">📈 Spending Analysis</div>',
        unsafe_allow_html=True
    )


    chart1, chart2 = st.columns(2)


    # --------------------------------------------------------
    # PIE CHART
    # --------------------------------------------------------

    with chart1:

        fig, ax = plt.subplots(
            figsize=(7, 5)
        )

        ax.pie(
            category_totals.values(),
            labels=category_totals.keys(),
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title(
            "Where Your Money Goes"
        )

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # --------------------------------------------------------
    # BAR CHART
    # --------------------------------------------------------

    with chart2:

        fig2, ax2 = plt.subplots(
            figsize=(7, 5)
        )

        ax2.bar(
            category_totals.keys(),
            category_totals.values()
        )

        ax2.set_title(
            "Expenses by Category"
        )

        ax2.set_ylabel(
            f"Amount ({currency})"
        )

        ax2.tick_params(
            axis="x",
            rotation=45
        )

        ax2.grid(
            axis="y",
            alpha=0.2
        )

        st.pyplot(
            fig2,
            use_container_width=True
        )

        plt.close(fig2)


    # ========================================================
    # SPENDING STATUS
    # ========================================================

    if total_expenses > income:

        st.error(
            "🚨 Your expenses are greater than your income!"
        )

    elif expense_rate > 80:

        st.warning(
            "⚠️ You're spending more than 80% of your income."
        )

    elif expense_rate > 60:

        st.info(
            "💡 Your expenses are relatively high. "
            "Consider reviewing your largest categories."
        )

    else:

        st.success(
            "✅ Your spending is currently under control."
        )


else:

    st.info(
        "🧾 No expenses saved yet. Add some expenses above!"
    )

# ============================================================
# FINANCIAL GOAL
# ============================================================

if goal:

    st.markdown(
        '<div class="section-title">🎯 Your Financial Goal</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""<div class="goal-card">
<h2>🎯 {goal}</h2>
<p>If you save <strong>{currency}{savings:,.0f}</strong> every month, you could accumulate:</p>
<h2>{currency}{yearly_savings:,.0f}</h2>
<p>in one year.</p>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# SAVE CURRENT DATA
# ============================================================

current_data = {
    "name": name,
    "income": income,
    "savings": savings,
    "currency": currency,
    "custom_currency": custom_currency,
    "goal": goal,
    "expenses": expenses
}

save_data(current_data)


# ============================================================
# WHAT IF? EXPENSE REDUCTION SIMULATOR
# ============================================================

st.markdown(
    '<div class="section-title">🤔 What If? Simulator</div>',
    unsafe_allow_html=True
)

st.write(
    "See how reducing your expenses could improve your savings."
)


# ============================================================
# GET CURRENT EXPENSES
# ============================================================

expenses = saved_data.get("expenses", [])

total_expenses = sum(
    float(expense.get("amount", 0))
    for expense in expenses
)


# ============================================================
# SIMULATOR
# ============================================================

if total_expenses > 0 and income > 0:

    what_if_col1, what_if_col2 = st.columns(2)


    with what_if_col1:

        reduction_percent = st.slider(
            "Reduce expenses by",
            min_value=0,
            max_value=100,
            value=10,
            step=5,
            format="%d%%",
            key="what_if_reduction"
        )


    with what_if_col2:

        simulation_months = st.slider(
            "Simulation period",
            min_value=1,
            max_value=60,
            value=12,
            step=1,
            format="%d months",
            key="what_if_months"
        )


    # ========================================================
    # CALCULATIONS
    # ========================================================

    reduction_amount = (
        total_expenses
        * reduction_percent
        / 100
    )

    simulated_expenses = (
        total_expenses
        - reduction_amount
    )

    current_monthly_savings = (
        income - total_expenses
    )

    simulated_monthly_savings = (
        income - simulated_expenses
    )

    extra_monthly_savings = (
        simulated_monthly_savings
        - current_monthly_savings
    )

    current_period_savings = (
        current_monthly_savings
        * simulation_months
    )

    simulated_period_savings = (
        simulated_monthly_savings
        * simulation_months
    )

    extra_period_savings = (
        simulated_period_savings
        - current_period_savings
    )


    # ========================================================
    # RESULTS
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Simulation Results</div>',
        unsafe_allow_html=True
    )


    result1, result2, result3, result4 = st.columns(4)


    with result1:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Current Expenses</div>
<div class="metric-value">{currency}{total_expenses:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    with result2:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">New Expenses</div>
<div class="metric-value">{currency}{simulated_expenses:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    with result3:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Extra Monthly Savings</div>
<div class="metric-value">{currency}{extra_monthly_savings:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    with result4:

        st.markdown(
            f"""<div class="metric">
<div class="metric-title">Extra Savings</div>
<div class="metric-value">{currency}{extra_period_savings:,.0f}</div>
</div>""",
            unsafe_allow_html=True
        )


    # ========================================================
    # BIG RESULT CARD
    # ========================================================

    st.markdown(
        f"""<div class="card">
<h2>🚀 What If You Cut Expenses by {reduction_percent}%?</h2>
<p>
You would save an additional
<strong>{currency}{extra_monthly_savings:,.0f}</strong>
every month.
</p>
<p>
Over {simulation_months} months, that could become
<strong>{currency}{extra_period_savings:,.0f}</strong>
in additional savings.
</p>
</div>""",
        unsafe_allow_html=True
    )


    # ========================================================
    # COMPARISON CHART
    # ========================================================

    st.markdown(
        '<div class="section-title">📈 Before vs After</div>',
        unsafe_allow_html=True
    )


    labels = [
        "Current",
        f"{reduction_percent}% Reduction"
    ]

    monthly_values = [
        current_monthly_savings,
        simulated_monthly_savings
    ]


    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.bar(
        labels,
        monthly_values
    )

    ax.set_title(
        "Monthly Savings Comparison"
    )

    ax.set_ylabel(
        f"Savings ({currency})"
    )

    ax.grid(
        axis="y",
        alpha=0.2
    )

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


    # ========================================================
    # SMART MESSAGE
    # ========================================================

    if reduction_percent == 0:

        st.info(
            "Try increasing the slider to see how reducing "
            "expenses could affect your savings."
        )

    elif extra_monthly_savings > 0:

        st.success(
            f"💡 Cutting your expenses by {reduction_percent}% "
            f"could give you an extra "
            f"{currency}{extra_monthly_savings:,.0f} "
            "to save every month!"
        )

    else:

        st.info(
            "Your current expenses are already very low."
        )


else:

    st.info(
        "🧾 Add some expenses first to use the "
        "What If? Simulator."
    )


# ============================================================
# OFFLINE CURRENCY CONVERTER
# ============================================================

st.markdown(
    '<div class="section-title">💱 Currency Converter</div>',
    unsafe_allow_html=True
)

st.write(
    "Convert currencies using SmartMoney's offline exchange rates."
)


# ============================================================
# OFFLINE EXCHANGE RATES
# Base currency = USD
# Update these values whenever you want.
# ============================================================

exchange_rates = {

    "USD": 1.0,

    "PKR": 280.0,

    "EUR": 0.86,

    "GBP": 0.74,

    "INR": 86.0,

    "CNY": 7.18,

    "JPY": 147.0,

    "AED": 3.67,

    "SAR": 3.75,

    "CAD": 1.38,

    "AUD": 1.53
}


currency_names = {

    "USD": "US Dollar",
    "PKR": "Pakistani Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "INR": "Indian Rupee",
    "CNY": "Chinese Yuan",
    "JPY": "Japanese Yen",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar"
}


# ============================================================
# CONVERTER INPUTS
# ============================================================

converter_col1, converter_col2, converter_col3 = st.columns(3)


with converter_col1:

    converter_amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=100.0,
        step=1.0,
        key="converter_amount"
    )


with converter_col2:

    from_currency = st.selectbox(
        "From",
        list(exchange_rates.keys()),
        format_func=lambda x:
            f"{x} — {currency_names[x]}",
        key="from_currency"
    )


with converter_col3:

    to_currency = st.selectbox(
        "To",
        list(exchange_rates.keys()),
        index=1,
        format_func=lambda x:
            f"{x} — {currency_names[x]}",
        key="to_currency"
    )


# ============================================================
# CONVERT
# ============================================================

if st.button(
    "🔄 Convert",
    key="convert_currency"
):

    if converter_amount == 0:

        st.warning(
            "Please enter an amount greater than 0."
        )

    else:

        # Convert FROM currency to USD
        amount_in_usd = (
            converter_amount
            / exchange_rates[from_currency]
        )

        # Convert USD to TO currency
        converted_amount = (
            amount_in_usd
            * exchange_rates[to_currency]
        )


        # Calculate exchange rate
        exchange_rate = (
            exchange_rates[to_currency]
            / exchange_rates[from_currency]
        )


        # ====================================================
        # RESULT
        # ====================================================

        st.markdown(
            f"""<div class="card">
<h3>💱 Conversion Result</h3>
<h1>{converter_amount:,.2f} {from_currency}
= {converted_amount:,.2f} {to_currency}</h1>
<p>
1 {from_currency}
= {exchange_rate:,.4f} {to_currency}
</p>
</div>""",
            unsafe_allow_html=True
        )


        st.caption(
            "⚠️ These are offline reference rates and "
            "are not live market rates."
        )


# ============================================================
# SMARTMONEY ADVICE
# ============================================================

st.markdown(
    '<div class="section-title">🧠 SmartMoney Advice</div>',
    unsafe_allow_html=True
)

if savings_rate >= 30:

    advice = (
        "You're in excellent shape. Consider dividing your "
        "savings between an emergency fund, long-term investments, "
        "and specific financial goals."
    )

elif savings_rate >= 20:

    advice = (
        "Your savings strategy is strong. Try maintaining your "
        "current savings rate while increasing your income over time."
    )

elif savings_rate >= 10:

    advice = (
        "You're building a good foundation. Look for small expenses "
        "you can reduce and redirect that money toward savings."
    )

else:

    advice = (
        "Start small. Even increasing your savings by 1–2% each "
        "month can make a meaningful difference over time."
    )

st.markdown(
    f"""<div class="advice">
<strong>Smart Recommendation</strong>
<p>{advice}</p>
</div>""",
    unsafe_allow_html=True
)

# ============================================================
# DATA SAVED MESSAGE
# ============================================================

st.caption(
    "💾 Your financial data is automatically saved locally."
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """<div class="footer">
<strong>SmartMoney</strong>
<br><br>
Personal finance dashboard built with Python & Streamlit.
<br><br>
Track smarter. Save better. Build your future.
<br><br>
© 2026 SmartMoney
</div>""",
    unsafe_allow_html=True
)