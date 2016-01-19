--- layout: post title: Setting up an ODBC connection in Windows
created: 1291233660 categories: [] ---

### Installing the MySQL ODBC driver (do this step once) {style="font-weight: bold; font-style: inherit; font-size: 15px; font-family: 'Segoe UI', 'Lucida Grande', Arial, sans-serif; vertical-align: baseline; line-height: 1.25em; color: #444444; padding: 0px; margin: 0px; border: 0px initial initial;"}

1.  Download the appropriate MyODBC driver
    from [http://dev.mysql.com/downloads/connector/odbc/5.1.html](http://dev.mysql.com/downloads/connector/odbc/5.1.html)
2.  Run the file as an administrator
3.  Follow the prompts to install the driver. You will just use the
    defaults so just keep clicking next/OK until the installation is
    finished

 

### Setting up Windows to access a database on Serenity (do this step once for each database) {style="font-weight: bold; font-style: inherit; font-size: 15px; font-family: 'Segoe UI', 'Lucida Grande', Arial, sans-serif; vertical-align: baseline; line-height: 1.25em; color: #444444; padding: 0px; margin: 0px; border: 0px initial initial;"}

1.  Open the **Control Panel**
2.  Open the **Administrative Tools**
    1.  If you are using the **Classic View** the **Administrative
        Tools** link should be in the **Control Panel** window
    2.  If you are using the **Category View** first open **Performance
        and Maintenance**the open **Administrative Tools**

3.  Open **Data Sources (ODBC)** using your administrative account by
    right clicking on the icon and selecting **Run As**
    1.  Click the **The following user** radio button
    2.  Enter your admin username and password
    3.  Click **OK**

4.  Select the **System DSN** tab
5.  Click **Add**
6.  Select the **MySQL ODBC Driver**
7.  Click **Finish**
8.  Enter a name for the remotely accessed database in **Data Source
    Name** (e.g., BBS\_on\_Serenity)
9.  Enter a description of the database if it will be helpful to you
10. In the **Server** box enter the name of the server
11. In the **User** box enter your MySql username
12. In the **Password** box enter your MySql password
13. Click on the arrow at the right hand side of the **Database** box
    and wait patiently for a few seconds
14. You will see a list of the databases on Serenity that you have
    access to
15. Click on the database you want and press **OK** twice

 

### Accessing the data in Access 2007 {style="font-weight: bold; font-style: inherit; font-size: 15px; font-family: 'Segoe UI', 'Lucida Grande', Arial, sans-serif; vertical-align: baseline; line-height: 1.25em; color: #444444; padding: 0px; margin: 0px; border: 0px initial initial;"}

1.  Open the Access database that you want to have access (alright, now
    it's just annoying) to the MySQL database you've setup using ODBC
    (or start a new database)
2.  Select the **External Data** tab on the **Ribbon**(the tabbed
    toolbar at the top of the screen)
3.  In the **Import** section select **More** and then **ODBC Database**
4.  Click the **Link to the data source by creating a linked
    table** radio button (this will mean that you will always be working
    with the most up to date data and that if you have editing
    priveldges that you will be able to insert or modify data on the
    server.
5.  Click **OK**
6.  Select the **Machine Data Source** tab
7.  Select the **Data Source** **Name** for the ODBC data source you
    created (if the data source you setup is not present see below for
    an alternative approach)
8.  Click **OK**
9.  In the list of **Tables** select the tables you wish to include in
    your Access database and click **OK**
10. The tables will appear in their own group and the fact that they are
    linked from the server will be indicated by a picture of the earth
    next to the table name.
11. You can now treat this like any other table in your database.
12. If you want to remove the link, just right click on the table and
    select **Delete**

 

### Setting up an ODBC source directly in Access 2007 {style="font-weight: bold; font-style: inherit; font-size: 15px; font-family: 'Segoe UI', 'Lucida Grande', Arial, sans-serif; vertical-align: baseline; line-height: 1.25em; color: #444444; padding: 0px; margin: 0px; border: 0px initial initial;"}

1.  If Access does not display the desired database after following
    Steps 1-16 of "Setting up Windows..."
2.  Simply follow steps 1-6 of "Accessing the data...", then
    click **New**
3.  Select **System Data Source** and hit Next.
4.  Follow steps 6-16 of "Setting up Windows..."

 

Source: This started as a modification/simplification of
the [walkthrough at devshed by W.J.
Gilmore](http://www.devshed.com/c/a/MySQL/MySQL-and-ODBC/), which has
been generously modified and added to by the members of
[weecology](http://weecology.org).
