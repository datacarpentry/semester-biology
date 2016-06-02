---
layout: page
title: Forms in Access
---

Forms allow us to manage how data is entered.
They allow us to simplify data entry by:

* Only presenting the fields that need to be added
* Presenting fields from multiple tables in a single view
* Controlling the data that is actually entered to help make sure it is valid

Creating a basic form
---------------------

We can create a basic form by:

1. Selecting the table we want to create the form for
2. Clicking on the **Create** tab
3. In the **Forms** section of the ribbon selecting the **Form Wizard**
4. Selecting the fields that we want to include the in form at adding them with the **>**
5. Choosing the data layout
6. Giving the form a name
7. Pressing **Finish**

### Example

* Portal database
* Plots table
* No PlotID (because it is autonumber)
* Columnar

Using a basic form
------------------

We can now use this form to look at the contents of the table using the arrows,
or add a new record by clicking on the arrow with the star next to it.

Once the new data has been entered we can add it to the database by either pressing the arrow with the star again,
or by pressing tab while in the last field.

Even without any more work forms will stop major data entry errors based on the data type.

Quality Assurance Basics
------------------------

We can provide much better control over data entry using forms.

1. Go to **Design View**
2. Select the data entry field you want to control
3. If it is not already open, open the **Property Sheet**
4. In the **Validation Rule** box enter the rule to limit values that can be entered
5. Optionally, enter text to return if the rule is violated in the **Validation Text** box

### Example

* List of possible strings for PlotTypeAlphaCode
* Restrict numeric codes to between 0 and 4

Selection options from a list
-----------------------------

We can also simple give users a list of options to select from.

1. Right click on data entry field
2. Select **Change To** and then the kind of box you want to supply
3. In the **Property Shee** click in the **Row Source** box and then click on the three dots
4. Now build a query that gives you the values you need
5. Click **Close**
6. Click **Yes**
7. Now the user just selects one of the options that you have given them

### Example

* List box for alpha codes
* The combo box for alpha codes

This is only the beginning
--------------------------

There are *many* other things that you can do using forms.
You can add buttons for starting new records, saving changes, or performing other tasks.
You can edit forms in multiple tables simultaneously and
have the values you enter for one table influence the values in another.
And many other powerful and useful controls.
