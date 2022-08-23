# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON

This repository has all the code used as part of the 202230 OOP class offered at Universidad del Norte


## How to use this repo

To use this repo you need to following pre-requisites:

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Miniconda is a python package manager that will help you create a virtual environment with all the dependencies installed.
- Install VSCode. [link](https://code.visualstudio.com/download). VSCode is a free IDE that is very popular to this day with tons of features and very lightweight. 
- Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VsCode
- Install [Git](https://git-scm.com/downloads)
- Clone this repository in a folder in your computer by running 
    ```
    git clone https://github.com/jdposada/oop_202230.git
    ``` 
    - The folder where you clone this repo will be names `<repo_folder>` from now on. 
- Open the cloned repository on VSCode
- Open the Anaconda prompt and navigate to your folder by typing 
    ```
    cd <repo_folder>/oop_202230
    ``` 
    and type 
    ```
    conda create -y -n oop_202230 --file requirements.txt
    ``` 
    - The last command will create a virtual environment for you with all the required packages. Anaconda prompt should be available either on your desktop or in your program list. 
- Press `CTRL + Shift + P` and type `Python: Select Interpreter`. Select the virtual environment with name `oop_202230 `
- Run `tests/test_installs.py` on this repo to check that everything is ok. You should get an **OK** message at the end of the run. 

## Support Material

We will be using material from several places, but mostly the material created by the authors of our main textbook. The code can be found in this [link](https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition). Portions of such code will be available in this repo with the proper attributions and modifications. 

## Personal Remote Development Environment on Cloud

### Azure setup and VM

- Open an [Azure Student Account](https://azure.microsoft.com/en-us/free/students/) using your Uninorte email. This will give you 100 USD in credits
- Start a VM with 2 Cores and 4GB of RAM. If possible select `Standard_B2s`, this specific VM has those characteristics and cost about ~0.04USD/hour. We will cover how to do this in class. We will use Ubuntu 20.04. Here some [instructions](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)
- Connect to the VM using SSH. If you are in windows you will need to use a [compatible SSH client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client). if you are in Ubuntu you are all set. the command you will need to run is something like this:
```
ssh oopclass@10.1.1.1
``` 
 In this command oopclass is the user that was created during the VM creation and the IP is assigned automatically by Azure.
- *Optional*
    - If you want to login on Github and you have two factor authentication enabled you need to first
        - [Generate a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
        - Run these commands so your Git credentials are stored along with your information
            ```
            git config --global credential.helper store
            git config --global user.name "Your Name"
            git config --global user.email you@example.com
            ```
- Clone our course repository on /home/$USER **inside the VM**:
```
git clone https://github.com/jdposada/oop_202230.git
```
- *Optional*
        - You could decide to [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the main repo so you have minor changes and other files in it. If that is the case you could keep it private. If you made this decision you should clone your fork instead of the class repo. Keep in mind you need to [keep your fork updated](https://stackoverflow.com/questions/39819441/keeping-a-fork-up-to-date)

### Locally

- On your **local** VSCode instance the following extension need to be installed
    -  [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- Here some summary on the instructions [here](https://code.visualstudio.com/docs/remote/ssh) to connect to our VM using SSH through VS Code. Press `CTRL + Shift + P` and:
    - Type `Remote-SSH: Connect to Host`
    - Select `Add New SSH host`
    - Type in your user and IP from the VM. It should be something like this `oopclass@10.1.1.1`. The user (oopclass) was created during the VM creation and the IP is assigned automatically by Azure.
    - Type the password that was defined during the creation of the VM.
- Now your VS Code should be connected to the VM.
