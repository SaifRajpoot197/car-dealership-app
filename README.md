# 🚗💰 Tkinter Wallet & Car Dealership Simulator

An interactive desktop GUI application built with Python's **Tkinter** library. This app lets users manage a virtual wallet, add custom amounts via an input box, and buy or sell a car with real-time balance validation.

## ✨ Features
* **Starting Balance:** Begins with **\$7,000** displayed clearly on the screen.
* **Quick Cash Controls:**
  * **Add Money:** Instantly add **+\$1,000** to your wallet.
  * **Spend Money:** Deduct **-\$1,000** from your balance.
* **Custom Money Entry:** Type any custom number into the input field and click **Money Added** to deposit it.
* **Buy Car (With Balance Check):** Purchase a car for **\$5,000**. If you don't have enough funds, the app alerts you with `"Not enough Money"`.
* **Sell Car:** Sell your car back for **\$4,000** and update the status to `"Car: Sold!"`.

## 🛠️ Technologies Used
* **Python 3**
* **Tkinter** (Standard Python GUI library)

## 🚀 How to Run the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project folder:**
   ```bash
   cd YOUR-REPO-NAME
   ```

3. **Run the Python script:**
   ```bash
   python main.py
   ```
   *(Make sure to replace `main.py` with your actual file name).*

## 🔮 Future Improvements
* Track car ownership state so the user can only sell a car if they actually own one.
* Prevent `spend_money()` from dropping the balance below **\$0**.
* Add error handling (`try-except`) for non-numeric text in the custom money entry box.
