# Fractal Export Price Predictor

A FastAPI-based web application that predicts export prices using machine learning. The project integrates an ML model with an interactive web interface, providing real-time predictions with a clean design.

![image alt](https://github.com/PrabhanshuKamal2121/Mega-Project/blob/ea3c63f8a2cf365d4ee426216e21a1f5f79adf57/FRONTEND-PricePredictor.png)


![image alt](https://github.com/PrabhanshuKamal2121/Mega-Project/blob/392ad3a35ddcbd8e2a580f6edcda86c14868355e/How_it_works.jpeg)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34C26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-264DE4?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code)
![n8n](https://img.shields.io/badge/n8n-FF6D70?style=for-the-badge&logo=n8n&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white)

## 📌 Features

- FastAPI backend for high-performance, asynchronous web APIs
- Machine learning model integration for price prediction
- Interactive web interface with custom HTML, CSS, and image branding
- Static file support (logo, CSS, and scripts served from `/static`)
- Deployed on Render with automatic CI/CD via GitHub
- Lightweight & scalable — can be hosted for free on Render's free tier
- Trained model on real-world data, improving accuracy from 11.4% to 78.4%
- Designed custom UI/UX with PostgreSQL integration

## 🚀 Demo

Live App URL: https://fractal-exportprice-predictor.onrender.com
(Deployed on Render — may take a few seconds to spin up on free tier)

## 🏗 Project Structure

```
mega-project/
├── app.py                # Main FastAPI application
├── model.pkl             # Trained ML model (example name)
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Jinja2 template for homepage
├── static/
│   ├── style.css         # Custom styles
│   └── Fractal_logo.png  # Branding/logo file
└── README.md             # Project documentation
```

## 🧠 How It Works

- **Input form**: User provides required data (export product parameters).
- **Backend processing**:
  - FastAPI receives input from the HTML form.
  - Data is validated and sent to the ML model.
- **Model prediction**: Pre-trained model predicts export price.
- **Response rendering**: Results are displayed back on the webpage using a template.

## ⚙️ Installation and Setup

1. Clone this repository

   ```bash
   git clone https://github.com/PrabhanshuKamal2121/Mega-Project.git
   cd Mega-Project
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts\activate       # On Windows
   ```

3. Install dependencies

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Run locally

   ```bash
   uvicorn app:app --reload
   ```

The app will be available at http://127.0.0.1:8000

## 🌐 Deployment on Render

- Push your code to GitHub.
- Create a new Render Web Service → select your repo.
- Configure:
  - **Build Command**:

    ```bash
    pip install --upgrade pip && pip install -r requirements.txt
    ```
  - **Start Command**:

    ```bash
    uvicorn app:app --host 0.0.0.0 --port $PORT
    ```
- Deploy and wait until Render builds and launches your app.
- Access your app at the generated URL.

**Static files note**:\
Make sure you mount static files in `app.py`:

```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

## 🧪 Testing

- Open "http://127.0.0.1:8000/" locally.
- Submit sample input and check prediction results.
- Inspect browser console/network tab to confirm static files load correctly.

## 📂 Key Files

- `app.py` — FastAPI application entry point.
- `templates/index.html` — Main page with input form.
- `static/style.css` — Stylesheet for the webpage.
- `Fractal_logo.png` — Logo used on UI.
- `requirements.txt` — Project dependencies.

## 🔮 Future Improvements

- Add user authentication for private access.
- Save user prediction history in a database.
- Containerize app with Docker for portability.
- Improve frontend with TailwindCSS or React.
- Add REST API endpoint for programmatic predictions.

## 📝 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.
