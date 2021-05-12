email=input("Enter Your EmailId:- ")
name=email[:email.index("@")]
domain=email[email.index("@")+1:]
print("Your Username--",name)
print("Domain--",domain) 
