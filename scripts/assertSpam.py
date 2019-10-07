# Chapter 10
# Asserts asked in the chapter's practice questions

# Creating a function that covers the requested assert statements
def checkAsserts(quest):
    if quest == 1:
        # Assert to check the value of spam
        spam = 10
        print('The value of spam is %s ' %(spam))
        spam = 12
        print('The value of spam is %s ' %(spam))
        assert spam == 10, 'The spam variable has to equal 10.'
    elif quest == 2:
        # Assert to check the values of bacon and eggs
        bacon = 'Hello'
        eggs = 'hello'
        assert bacon.lower() != eggs.lower(), 'The variables bacon and eggs have the same value.'
    else:
        # Assert that always trigger
        assert 1 == 2, 'This assert message will always trigger.'

# Calling the function
checkAsserts(3)