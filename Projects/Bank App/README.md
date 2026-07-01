# Bank App

A simulated banking system built as an OOP exercise in Python, supporting deposits, withdrawals, transfers between accounts, daily withdrawal limits, and rollback-safe transaction handling.

## Features

- **Deposit / Withdraw** with input validation (`InvalidAmountError` on zero or negative amounts).
- **Daily withdrawal limit** of ₹50,000, tracked per account by summing same-day withdrawals from transaction history.
- **Transfer between accounts**, with automatic rollback (balance and log restored) if the deposit leg fails after a successful withdrawal.
- **Transaction history** as a Pandas DataFrame, logging type, amount, resulting balance, and timestamp for every operation.
- **Custom exceptions**: `InvalidAmountError`, `InsufficientFundsError`.

## Files

- `code.py` — original CLI version. Runs as a terminal menu (`python code.py`), operates on two hardcoded in-memory accounts (`acc1`, `acc2`).

## Running locally (CLI version)

```bash
python code.py
```

Menu options: deposit, withdraw, transfer to the other account, view transaction history, view balance, exit.

## Live demo

This project is embedded in the portfolio site as an interactive Streamlit page. The live version:

- Lets you create any number of named accounts (not just two hardcoded ones).
- Wraps the same `Bank_App` class logic — deposit, withdraw, transfer, limits, and rollback behavior are unchanged.
- Replaces the CLI `input()` loop with Streamlit widgets, since a web app has no terminal stdin.
- Stores all accounts in `st.session_state` only. **Nothing is persisted** — all accounts and history are wiped when you refresh the page or close the tab.

## Notes on the live version

Two small, intentional adaptations were made to the class so it surfaces errors to a UI instead of a terminal:

- `withdraw()` now raises an exception on hitting the daily limit instead of printing and silently returning, so the page can display the error.
- `transfer()` re-raises the underlying error after rolling back, instead of just returning `False`, so the page can show why a transfer failed.

Balances, limits, rollback logic, and exception types are otherwise identical to the original `code.py`.

## Tech

- Python
- Pandas (transaction history as DataFrame)
