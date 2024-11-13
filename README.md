# How to Run Jyupiter Notenook

### Install Classic Jupyter Notebook 
Open command prompt.
```
pip install notebook
```
Check the installation logs. Find and copy the path where the notebook is installed.

Add it to PATH of your system environment variable.

[Reference](https://jupyter.org/install)


### Run Jupyter Notebook
Open command prompt
```
jupyter notebook
```

# Development

### GitHub
Github is used for development work.\
If you enabled two-factor authentication in your GitHub account you won't be able to push via HTTPS using your accounts password. Instead you need to generate a personal access token. This can be done in the application settings of your GitHub account. Using this token as your password should allow you to push to your remote repository via HTTPS. Use your username as usual.

[Manage your personal access key](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)



# Environment and Setup

### git
To create a local git repo, open command prompt and type the command:

**git clone https://github.com/tuan2174/FWA.git**


### Dev Machine

In your dev machine, 
```
git clone https://github.com/tuan2174/FWA.git
```

Install or Upgrade [Python version 3.13]('https://www.python.org/downloads/release/python-3130/')
Check "Add python.exe to PATH".

### Python Virtual Environment
從Visual Studio Code打開Terminal。
```sh
py -m venv src  
# Run the following commands every time before python work
cd src/scripts
#Activate the environment s
activate
```

### Install Modules
Go to \FWA and run command：
```
$ pip install -r requirements.txt
```
** 當開發過程中有用pip install加新的模組到虛擬環境裡，
不要忘了更新file：
```
$ pip freeze > requirements.txt 
```
