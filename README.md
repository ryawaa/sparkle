# Sparkle ✨ - The Engine Behind Twinkle

**Sparkle** is the powerful API that fuels Twinkle, allowing you to keep track of real-time stock prices and company data with ease. This API offers detailed, accurate, and timely financial data, enabling developers to build feature-rich financial applications.

> **Documentation**: [sparkle-demo.ryawaa.com/docs](https://sparkle-demo.ryawaa.com/docs) 📚
> 
> **Live Demo**: [sparkle-demo.ryawaa.com](https://sparkle-demo.ryawaa.com) 🌐
> 
> **GitHub Repository**: [github.com/ryanamay/sparkle](https://github.com/ryanamay/sparkle) 🐙
> 
> **Source Code**: Available on [**code.lgbt**](https://code.lgbt/ryanamay/sparkle) 🏳️‍🌈

---

## Features

- **Real-Time Data**: Get access to real-time stock prices and market data.
- **Comprehensive Endpoints**: Fetch data including company financials, stock recommendations, and news.
- **Broadcast Updates**: Receive real-time updates broadcasted from a single FinHub key.
- **Scalable**: Designed to handle high volumes of requests efficiently.
- **Secure**: Implemented with robust security measures to protect your data.
- **Detailed Documentation**: [API documentation](https://sparkle-demo.ryawaa.com/docs) to help you get started quickly.
- **Source Code Available**: Open source on [**code.lgbt**](https://code.lgbt/ryanamay/sparkle) 🏳️‍⚧️!

---

## 🛠 Running Sparkle Locally

This project is not production-ready, but you can easily run it locally. A feature-rich version is available, but a refactor is on the way in the `branch/refactor`.

### Running Sparkle via Docker (Recommended)
```bash
docker run -d -p 8000:8000 ryanamay/sparkle
```

### Running Sparkle Directly

Sparkle uses Poetry to manage dependencies.

#### 1. Install `poetry`:
##### Via pipx (Recommended)
```bash
pipx install poetry
```

##### Via pip
```bash
python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
```

### 2. Running the app via uvicorn:
```bash
git clone https://github.com/ryanamay/sparkle.git
cd sparkle
poetry install
cd app
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🛠 Deployment

Though it's not yet production-ready, you can deploy Sparkle using any cloud provider that supports Docker or by running it directly on a server. Keep in mind that the current codebase might need refinement for production environments, and the refactor branch is in progress.

---

## 📝 License

Sparkle is licensed under an open-source license. Feel free to use it, contribute, and make it better.
##### Note: The repository is also hosted on code.lgbt – a community-driven git platform for diverse developers! 🌈
