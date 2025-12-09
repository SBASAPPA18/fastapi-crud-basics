# FastAPI CRUD Project with React Frontend

A full-stack application demonstrating CRUD operations using FastAPI (Backend) and React + Vite (Frontend).

## 🚀 Features
- **FastAPI Backend**: RESTful API with PostgreSQL database.
- **React Frontend**: Modern UI with dark mode and glassmorphism design.
- **CRUD Operations**: Create, Read, Update, Delete products.
- **Real-time**: Seamless integration between frontend and backend.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, SQLAlchemy, Pydantic
- **Frontend**: React, Vite, Vanilla CSS (Custom Design)
- **Database**: PostgreSQL

## 🏁 Getting Started

### Prerequisites
- Python 3.8+
- Node.js & npm

### 1. Start the Backend
Navigate to the root directory:
```powershell
# Activate virtual environment (Windows)
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```
The API will run at: `http://localhost:8000`

### 2. Start the Frontend
Open a new terminal and navigate to the `frontend` folder:
```powershell
cd frontend

# Install dependencies (first time only)
npm install

# Run development server
npm run dev
```
The UI will open at: `http://localhost:5173`

## 📂 Project Structure
```
/
├── main.py              # FastAPI Application Entry
├── database.py          # Database Connection
├── models.py            # Pydantic Models
├── database_model.py    # SQLAlchemy Models
├── frontend/            # React Application
│   ├── src/             # Frontend Source Code
│   ├── public/          # Static Assets
│   └── package.json     # Frontend Dependencies
└── requirements.txt     # Python Dependencies
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
