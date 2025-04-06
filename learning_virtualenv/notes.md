# Virtual Envs
## Creating new virtual envs
**Check python version:**

```
python3 --version
```
**Create new virtualenv**
```
python3 -m venv name_of_your_environment

```
**Activate virtual env**
```
source path_to_your_env/bin/activate
```
## Add virtual env to vs code 
- Get virtual env python path
![Select python path](./assests/select_python_path.png)
- press `clt+shift+p` , select python interpreter
![Select python interpreter](./assests/vscode_python_interpreter.png)
- Select interpreter path
![Select interpreter path](./assests/enter_python_path.png)
![paste interpreter path](./assests/paste_python_path.png)

## Install packages
` python -m pip install package_name `