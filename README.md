# jarvic
Jarvic is a learning chatbot. I am trying to copy-paste into Jarvic the learning curve of a newborn baby. It works with Python + Flask.
This is an ongoing project right now...

What's done recently:
- the basic answering and learning functions are up and running
- it's online and available from browser - working with Flask
- it logs all the user reactions into 2 files (words and sentences)
- when you give Jarvic an input, it uses a basic logic to give back an answer - based on the previous conversations it had.
- every time you add an input, it learns it. At the next answer Jarvic may use it's new knowledge.
(I'll add a more detailed discription on the logic of Jarvic, once it's done.)
- it logs each conversation into separated files. (recoverable and reviewable conversations)
- fixed character coding issues

My next todo's:
- Do controlled supervised user tests.
- Find some chatlog material, that I can use to train Jarvic.
- Let Jarvic, evaluate his own answers, too. By scoring from 0 to 10. 0 is when the user left the conversation right after Jarvic's answer. 10 is when user stayed for 10 more "lines".
- Giving the answer based not only on the last user input, but the last 5 user inputs. (Goal: understand if someone teaches "you are" instead of "i am".)
- Identify stopwords automatically.
- Identify reactions by users (eg. words), that predicts longer conversations.
- Ger prepared for typos.