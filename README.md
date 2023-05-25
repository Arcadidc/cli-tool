
# CLI-Tool for the TODO app!

This is a cli-tool in order to interact with the [TODO app](https://github.com/Arcadidc/minikube-node-todo). I changed some things from the original repository that can be found [here!](https://github.com/scotch-io/node-todo) with the changes explained. 

## First steps:
 - First of all check for the config.ini file, where you will be able to edit the IP in order to connect to the API. If you followed the steps correctly you should be available to access in your host machine. 

 - After that, enjoy! You will be able to execute it using `python tool.py`. I put all the dependencies in the `requirements.txt` file. 
 
 ## How to use it:
 
 You have different options with this tool
    
- Get all Todo available in the database, using the flag `--get` or `-g`. You will be also able to select if you want it in json,txt or as a table (by default json). With this command you can also add --path and point where do you want this file. **Example:**

    >  python tool.py --get json 

- Add a new Todo in the database, using the flag `--add` or `-a`. **Example:**

     > python tool.py --add NewTodo

- Delete an existing Todo from the database, using the flag `--delete` or `-d`. You will also need to pass the ID.  **Example:**

     > python tool.py --delete 54454
    
- Execute a Workflow , currently it creates a number of Todo randomly between 0 and 100. After adding the ToDos in the database, it  stores all the information about the Todo in the differents formats (JSON, TXT, Table) and finally it deletes all the ToDos created during this workflow.  **Example:**

     > python tool.py -w

