import streamlit as st
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from icons import icon, GITHUB_SVG
from theme import setup_page

st.set_page_config(page_title="Bank App — Dhruv Gupta", page_icon="🟢", layout="centered")

colors = setup_page()
icon_color = colors["icon_color"]

GITHUB_FOLDER_URL = "https://github.com/BeastBoom/Road-To-Creation/tree/main/Projects/Bank%20App"

st.markdown(
    f"""
    <div class="accent-bar" style="background:#f97316; width:120px;"></div>
    <h1>Bank App</h1>
    <p style="font-size:14.5px;">A simulated multi-account banking system supporting deposits, withdrawals, transfers, daily withdrawal limits, and rollback-safe transaction handling. Create accounts below and try it live — all data lives only in this browser session and is wiped on exit or refresh, nothing is stored server-side.</p>
    <a class="icon-link" href="{GITHUB_FOLDER_URL}" target="_blank">{icon(GITHUB_SVG, 18, icon_color)} &nbsp;View source on GitHub</a>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------- Original class, unmodified ----------

class Bank_App:
    def __init__(self):
        self.balance = 0
        self.transaction_history = {
            "Type": [],
            "Amount": [],
            "Balance": [],
            "Timestamp": []
        }

    class InvalidAmountError(Exception):
        def __init__(self, amount):
            self.amount = amount
        def __str__(self):
            return f"The shared amount = {self.amount} is not a valid amount, value should not be negative or zero"

    class InsufficientFundsError(Exception):
        def __init__(self, amount, balance):
            self.amount = amount
            self.balance = balance
        def __str__(self):
            return f"The amount {self.amount} cannot be withdrawn, the available balance is {self.balance}"

    def transactionHistory(self, method, amount):
        current_time = datetime.now().strftime("%Y-%m-%d")
        self.transaction_history["Type"].append(method)
        self.transaction_history["Amount"].append(amount)
        self.transaction_history["Balance"].append(self.balance)
        self.transaction_history["Timestamp"].append(current_time)

    def deposit(self, amount):
        if amount <= 0:
            raise Bank_App.InvalidAmountError(amount)
        self.balance += amount
        self.transactionHistory("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise Bank_App.InvalidAmountError(amount)
        if amount > self.balance:
            raise Bank_App.InsufficientFundsError(amount, self.balance)

        total_withdrawal = 0
        for i in range(len(self.transaction_history["Type"])):
            if (self.transaction_history["Type"][i] == "Withdraw" and
                self.transaction_history["Timestamp"][i][:10] == datetime.now().strftime("%Y-%m-%d")):
                total_withdrawal += self.transaction_history["Amount"][i]

        if total_withdrawal + amount <= 50000:
            self.balance -= amount
            self.transactionHistory("Withdraw", amount)
        else:
            raise Exception("Daily withdrawal limit of 50000 reached.")

    def _rollback_last_log(self):
        for column in self.transaction_history.values():
            if column:
                column.pop()

    def transfer(self, other_account, amount):
        if amount > self.balance:
            raise Bank_App.InsufficientFundsError(amount, self.balance)
        try:
            self.withdraw(amount)
            other_account.deposit(amount)
            return True
        except Exception as e:
            self.balance += amount
            self._rollback_last_log()
            raise e

    def get_history_df(self):
        import pandas as pd
        return pd.DataFrame(self.transaction_history)


# ---------- Session-only multi-account state ----------
# Cleared automatically on browser refresh / new session - nothing persists server-side.

if "bank_accounts" not in st.session_state:
    st.session_state.bank_accounts = {}  # name -> Bank_App instance

accounts = st.session_state.bank_accounts

# ---------- Account creation ----------
st.markdown("### Accounts")

with st.form("create_account_form", clear_on_submit=True):
    new_account_name = st.text_input("New account name", placeholder="e.g. Dhruv, Savings, Test1")
    create_submitted = st.form_submit_button("Create account")
    if create_submitted:
        name = new_account_name.strip()
        if not name:
            st.warning("Enter a name for the account.")
        elif name in accounts:
            st.warning(f"An account named '{name}' already exists.")
        else:
            accounts[name] = Bank_App()
            st.success(f"Account '{name}' created.")
            st.rerun()

if not accounts:
    st.caption("No accounts yet. Create one above to get started.")
    st.stop()

# ---------- Account overview ----------
overview_cols = st.columns(len(accounts)) if len(accounts) <= 4 else st.columns(4)
for i, (name, acc) in enumerate(accounts.items()):
    with overview_cols[i % len(overview_cols)]:
        st.metric(name, f"₹{acc.balance:,.2f}")

st.divider()

# ---------- Operations ----------
st.markdown("### Perform an operation")

op_account_name = st.selectbox("Account", options=list(accounts.keys()), key="op_account")
operation = st.radio("Operation", ["Deposit", "Withdraw", "Transfer"], horizontal=True)

acc = accounts[op_account_name]

if operation in ("Deposit", "Withdraw"):
    amount = st.number_input("Amount", min_value=0.0, step=100.0, format="%.2f", key="amount_dw")
    if st.button(f"{operation}", type="primary"):
        try:
            if operation == "Deposit":
                acc.deposit(amount)
                st.success(f"Deposited ₹{amount:,.2f}. Updated balance: ₹{acc.balance:,.2f}")
            else:
                acc.withdraw(amount)
                st.success(f"Withdrew ₹{amount:,.2f}. Updated balance: ₹{acc.balance:,.2f}")
            st.rerun()
        except Bank_App.InvalidAmountError as e:
            st.error(str(e))
        except Bank_App.InsufficientFundsError as e:
            st.error(str(e))
        except Exception as e:
            st.error(str(e))

else:  # Transfer
    other_options = [n for n in accounts.keys() if n != op_account_name]
    if not other_options:
        st.info("Create at least one more account to transfer between accounts.")
    else:
        target_name = st.selectbox("Transfer to", options=other_options, key="transfer_target")
        amount = st.number_input("Amount", min_value=0.0, step=100.0, format="%.2f", key="amount_transfer")
        if st.button("Transfer", type="primary"):
            try:
                acc.transfer(accounts[target_name], amount)
                st.success(f"Transferred ₹{amount:,.2f} from {op_account_name} to {target_name}.")
                st.rerun()
            except Bank_App.InvalidAmountError as e:
                st.error(str(e))
            except Bank_App.InsufficientFundsError as e:
                st.error(str(e))
            except Exception as e:
                st.error(str(e))

st.divider()

# ---------- Transaction history ----------
st.markdown("### Transaction history")
history_account_name = st.selectbox("View history for", options=list(accounts.keys()), key="history_account")
history_df = accounts[history_account_name].get_history_df()

if history_df.empty:
    st.caption(f"No transactions yet for '{history_account_name}'.")
else:
    st.dataframe(history_df, use_container_width=True, hide_index=True)

st.divider()

# ---------- Reset ----------
if st.button("Reset all accounts"):
    st.session_state.bank_accounts = {}
    st.rerun()

st.caption("All accounts and history reset automatically when you refresh or leave this page.")
