#Excercise 8-10 and 8-11

#Functions used to print texts in list of messages
def print_messages(messages):
    for message in messages:
        print(message)
#Function used to move texts from list of messages to list of sent messages
def sent_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)

#List of messages
messages = ['Heyyyy', 'How was your day?', '...', 'xD']
#List of sent messages
sent = []

#Calling print_messages to print all messages in list of messages
print_messages(messages)
#Calling sent messages to move all texts in list of messages to list of sent messages.
#Passed a slice to retain values of original list
sent_messages(messages[:], sent)

#Printing both lists to show their respective values
print(messages)
print(sent)