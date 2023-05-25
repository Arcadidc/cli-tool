
##### CLI-TOOl for the TODO app!

This is a cli-tool in order to interact with the [TODO app](https://github.com/scotch-io/node-todo). I changed some things in that repository (can be found [here](https://github.com/Arcadidc/minikube-node-todo)) with the changes explained. 

## First steps:
 - First of all check for the config.ini file, where you will be able to edit the IP in order to connect to the API. If you followed the steps correctly , it should be available in your host machine. 

 - After that, enjoy! You will be able to execute it using `python tool.py` if you have set the  Python environment correctly. I put all the dependencies in the `requirements.txt` file. 
 
 ## How to use it:
 
 You have different options with this tool
    
    - Get all ToDo available in the database, using the flag --get or -g. You will be also able to select if you want it in json,txt or as a table (by default json). With this command you can also add --path and point where do you want this file.

        *Example* : python tool.py --get json 

    - Add a new ToDo in the database, using the flag --add or -a.

         *Example* : python tool.py --add NewTodo

    - Delete an existing ToDo from the database, using the flag --delete or -d.

        *Example* : python tool.py --delete 54454
    
    - Execute a Workflow , currently it creates a number of ToDo randomly between 0 and 100. After adding the ToDos in the database, it  stores all the information about the ToDo in the differents formats (JSON, TXT, Table) and finally it deletes all the ToDos created during this workflow.

