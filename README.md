# 2022 Spring Introduction to Programming in Python Final Project
## Goal
Create a money management application.


## Required Features and Widgets
* Read and save file (keep the records after closing and reopening the window).
* Add a record using tkinter.Entry.
* Prevent users from adding a record with invalid date format.
* Delete a record.
* View the records using tkinter.Listbox.
* View the balance using tkinter.Label.
* Find records under a category.

## Reference Steps
**1. Design your layout and arrange the widgets.**
![](https://i.imgur.com/RB5QmXV.png)

**2. Rearrange the program flow so that the file is read before the window shows and written after the window is closed.**
* Instantiate Categories and Records.
* Create the window and the widgets and call tkinter.mainloop().
* Comment out the while loop prompting for commands and just call records.save() after tkinter.mainloop().

**3. Implement the "update initial money" feature.**
* Update the attribute self._initial_money in the Records class.
* Update the balance in the bottom left corner.
* Check if the initial money is really updated in the file after closing the window.

**4. Show the records read from file in the Listbox.**
**5. Implement the "add a record" feature.**
* Call the add method of the Records class.
* Add the record to the Listbox.

**6. Implement the "delete the selected record" feature.**
* Get the index of the selected record.
* Call the delete method of the Records class.
* Delete the record in the Listbox.
* Update the balance.

**7. Implement the "find the records under a category" feature.**
* Call the find_subcategories method of the Categories class.
* Filter the records and update the content of the Listbox.
* Update the message in the bottom left corner.

**8. Implement the "reset to show all records back" feature.**
* Update the content of the Listbox.
* Update the message in the bottom left corner.


## Related Knowledge
**1. tkinter widges**
* Frame
* Label
* Entry
* Button
* Scrollbar (advanced)
* Messagebox (advanced)
* Combobox (advanced)

**2. Layout managers**
* pack
* grid

**3. command parameter for Button**
**4. StringVar**

## Structure
pymoney is the top module.