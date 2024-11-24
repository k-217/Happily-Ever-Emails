# Happily-Ever-Emails!

## Introduction

Happily Ever Emails! is a basic application that takes an email from a user, splits it into its username and domain, and allows to send anonymous messages to the mail. 

## Features

1) Built with python backend that employs smtplib for sending mails with SMTP (Simple Mail Transfer Protocols) protocols and tkinter for the user interface, along with SSL that provides TLS encryption in socket-based communication between Python clients and servers and re (regular expressions) that identify a sequence of characters defining a search pattern.
2) Allows you to send anonymous mails (mails from the account linked with the python code, check instructions) to people whom you could not speak in-person and express gratitude and appreciation. 

## Instructions to Run the Application

Simpply, download the python file. Make sure to have downloaded tkinter, smtplib, ssl, and re modules in python. If not, run these commands in the command prompt:

```
pip install tk
```
```
pip install secure-smtplib
```
```
pip install regex
```
```
pip install ssl
```

Then, go to any python compiler and run the code to have a screen displayed on your desktop. Choose between slicing mail ids or sending mails. Follow the simple instructions and there you go!

Please feel free to change the specifications provided according to your preferences. 

To send emails from another address:

1) Ensure that double factor authentication is enabled on that address.
2) Open gmail from that address.
3) Click on the upper right circle button showing profile picture of the id.
4) Click on "Manage your google account".
5) On the search bar type "App passwords" (or find it under the 'Security' section) and click it.
6) Write your gmail password(if it doesn't asks for it, proceed directly to the next step)
7) Click on 'Select app' > 'Other (Custom name)'
8) Type "SMTP Email" and then click on 'GENERATE'.
9) Save the password shown to you now somewhere. (It will not be shown to you again)
10) No open the code in a code editor.
11) Type your email id in place of 'emailslicer8888@gmail.com'. (line 104)
12) Type the password you generated after step 8 in place of 'paaluaugfpcxvkeh' (line 106)

## Future Projections

1) Attaching files in the mails.
2) Getting emails from .csv files and slicing them.
3) Storing the usernames and domains in a database.
4) Adding chatGPT API to generate emails for a specific purpose.
5) Option to view all the recepients added and option to remove them.
6) Specific purpose: Marketing and Sales purposes.
