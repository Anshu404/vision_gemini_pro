# vision_gemini_pro
#
# 🤖 Gemini LLM Q&A Streamlit App

This is a simple Streamlit web application that uses Google's Gemini Pro (via `google-generativeai`) to answer user-input questions using LLM.

---

## 🚀 Features

- Uses **Google's Gemini Pro** model to generate responses
- Streamlit-based interactive UI
- Environment variable management using `.env`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-llm-app.git
cd gemini-llm-app
2. Install required packages
Make sure you have Python 3.8+ installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install streamlit python-dotenv google-generativeai
3. Set up .env file
Create a .env file in the root directory and add your Google API Key:

ini
Copy
Edit
GOOGLE_API_KEY=your_actual_api_key_here
You can get your key from Google AI Studio.

4. Run the app
bash
Copy
Edit
streamlit run app.py
Your app will be available at http://localhost:8501

📁 File Structure
bash
Copy
Edit
.
├── app.py
├── .env
├── README.md
└── requirements.txt
📦 Example requirements.txt
nginx
Copy
Edit
streamlit
python-dotenv
google-generativeai
📷 App Preview
<!-- Optional: Add a screenshot named preview.png in your repo --> <!-- ![App Screenshot](preview.png) -->
🙋‍♂️ Author
Anshu Mandal
IIT Mandi | Data Science

🧠 License
Feel free to use or adapt this app under the MIT License.
