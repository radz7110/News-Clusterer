# Step-by-Step: Push to GitHub

Complete guide to get your Topic Clusterer project on GitHub.

## Prerequisites

You need:
- GitHub account (free at https://github.com)
- Git installed (you already have it - verified ✓)
- Your project has git initialized (you already have it - verified ✓)

---

## STEP 1: Create GitHub Repository

### 1a. Go to GitHub
Visit: https://github.com/new

### 1b. Fill in the Form

**Repository name:** 
```
topic-clusterer
```

**Description:**
```
AI-powered topic clustering for news articles using DBSCAN and Claude. 
Scrapes 100+ newspapers, embeds with semantic AI, clusters automatically, 
labels with LLM, visualizes interactively.
```

**Public or Private:**
- Select **Public** (so others can see/use it)

**Initialize this repository with:**
- ✗ Skip "Add a README" (you already have one)
- ✗ Skip "Add .gitignore" (you already have one)
- ✗ Skip "Add a license" (optional for now)

### 1c. Click "Create Repository"

**Don't close this page!** You need the URL next.

---

## STEP 2: Copy the Repository URL

After clicking "Create Repository", GitHub shows you instructions.

Look for this section:
```
…or push an existing repository from the command line
```

You'll see a URL that looks like:
```
https://github.com/YOUR-USERNAME/topic-clusterer.git
```

**Copy this entire URL.** You'll use it in the next step.

---

## STEP 3: Add GitHub as Remote

Open PowerShell in your Topic Clusterer folder:

```powershell
cd "C:\Users\ridhs\Downloads\Projects\Topic Clusterer"
```

Run this command (replace `YOUR-USERNAME` with your actual GitHub username):

```powershell
git remote add origin https://github.com/YOUR-USERNAME/topic-clusterer.git
```

**Example:**
```powershell
git remote add origin https://github.com/radsosa611/topic-clusterer.git
```

**Verify it worked:**
```powershell
git remote -v
```

Should show:
```
origin  https://github.com/YOUR-USERNAME/topic-clusterer.git (fetch)
origin  https://github.com/YOUR-USERNAME/topic-clusterer.git (push)
```

---

## STEP 4: Rename Branch to "main"

```powershell
git branch -M main
```

This renames `master` to `main` (GitHub standard).

**Verify:**
```powershell
git branch
```

Should show:
```
* main
```

---

## STEP 5: Push to GitHub

This is the big moment!

```powershell
git push -u origin main
```

**What this does:**
- `-u` = set upstream (so future pushes are automatic)
- `origin` = your GitHub repository
- `main` = your local branch

---

## STEP 6: GitHub Will Ask for Authentication

### First Time Only

**You'll see:**
```
Username for 'https://github.com':
```

**You have 2 options:**

#### Option A: Personal Access Token (Easier, Recommended)

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"**
3. Give it a name: `topic-clusterer`
4. Select scopes: Check ✓ **repo** (full control of repositories)
5. Click **"Generate token"**
6. **Copy the token** (long string of letters/numbers)
7. **Back in PowerShell**, when asked for password, paste the token

**GitHub will remember it** for next time (doesn't ask again).

#### Option B: SSH Key (More Secure, Slightly Complex)

If you want to set this up later, that's fine. Personal access token is easier for now.

---

## STEP 7: Verify Success

After the push completes, you should see:

```
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 8 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (16/16), 28.23 KiB | 14.12 MiB/s, done.
Total 16 (delta 0), reused 0 (delta 0), writing objects...
remote: https://github.com/YOUR-USERNAME/topic-clusterer.git/tree/main
 * [new branch]      main -> origin/main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**Great!** Your code is on GitHub!

---

## STEP 8: View Your Repository Online

1. Go to: https://github.com/YOUR-USERNAME/topic-clusterer
2. You should see all your files:
   - topic_clusterer.py
   - feeds.json
   - manage_feeds.py
   - README.md
   - etc.

---

## ✅ Complete Checklist

- [ ] Created GitHub repository
- [ ] Copied repository URL
- [ ] Ran `git remote add origin ...`
- [ ] Ran `git branch -M main`
- [ ] Ran `git push -u origin main`
- [ ] Provided GitHub authentication (token or SSH)
- [ ] Verified files appear on GitHub.com
- [ ] ✅ **DONE!**

---

## 🎉 What's Next?

### Share Your Project
Copy your GitHub link and share:
```
https://github.com/YOUR-USERNAME/topic-clusterer
```

### Future Pushes
Next time you make changes, just run:
```powershell
git add -A
git commit -m "Your message"
git push
```

(No need for `-u origin main` again - it remembers!)

### Add More Newspapers
```powershell
# Edit feeds.json
# Then:
git add feeds.json
git commit -m "Add more newspaper sources"
git push
```

### Track Issues & Improvements
GitHub lets you:
- Create Issues (to-do items)
- Add Collaborators (invite friends to contribute)
- Start Discussions (get feedback)

---

## 🔧 Troubleshooting

### "fatal: not a git repository"
**You're in the wrong folder.** Run:
```powershell
cd "C:\Users\ridhs\Downloads\Projects\Topic Clusterer"
git status
```

### "remote origin already exists"
You already added it. Check:
```powershell
git remote -v
```

If it's wrong, remove it:
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/topic-clusterer.git
```

### "Authentication failed"
- Token not working? Generate a new one: https://github.com/settings/tokens
- For SSH help: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### "Branch already exists"
If GitHub says `main` already exists:
```powershell
git push -u origin main --force
```

(Only use `--force` if you're sure - it overwrites)

### Push is slow
This is normal! Your machine is uploading files to GitHub.

---

## 📚 Reference: All Commands in Order

```powershell
# 1. Navigate to project
cd "C:\Users\ridhs\Downloads\Projects\Topic Clusterer"

# 2. Verify git status
git status

# 3. Add GitHub as remote
git remote add origin https://github.com/YOUR-USERNAME/topic-clusterer.git

# 4. Verify remote
git remote -v

# 5. Rename branch
git branch -M main

# 6. Push to GitHub
git push -u origin main

# 7. GitHub asks for password - paste your token

# 8. Verify on GitHub
# Visit: https://github.com/YOUR-USERNAME/topic-clusterer
```

---

## 🎯 One-Minute Quick Reference

**Replace `YOUR-USERNAME` with your GitHub username, then run:**

```powershell
cd "C:\Users\ridhs\Downloads\Projects\Topic Clusterer"
git remote add origin https://github.com/YOUR-USERNAME/topic-clusterer.git
git branch -M main
git push -u origin main
```

Then go to: https://github.com/YOUR-USERNAME/topic-clusterer

Done! 🚀

---

## Need Help?

- **GitHub docs**: https://docs.github.com
- **Git basics**: https://git-scm.com/doc
- **SSH setup**: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
