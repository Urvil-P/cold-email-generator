from lm import llm

class Email_Generator:
    
    def __init__(self,llm):
        self.llm = llm
        
    def generate_email(self, sender, receiver, purpose):

        subject_template = f'''Write a Proper Email subject for "{purpose}". I only want single subject not more than one.  I dont want to start your response with some acknowledgement sentence or phrases like: 
        -> Sure here is the mail,
        -> Here is the cold mail content,
        -> This is you cold mail to... 
        I hope you understand, I want you to RETURN ONLY EMAIL CONTENT NOT ANY OTHER IRRELEVANT IN YOUR RESPONSE, I just want a single Email SUBJECT for "{purpose}" PLEASE.'''

        content_template = f'''You are a Powerful Cold Email Generator Having Expertise in Various Domains. Please Help "{sender}" generating a code email to "{receiver}" for "{purpose}". Keep it short and in polite tone. You will only return the mail content WITHOUT any ACKNOWLEDGEMENT MESSAGE.
        Just give me the content of the mailm, without any additional irrelevant messages. As your response will automatically send to reciever without human verification.
        
        I dont want to start your response with some acknowledgement sentence or phrases like: 
        -> Sure here is the mail,
        -> Here is the cold mail content,
        -> This is you cold mail to... 

        I hope you understand, I want you to RETURN ONLY EMAIL CONTENT NOT ANY OTHER IRRELEVANT IN YOUR RESPONSE, without any SUBJECT, I JUST WANT EMAIL CONTENT, PLEASE.
        '''

        subject = self.llm.invoke(subject_template).content
        mail = self.llm.invoke(content_template).content
        
        return subject,mail
    

if __name__ == "__main__":
    eg = Email_Generator(llm)
    sub,cont = eg.generate_email("Urvil","Krishna","Stay at Your Place")
    print(sub)
    print(cont)