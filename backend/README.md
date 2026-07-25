# CareerPilot Backend Deployment

## Vercel Backend
1. Create a new Vercel project and point it to the `backend` folder.
2. Ensure `backend/requirements.txt` is present.
3. Add `backend/vercel.json` and `backend/api/index.py`.
4. In Vercel project settings, add environment variables:
   - `GROQ_API_KEY`
   - `GROQ_MODEL` (optional, default: `llama-3.3-70b-versatile`)
   - `LLM_TEMPERATURE` (optional, default: `0`)
5. Deploy. The backend will expose `/api/index` as a serverless endpoint; your frontend should use the full URL returned by Vercel.

## Render Backend
1. Create a new Web Service on Render.
2. Set the root directory to `backend`.
3. Set the environment to Python 3.11 or 3.12.
4. Set the build command to:
   ```bash
   pip install -r requirements.txt
   ```
5. Set the start command to:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Add environment variables:
   - `GROQ_API_KEY`
   - `GROQ_MODEL`
   - `LLM_TEMPERATURE`

## Frontend Configuration
1. In the frontend, use the environment variable `VITE_API_BASE_URL`.
2. In Vercel, set `VITE_API_BASE_URL` to the backend URL from Render or Vercel.

Example frontend request URL:
```
https://your-backend-url.vercel.app/api/index
```
