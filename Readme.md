# Moneta - Currency Converter Chatbot

**Moneta** is a professional, AI-powered currency converter chatbot built with **Flask**, **Dialogflow**, and **CurrencyAPI**. It provides real-time exchange rates for over 150 currencies through an elegant, minimalist orange-and-white web interface.

---

## 🚀 Features

* **Real-Time Conversions:** Fetches live exchange rates using the CurrencyAPI.
* **Natural Language Processing:** Powered by Dialogflow to understand user queries like "How much is 100 USD in INR?".
* **Modern UI:** A clean, responsive "Sunset Minimalist" frontend designed for high user engagement.
* **Web Integration:** Easy-to-use Dialogflow Messenger integration for web deployment.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask
* **Frontend:** HTML5, CSS3 (Custom UI), Dialogflow Messenger
* **API:** [CurrencyAPI](https://currencyapi.com/)
* **Deployment Tools:** Ngrok (for local development/fulfillment)

---

## 📋 Prerequisites

* Python 3.7+ installed.
* A [CurrencyAPI](https://currencyapi.com/) account and API Key.
* A Dialogflow ES Agent.
* [Ngrok](https://ngrok.com/) installed on your machine.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/currency-converter-chatbot.git
cd currency-converter-chatbot

```

### 2. Install Dependencies

It is recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

```

### 3. Configure API Key

In `app.py`, locate the `fetch_conversion_factor` function and ensure your API key is correctly set.
*Note: For production, it is recommended to use environment variables (`.env`).*

---

## 🏃 How to Run

### Step 1: Start the Flask Server

```bash
python app.py

```

The server will start on `http://127.0.0.1:5001`.

### Step 2: Expose with Ngrok

Open a new terminal and run:

```bash
ngrok http 5001

```

Copy the `https` forwarding URL provided by ngrok.

### Step 3: Configure Dialogflow Fulfillment

1. Go to the **Dialogflow Console**.
2. Navigate to **Fulfillment**.
3. Enable **Webhook** and paste your Ngrok URL.
4. Click **Save**.

### Step 4: Open the Chatbot UI

Since opening the HTML file directly may cause CORS issues, serve it using Python:

```bash
python -m http.server 8000

```

Visit `http://localhost:8000/chatbot/chatbot.html` in your browser.

---

## 📁 Project Structure

```text
.
├── app.py              # Flask backend handling webhook requests
├── requirements.txt    # Python dependencies
├── sample.json         # Sample Dialogflow request for testing
├── .gitignore          # Files to be ignored by Git
└── chatbot/
    └── chatbot.html    # Frontend UI with Moneta branding

```

---