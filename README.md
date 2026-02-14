# Git & Git Hub Essentials
## 🔗Introduction
💻 Git is a "Version Controlling System" this is where we say *"you can save you work progress step by step as versions or something like phases or stages* in plain language. 

### 🔄How is this relevent to Software development Industry?
In general we can manage our break points or any specific milestone in a software develepment product by just **"simply save or make a copy of our work and save somewhere on the hard disk or any other backup storage** same as that but in more clean,easy and comprehensive way the **GIT** is tool that aid us to do that. 

In **GIT** we make **branchs** to track and id our work flows in the IDE or any kind of interface where we develop our product. Here we can form many branchs, the first branch we make will be **Default : Main/Master** branch this is the branch we keep our clean, accurate and working product progress. 

Apart from the Main branhc, we can make more and more branch as much as we want and we need in occationally. But we need to be ***aware*** that from which branch we should split our new branhcs. So at the end when real development project, a **Tree** like structure is what we can get. 

🖋️ The most crucial thing we must understand is this tree structure, where we should aware that from which branhc we are on currently and from where our branh will split into 

### Example
Imagine we are developing an **API** API can have several major components, 

    ✅ Endpoints 

    ✅ Controllers 

    ✅ Models 

    ✅ Middleware/auth 

    ✅ Business Logic 
are some among from them. 

We can start with **Main** branch, and we can form branchs from **Main** and seperate our individual components at another phase where we wont mx with our code from **Main** delivery progress.  
### branches from Main branch
    🔀feature/endPoints
    🔀feature/models 
        🔀feature/models/dbtables 
        🔀feature/models/methods
    🔀feature/businessLogic 
As you can see we can form branches not for like we like it, but for we want to seperate and break down bigger tasks in to smaller tasks and merge them upward and finally merge to Main branch where we actually develop and deliver the product. 

    We use GIT for manage local machine/computer code version controlling
    We use Git Hub for share our code with other developers, work together and contribute for common project etc. 

## GIT -Installaztion - Windows
You can download GIT from the,   `https://git-scm.com/install/windows`
[download here](https://git-scm.com/install/windows)  

## GIT -Installaztion - Linux 
### Debian/Ubuntu 
For the latest stable version for your release of Debian/Ubuntu 
```
apt-get install git
``` 
For Ubuntu, this PPA provides the latest stable upstream Git version  

### Fedora 
(up to Fedora 21)
```
yum install git
``` 
(Fedora 22 and later)
```
dnf install git
```

## ⚙️Configuratoin

After installation, check the GIT versoin and working fine. 
```
git --version
```
Add a name and e mail to identify commits and ownership 
```
git config --global user.name "Your Name"
```
```
git config --global user.email "email@example.com"
```
To check the entered details
```
git config --list
```
## GIT-Commands (Local)
### initiate GIT 
```
git init
```
### Adjust GIT master branch to Main
```
git config --global init.defaultBranch main
```
### Check Git status
```
git status
```
### Add all modified files and folders
```
git add .
```
### Add particular file
```
git add fileName.extension
```
### After staging commit the changes to the relavent branch
```
git commit -m "the commit message goes here"
```
### Check branch status
```
git status
```
### Check git history
```
git log
```
### Check older version code (wont save new modifications)
```
git checkout [commit-hashvalue]
```
### Make a new branch
```
git branch branch_name
```
### Make a new branch and jump to it
```
git checkout -b branch_name
```
### Delete a branch (MAKE SURE YOU ARE IN MAIN / ANOTHER BRANCH)
*✴️ only delete if the branch is merged*
```
git branch -d branch_name
```
### Forced delete a branch
```
git branch -D branch_name
```
### Delete a branch from gitHub Server from Local
```
git push origin --delete branch_name
```
## GIT-Commands (Local & GitHub)
To share the Local development progress we need remote server very much like Git, and that is GitHub. 
Once you perfectly able to create an account on GitHub you can make new ***Repositories*** for each project /task/ work.  

### Establishing connection from repo to Local project folder
First we have to copy the url from the repo.  
#### 1. Establish repo url to Project folder
```
git remote add origin [git_repo_url]
```
#### 2. Check and verify the connection
```
git remote -v
```
#### 3. Publish the Main branch
```
git push -u origin Master
```
### Add any branch (Publish) to repo
```
git push -u origin branch_name
```
### Push changes (After published any branch push is enough)
```
git push
```
### Sync or update local branch with repo branch
Here we do `git fetch` and `git merge` 2 in one command
```
git pull
```
