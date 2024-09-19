# Web Scrawler in Python

This program executes a web scrawler using the data of the main page of [HackerNews](https://news.ycombinator.com/) and storing it in JSON files. 
The program is devoloped in Python 3.12.6 and pip 24.2.

## How execute the program?

To run the program, open a console and go to the directory hackernews/hackernews and execute the file using the command:

```
python menu_crawler.py
```

![image](https://github.com/user-attachments/assets/5780f4f8-b84f-449a-ae87-99cb2e8d4b95)

## What to use the program?

When you execute the previous command, you will see a menu displayed in console, like this:

![image](https://github.com/user-attachments/assets/8ed6a1d9-c516-4728-aa41-470b607be0ad)

### Menu Option 1

If you select option 1, the program will run the web scrawler with all the information of the page:

![image](https://github.com/user-attachments/assets/9ad72df2-fdeb-4588-b35a-4752c660ab19)
![image](https://github.com/user-attachments/assets/5fc1d127-d979-4aab-af1e-5fea4e24afef)
![image](https://github.com/user-attachments/assets/c688a721-ebda-4847-b9da-8aa520ce3acb)
![image](https://github.com/user-attachments/assets/10199eda-0826-41d2-9008-f02191d7f90e)
![image](https://github.com/user-attachments/assets/50a1484e-cfee-4e62-8822-e9a866801fd1)

After the scrawler finished. The information of the JSON file is also showed in console:

![image](https://github.com/user-attachments/assets/004a21fc-ed73-4be8-8e3e-cfcfca78b5c7)

If you want to check the information, in same directory open the file "initial-data.json":

![image](https://github.com/user-attachments/assets/a7c7c9b8-978c-4d6c-b4d8-4e3025cd6253)

### Menu Option 2

If you select option 2, the program will run the first filter with the previous storage data ordered by points field, and also print it in console:

![image](https://github.com/user-attachments/assets/1682eb8b-de20-42ce-b9be-c5d383ad2a73)

If you want to check the information, in same directory open the file "filtered_less_than_or_equal_to_five_words.json":

![image](https://github.com/user-attachments/assets/dabab0f2-772a-4e30-821a-bfa6696fbca5)

### Menu Option 3

If you select option 3, the program will run the second filter with the previous storage data ordered by comments field, and also print it in console:

![image](https://github.com/user-attachments/assets/c6903c9e-7374-4079-bb8d-7fa93847cdf9)

If you want to check the information, in same directory open the file "filtered_more_than_five_words.json":

![image](https://github.com/user-attachments/assets/d5adf670-e600-40ef-8047-1278beb85966)

### Menu Option 4

If you select option 4, the program will run the web scrawler, the first and second filter as a direct example option.

### Menu Option 5

If you select option 5, you exit the program.

## Note
* All options you selected in menu will be store as activity with respective time in the file "user_interaction.json":
![image](https://github.com/user-attachments/assets/b3b7761f-fa61-4f9c-a486-9a564cd62b51)

* If you want more detail about the code, all methods in program are commented describing the functionality.








