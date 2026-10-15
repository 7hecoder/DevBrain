# DevBrain

DevBrain is a developer utility toolkit providing practical tools for common programming tasks through a React frontend and a FastAPI backend.

## Features

- Secure password generation
- UUID generation
- Text hashing (MD5, SHA-1, SHA-256, SHA-512)
- Unix timestamp conversion
- Base64 encoding and decoding
- JSON formatting and validation
- URL encoding and decoding
- Text comparison and diff generation
- Regular expression testing
- JWT header and payload decoding (without signature verification)

## Tech Stack

**Frontend:** React, Vite, Tailwind CSS

**Backend:** Python, FastAPI, Pydantic

## Run Locally

### 1. Start the backend

Open a terminal:

```bash
cd ~/project/DevBrain/backend
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend API: `http://127.0.0.1:8000`

Interactive API documentation: `http://127.0.0.1:8000/docs`

### 2. Start the frontend

Open a second terminal:

```bash
cd ~/project/DevBrain/frontend
npm install
npm run dev
```

Open the local URL printed by Vite in your terminal.

## Security Notes

- Passwords are generated using Python's `secrets` module.
- JWT decoding does not verify signatures. Decoded claims must not be trusted without independent verification.
- MD5 and SHA-1 are provided for compatibility and should not be used for security-sensitive hashing.
- Do not commit credentials, environment files containing secrets, or virtual environments.

## Project Status

Under active development.
