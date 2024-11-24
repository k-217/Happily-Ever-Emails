import tkinter as tk #used for GUI development
import smtplib #used for sending mails via SMTP protocols
import ssl #used for secure network communication over the Internet using the SSL/TLS protocols
import re #used to check if the user has written a valid email address.

main = tk.Tk()

main.title("Emails")
main.geometry("1300x750")
main.configure(bg = "#DC4A3D")

emails = []     #Used to store all the emails, usernames and domains
usernames = []
domains = []

def slicing():  #Called when 'Slice Emails' button is pressed
    sl = tk.Toplevel()
    sl.title("Email Slicer")
    sl.geometry('1300x750')
    sl.configure(bg = "#DC4A3D")

    def emailChk(s):    #Used to check if the given email address in valid

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, s):
            return True
        else:
            return False
   
    def output(): 
        
        e = c.get(1.0, 'end-1c')    #storing the received email address in this variable
        thanks = None
        
        if emailChk(e):
            
            s = e.split('@')
       
            u, d = s[0], s[1]   #'u' is the username and 'd' is the domain

            emails.append(e)

            usernames.append(u)

            domains.append(d)

            output.configure(text = f"Username: {u}\tDomain: {d}")
            
            thanks = True
        
        else:
            output.configure(text = "Please enter a valid email address")
            thanks = False

        if thanks: 
            tk.Label(sl, text = "==============================================================================================================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 7, column = 1, pady = 10, padx = 20, sticky ='w')
            
            tk.Label(sl, text = "Thank you for using Email Slicer! You may proceed to sending emails.", font = ("Courier", 18), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 9, column = 1, pady = 15, padx = 20, sticky = 'w')

            tk.Label(sl, text = "==============================================================================================================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 10, column = 1, pady = 10, padx = 20, sticky ='w')

    tk.Label(sl, text = "Welcome to Email Slicer!", font = ("Courier", 30, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 0, column = 1, pady = 10, padx = 10, sticky = 'w')

    tk.Label(sl, text = "========================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 1, column = 1, pady = 10)

    info = tk.Label(sl, text = "Welcome to Email Slicer! It is an application for separating an email address's username and domain name.\nWe ask you to provide us with an email address and we will present the username and domain as the output.", font = ("Courier", 15), fg = "#F5F5F5", bg = "#DC4A3D")
    info.grid(row = 2, column = 1, pady = 10, padx = 25, sticky = 'w')

    tk.Label(sl, text = "========================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 3, column = 1, pady = 1)
    
    a = tk.Label(sl, text = "Enter Email Address: ", font = ("Courier", 18), fg = "#F5F5F5", bg = "#DC4A3D")
    a.grid(row = 4, column = 1, pady = 10, padx = 20, sticky = 'w')

    c = tk.Text(sl, height = 2, width = 90, font = ("Courier", 18), fg = "#000000", bg = "#CBCBC9")
    c.grid(row = 5, column = 1, pady = 10, padx = 20, sticky = 'w')

    b = tk.Button(sl, text = "Submit", font = ("Courier", 18), fg = "#DC4A3D", bg = "#F5F5F5", command = output)
    b.grid(row = 6, column = 1, pady = 1)

    output = tk.Label(sl, text = "", font = ("Courier", 18), fg = "#F5F5F5", bg = "#DC4A3D")
    output.grid(row = 8, column = 1, pady = 10, padx = 20, sticky ='w')

    tk.Canvas(sl, width=10, height=100, bg = "#F5F5F5").grid(row = 0, column = 0, padx = 20, pady = 10)
    tk.Canvas(sl, width=10, height=100, bg = "#F5F5F5").grid(row = 2, column = 0, padx = 20, pady = 10)
    tk.Canvas(sl, width=10, height=100, bg = "#F5F5F5").grid(row = 2, column = 2, padx = 20, pady = 10)



def send(): #Called when 'Send Emails' button is pressed
    se = tk.Toplevel()
    se.title("Sending Emails")
    se.geometry('1300x750')
    se.configure(bg = "#DC4A3D") 

    def output():

        try:
            
            print("Connecting to server...")

            smtp_port = 587                 # Standard secure SMTP port
            smtp_server = "smtp.gmail.com"  # Google SMTP Server

            email_from = "emailslicer8888@gmail.com"

            pswd = "paaluaugfpcxvkeh" #SMTP password for this email id
            message = c.get(1.0, 'end-1c')

            simple_email_context = ssl.create_default_context()
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from, pswd)
            print("Connected to server :-)")


            #Sending the emails
            if emails != []:

                print('\n',emails,'\n')
                for i in emails:
            
                    print(f"Sending email to - {i}")
                    TIE_server.sendmail(email_from, i, message)
                    print(f"Email successfully sent to - {i}")
            
                msg.configure(text = "All emails sent successfully!")

            else:
                msg.configure(text = "Please enter atleast one email first.")

        except Exception as e: #To print any errors if they occur
            print(e)

    # Close the port
        finally:
            TIE_server.quit()   #Disconnecting from the server
        
        tk.Label(se, text = "==============================================================================================================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 7, column = 1, pady = 10, padx = 20, sticky ='w')

        tk.Label(se, text = "Thank you for using Happily Ever Emails!", font = ("Courier", 18), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 9, column = 1, pady = 15, padx = 20, sticky = 'w')

        tk.Label(se, text = "==============================================================================================================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 10, column = 1, pady = 10, padx = 20, sticky ='w')

    tk.Label(se, text = "Welcome!", font = ("Courier", 30, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 0, column = 1, pady = 10, padx = 20)

    tk.Label(se, text = "========================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 1, column = 1, pady = 10)

    info = tk.Label(se, text = "Welcome! Enter a message below. Please ensure that you have added an email using the Email Slicer before.", font = ("Courier", 15), fg = "#F5F5F5", bg = "#DC4A3D")
    info.grid(row = 2, column = 1, pady = 10, padx = 25, sticky = 'w')

    tk.Label(se, text = "========================================", fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 3, column = 1, pady = 1)
    
    a = tk.Label(se, text = "Enter Message: ", font = ("Courier", 18), fg = "#F5F5F5", bg = "#DC4A3D")
    a.grid(row = 4, column = 1, pady = 10, padx = 20, sticky = 'w')

    c = tk.Text(se, height = 2, width = 90, font = ("Courier", 18), fg = "#000000", bg = "#CBCBC9")
    c.grid(row = 5, column = 1, pady = 10, padx = 20, sticky = 'w')
    
    msg = tk.Label(se, text = "", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D")
    msg.grid(row = 8, column = 1, pady = 10, sticky = 'w', padx = 20)

    b = tk.Button(se, text = "Submit", font = ("Courier", 18), fg = "#DC4A3D", bg = "#F5F5F5", command = output)
    b.grid(row = 6, column = 1, pady = 10)

    tk.Canvas(se, width=10, height=100, bg = "#F5F5F5").grid(row = 0, column = 0, padx = 20, pady = 10)
    tk.Canvas(se, width=10, height=100, bg = "#F5F5F5").grid(row = 2, column = 0, padx = 20, pady = 10)
    tk.Canvas(se, width=10, height=100, bg = "#F5F5F5").grid(row = 2, column = 2, padx = 20, pady = 10)
    tk.Label(se, text = "P.S. All the mails are sent anonymously.", font = ("Courier", 12), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 11, column = 1, pady = 1, padx = 20, sticky = 'w')
    tk.Label(se, text = "Appreciate your acquaintances, be grateful to someone, and send lovely notes to the ones who stood before you!", font = ("Courier", 12), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 12, column = 1, pady = 1, padx = 20, sticky = 'w')

#Code for the main menu
tk.Label(main, text = "Happily Ever Emails!", font = ("Courier", 50, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 0, column = 1, pady = 5, padx = 20)
tk.Label(main, text = "Welcome to Happily Ever Emails!", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 2, column = 1, pady = 20, padx = 10, sticky = 'w')
tk.Label(main, text = "This app is curated as a simple messaging device for the users.", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 4, column = 1, pady = 5, padx = 10, sticky = 'w')
tk.Label(main, text = "Here are the steps to access it:", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 5, column = 1, pady = 5, padx = 10, sticky = 'w')
tk.Label(main, text = "1. Click on Email Slicer. Type an email address. We shall split it for you.", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 6, column = 1, pady = 5, padx = 10, sticky = 'w')
tk.Label(main, text = "2. Close Email Slicer and let yourself come to the home page. Now, click the second button.", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 7, column = 1, pady = 5, padx = 10, sticky = 'w')
tk.Label(main, text = "3. Type your message on the screen and it will reach to the specificed mail address in a few seconds.", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 8, column = 1, pady = 5, padx = 10, sticky = 'w')
tk.Label(main, text = "Thankyou for considering us as your e-mailing companion!", font = ("Courier", 18, "bold"), fg = "#F5F5F5", bg = "#DC4A3D").grid(row = 9, column = 1, pady = 5, padx = 10, sticky = 'w')

tk.Button(main, text = "Slice Emails", font = ("Courier", 30, "bold"), fg = "#F5F5F5", bg = "#DC4A3D", command = slicing).grid(row = 10, column = 1, pady = 20, padx =20, sticky = 'w')
tk.Button(main, text = "Send Emails", font = ("Courier", 30, "bold"), fg = "#F5F5F5", bg = "#DC4A3D", command = send).grid(row = 12, column = 1, pady =20, padx = 20, sticky = 'w')

tk.Canvas(main, width = 400, height = 5, bg = "#F5F5F5").grid(row = 1, column = 1, padx = 20, pady = 10)
tk.Canvas(main, width = 10, height = 100, bg = "#F5F5F5").grid(row = 10, column = 0, padx = 20, pady = 10)
tk.Canvas(main, width = 10, height = 100, bg = "#F5F5F5").grid(row = 12, column = 0, padx = 20, pady = 10)
tk.Canvas(main, width = 300, height = 10, bg = "#F5F5F5").grid(row = 11, column = 1, padx = 20, pady = 10, sticky = 'w')

main.mainloop() #Is responsible for running the main event loop of the Tkinter GUI application
