🚀 GitHub Setup Guide — EduMind AI
Step-by-Step: Upload to GitHub & Enable GitHub Pages
Step 1: Create GitHub Repository
Go to github.com → Sign in
Click "New" (green button)
Repository name: edumind-ai
Set to Public
Do NOT initialize with README (you already have one)
Click "Create repository"
Step 2: Upload Files
Option A — Using Git (recommended):
cd EduMind-AI
git init
git add .
git commit -m "Initial commit: EduMind AI Beta v0.1.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/edumind-ai.git
git push -u origin main
Option B — Upload manually:
On your new repo page, click "uploading an existing file"
Drag and drop all files/folders
Click "Commit changes"
Step 3: Enable GitHub Pages
Go to your repo → Settings tab
Left sidebar → Pages
Under "Source" → Select "GitHub Actions"
The workflow at .github/workflows/deploy.yml will auto-run
Wait 2–3 minutes → your site will be live at:
https://YOUR_USERNAME.github.io/edumind-ai
Step 4: Verify Everything Works
✅ Visit your GitHub Pages URL
✅ Type a question like "What is photosynthesis?"
✅ See the AI respond with subject, difficulty, and confidence
✅ Check the Actions tab to see the deployment succeeded
File Structure to Upload:
edumind-ai/
├── index.html          ← Main GitHub Pages file
├── README.md           ← Project documentation
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml  ← Auto-deployment
├── src/
│   ├── app.py
│   ├── qa_engine.py
│   └── cli.py
├── data/
│   └── knowledge_base.json
├── docs/
│   └── ARCHITECTURE.md
└── tests/
    └── test_qa_engine.py
