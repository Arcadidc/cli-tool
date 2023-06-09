
# CLI-Tool for the TODO app!

This is a cli-tool in order to interact with the [TODO app](https://github.com/Arcadidc/minikube-node-todo). I changed some things from the [original](https://github.com/scotch-io/node-todo) repository. To make this application work you first should have your minikube cluster running and accessible.

## First steps:
 - First of all check for the config.ini file, where you will be able to edit the IP in order to connect to the API. If you followed the steps correctly from the other project you should be available to access from your host machine. 

 - After that, you will need to install de dependencies that can be found in the file `requirements.txt` with the command `pip install -r requirements.txt`. After that you will be able to execute it using `python3 tool.py`.
 
 ## How to use it:
 
 You have different options with this tool
    
- Get all Todo available in the database, using the flag `--get` or `-g`. You will be also able to select if you want it in json,txt or as a table (by default json). With this command you can also add `--path` and point where do you want this file. **Example:**

    >  python3 tool.py --get json 

- Add a new Todo in the database, using the flag `--add` or `-a`. **Example:**

     > python3 tool.py --add NewTodo

- Delete an existing Todo from the database, using the flag `--delete` or `-d`. You will also need to pass the ID.  **Example:**

     > python3 tool.py --delete 54454
    
- Execute a Workflow , using the flag  `--workflow` or `-w`. It creates a number of Todo randomly between 0 and 100. After adding all the Todo in the database, it  stores all the information  in differents formats (JSON, TXT, Table) and finally it deletes all the Todos.  **Example:**

     > python3 tool.py -w

