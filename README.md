# jarvic
Jarvic is a learning chatbot. I try to copy-paste into Jarvic the learning curve of a newborn baby. It works with Python + Flask.
This is an ongoing project right now...

What's done recently:
- the basic answering and learning functions are up and running
- it's online and available from browser - working with Flask
- it logs all the user reactions into 2 files (words and sentences)
- when you give Jarvic an input, it uses a basic logic to give back an answer - based on the previous conversations it had.
- every time you add an input, it learns it and on the next answer it may use it's new knowledge
(I'll add a more detailed discription on the logic of Jarvic, once it's done.)

My next todo's:
!.) Log each conversation into separated files.
0.) Find some chatlog material, that I can use to train Jarvic.
1.) Let Jarvic, evaluate his own answers, too. By scoring from 0 to 10. 0 is when the user left the conversation right after Jarvic's answer. 10 is when user stayed for 10 more "lines".
2.) Give the answer based not only on the last user input, but the last 5 user inputs. (Goal: understand if someone teaches "you are" instead of "i am".)
3.) Identify stopwords automatically.
4.) Identify reactions by users (eg. words), that predicts longer conversations.
+1.) Ger prepared for typos.