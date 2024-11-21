import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import random
import string
import math
from spellchecker import SpellChecker
spell = SpellChecker() # instantiates this class that will check if the words found in the Boggle are correct


class AccessFiles(): # a class that accesses and creates the files needed for the competition
    def __init__(self):
        # when the system is to be used for the competition I will manually change the path to the ones which can be access by the school computers
        self.entries = os.listdir('/Users/adeituraandu/Desktop/spelling bee files') #creates a list of the directories/folders that can be access by this file path
        self.path = '/Users/adeituraandu/Desktop/spelling bee files' # is a set path that can be reused throught the code


    def CreateNewFolder(self, nameOfYear, label, label2): # the method creates the folder in the specified file path
        for i in range(len(self.entries)): # loops through the list of folders
            if nameOfYear == self.entries[i]: # checks if the folder name entered by the user is equal to a folder already created 
                # lets the user know that the year they have entered has already been created
                label.config(text="This year has already been created. \n If you would like to access this year go back and select 'Open Existing Game'.")

        newFolder = os.mkdir('/Users/adeituraandu/Desktop/spelling bee files/'+ nameOfYear) # makes a directory/folder using the year entered by the user
        for i in self.entries:
            if nameOfYear == i:
                raise Exception("This file already exists")

        self._CreateNewCompetitionFiles(nameOfYear, label2)# goes to the method that creates all the file needed for the competition


    def _CreateNewCompetitionFiles(self, nameOfYear, label): #creates the set files needed for the competition when a new one is created

        # stores the list of the files to be added into the new folder
        fileNames = ["Year 7 Maths Words", "Year 7 English Words", "Year 7 Science Words", 
                    "Year 8 Maths Words", "Year 8 English Words", "Year 8 Science Words", 
                    "Year 9 Maths Words", "Year 9 English Words", "Year 9 Science Words", 
                    "Year 10+ Maths Words", "Year 10+ English Words", "Year 10+ Science Words", 
                    "Anagram File", "Original Anagram File"]
        
        for i in fileNames: #for loop that loops through the items in the fileNames list
            print("i: ", i)
            self._AddFilesToFolder(i, nameOfYear) #calls the method that will add the files to the selected folder
        label.config(text = "Successfully created a new year")
        self.entries.append(nameOfYear) #adds the year chosen by the user into the list of folders in the directory previously stated
        self.GetYear(nameOfYear) #calls the method that will allow the user to access the folder they would like

    
    def _AddFilesToFolder(self, f, nameOfYear): # method that adds the files into the specified folder
        newPath = os.path.join(self.path, nameOfYear, f) # creates a new path that will lead to the items needed in the folder previsouly chosen
        print("new path: ", newPath) # prints the new path
        with open(newPath, "w") as file: #opens the file path leading to the specified file in write mode 
            print(file) #prints the file


    def OpenExistingFolder(self, label): # method that opens an existing folder
        while '.DS_Store' in self.entries: # while loop that is used to search through the list self.entries to find the specified string
            self.entries.remove('.DS_Store') # removes 'DS_Store' which is stored in the self.entries so that it is not visible to user when selecting a year
        print(self.entries) # prints the list of folders and files in the specified folder
        self.entries = [s for s in self.entries if s.isnumeric()] # removes any items in the list that are not previous years created for the competition
              

        print(self.entries)
        label.config(text = self.entries) # edits the label to produce the list of years that the user can select
        #self.GetYear() # calls the method that will allow the user to access the files in the year group they selected
        

    def GetYear(self, chooseYear, label, entryBox): # a method that allows the user to access the files in the specified folder
        global listOfFiles # makes a list of files a global variable
        listOfFiles = [] # a list to store the files in the specified year
        for i in range(len(self.entries)): # loops through the list self.entries
            if self.entries[i] == chooseYear: # checks to see if the user input is equal to an item in the list of self.entries
                print(chooseYear)
                print(self.entries[i])
                #print("successful")
                
                filesInYear = os.listdir('/Users/adeituraandu/Desktop/spelling bee files/'+ self.entries[i]) # creates a list of the files available in the specified folder
                for files in filesInYear: # for loop that loops through the filesInYear and stores it in a variable called files
                    print(files)
                    listOfFiles.append(files) # adds the variable files into listOfFiles
            else:

                print(chooseYear)
                print(self.entries[i])
                #print("unsuccessful")
                
        if len(listOfFiles) == 0:
            label.config(text = "This year does not exist \n please enter one from the list presented")
            entryBox.delete(0, tk.END)
        else:
            label.config(text = "Successful")

        print("list of files in", chooseYear, "folder", listOfFiles) # prints the list of files for the specified year


    def editFile(self, file, year): # a method that allows the files to be edited
        for i in range(len(listOfFiles)): # loops through the listOfFiles
            if file == listOfFiles[i]: # if the user input passed into the subroutine as file is equal to an item in the listOfFiles 
                print(listOfFiles[i])
                print(file)
                path = os.path.join(self.path, year, file) # creates a new path 
                c = CreateSpellBeeWords() # creates an instance of the CreateSpellBeeWords class
                c.CreateWords(path, year) # calls the method CreateWords
    
    
    def editAnagramFile(self, file, year, data): # a method that edits the anagram files
        if file == "Anagram File": # checks if the string entered by the user which is passed in as the variable file is equal to the anagram file in the folder specified
            print(file)
            path = os.path.join(self.path, year, file) # creates a new path
            CopyToTextBox(path, data) # calls the subroutine which 
        elif file == "Original Anagram File":
            print(file)
            path = os.path.join(self.path, year, file)
            #Opath = os.path.join(self.path, year, file)
            AddUserInputIntoList(path, year)


    def EditLoginFiles(self):
        logins = ["Teacher Login Details", "Student Login Details"] # a list with the names of the login files for the teacher and students
        for i in logins: # loops through the list 
            newPath = os.path.join(self.path, i) # creates a path that opens each file name
    
            if i == "Teacher Login Details": # checks if the name of the file is for the teacher login and stores the teacher login details in the file
                file = open(newPath, "w") # opens the teacher login file in write mode
                file.write("teacher") # username
                file.write(" ") # creates a space so the username and password can be differntiated
                file.write("Password") # password
            elif i == "Student Login Details": # checks if the name of the file is for the student login and stores the student login details in the file
                file = open(newPath, "w") # opens the student login file in write mode
                file.write("student") # username
                file.write(" ") # creates a space so the username and password can be differntiated
                file.write("Queenswood") # password





##### Class Logins #####


class TeacherLogins(): # a method that checks the username an password details for the teachers
    def __init__(self, path, usernameBox, passwordBox, label):
        self.__TLogin = open(path, "r") # opens the login file in read mode
        self.__userEntry = usernameBox # stores the entry box for the username
        self.__passEntry = passwordBox # stores the entry box for the password
        self.__label = label # stores the label that will show if the username or password is correct or incorrect
        self.login() # calls the login method

    def login(self):
        username = T_userN.get()
        password = T_passW.get()
        self.__userEntry.delete(0, tk.END)
        self.__passEntry.delete(0, tk.END)

        logins = self.__TLogin.readlines() # reads the contents of the file

        for line in logins: # loops through the contents of the file
            credentials = line.split() # splits the data in the file and stores it in a list


            # checks if the username is equal to the string stored in index postion 0 and if the password is equal to the string stored in index position 1
            if username == credentials[0]:
                if password == credentials[1]:
                    #outputs text in the screen showing that the credentials are correct
                    self.__label.config(text = "Successful login!", fg = "green")
                    OpenTeacherArea()#goes to the teacher area where they can create/edit the game
                else: 
                    # label showing the password is incorrect
                    self.__label.config(text = "The password is incorrect \n Please try again", fg = "red")

            else:
                # label showing the username is incorrect
                self.__label.config(text = "The username is incorrect \n Please try again", fg = "red")
    

class StudentLogins(): # a method that checks the username an password details for the students
    def __init__(self, path, usernameBox, passwordBox, label):
        self.SLogin = open(path, "r") # opens the login file in read mode
        self.__userEntry = usernameBox # stores the entry box for the username
        self.__passEntry = passwordBox # stores the entry box for the password
        self.__label = label # stores the label that will show if the username or password is correct or incorrect
        self.login() # calls the login method

    def login(self):
        username = S_userN.get()
        password = S_passW.get()
        self.__userEntry.delete(0, tk.END)
        self.__passEntry.delete(0, tk.END)
        logins = self.SLogin.readlines() # reads the contents of the file


        for line in logins: # loops through the contents of the file
            credentials = line.split() # splits the data in the file and stores it in a list

            # checks if the username is equal to the string stored in index postion 0 and if the password is equal to the string stored in index position 1
            if username == credentials[0]:
                if password == credentials[1]:
                    #outputs text in the screen showing that the credentials are correct
                    self.__label.config(text = "Successful login!", fg = "green")
                    OpenStudentArea()#goes to the teacher area where they can create/edit the game
                else: 
                    # label showing the password is incorrect
                    self.__label.config(text = "The password is incorrect \n Please try again", fg = "red")
                    
            else:
                # label showing the username is incorrect
                self.__label.config(text = "The username is incorrect \n Please try again", fg = "red")
         

##### Class Logins #####


class PlayGame():
    def __init__(self, i):
        self.__Teams = [] # a list to store the teams
        self.__Teams.append(Team("Clapham North")) # adds a team in the list of teams
        self.__Teams.append(Team("Clapham South")) # adds a team in the list of teams
        self.__Teams.append(Team("Hartley")) # adds a team in the list of teams
        self.__Teams.append(Team("Waller")) # adds a team in the list of teams
        self.__count = i # a counter to check what item in the list to access
        print("self.count: ", self.__count)
        self.CurrentTeam = self.__Teams[self.__count] # shows the current player
        print("Current Team: ", self.CurrentTeam.GetName())


    def DisplayTeam(self, label): 
        label.config(text = self.CurrentTeam.GetName()) # displays the current team


    def DisplayScore(self, label):
        label.config(text = self.CurrentTeam.GetScore()) # displays the score for the current team


    # shows the winner of the competition
    def DisplayPoints(self, label):
        print(self.__Teams[0].GetScore()) 
        print(self.__Teams[1].GetScore())
        print(self.__Teams[2].GetScore())
        print(self.__Teams[3].GetScore())
        # if all the teams have the same score it will result in a draw
        if self.__Teams[0].GetScore() == self.__Teams[1].GetScore() and self.__Teams[0].GetScore() == self.__Teams[2].GetScore() and self.__Teams[0].GetScore() == self.__Teams[3].GetScore():
            print("Draw")
            label.config(text = "Draw") # this will display on the screen that it is a draw

        # if the team in index position 0 has more points than the other teams they will win
        elif self.__Teams[0].GetScore() > self.__Teams[1].GetScore() and self.__Teams[0].GetScore() > self.__Teams[2].GetScore() and self.__Teams[0].GetScore() > self.__Teams[3].GetScore():
            print(self.__Teams[0].GetName(), "has won")
            label.config(text = self.__Teams[0].GetName()) # this will display on the screen the winning team

        # if the team in index position 1 has more points than the other teams they will win
        elif self.__Teams[1].GetScore() > self.__Teams[0].GetScore() and self.__Teams[1].GetScore() > self.__Teams[2].GetScore() and self.__Teams[1].GetScore() > self.__Teams[3].GetScore():
            print(self.__Teams[1].GetName(), "has won")
            label.config(text = self.__Teams[1].GetName()) # this will display on the screen the winning team

        # if the team in index position 2 has more points than the other teams they will win
        elif self.__Teams[2].GetScore() > self.__Teams[0].GetScore() and self.__Teams[2].GetScore() > self.__Teams[1].GetScore() and self.__Teams[2].GetScore() > self.__Teams[3].GetScore():
            print(self.__Teams[2].GetName(), "has won")
            label.config(text = self.__Teams[2].GetName()) # this will display on the screen the winning team

        # if the team in index position 3 has more points than the other teams they will win
        elif self.__Teams[3].GetScore() > self.__Teams[0].GetScore() and self.__Teams[3].GetScore() > self.__Teams[1].GetScore() and self.__Teams[3].GetScore() > self.__Teams[2].GetScore():
            print(self.__Teams[3].GetName(), "has won")
            label.config(text = self.__Teams[3].GetName()) # this will display on the screen the winning team



    # this method will add up the points entered by the user at the end for team North
    def NorthPoints(self, r1, r2, r3, r4):
        north = int(r1)+int(r2)+int(r3)+int(r4)
        self.__Teams[0].UpdateScore(north)


    # this method will add up the points entered by the user at the end for team South
    def SouthPoints(self, r1, r2, r3, r4):
        south = int(r1)+int(r2)+int(r3)+int(r4) 
        self.__Teams[1].UpdateScore(south)  


    # this method will add up the points entered by the user at the end for team Hartley
    def HartleyPoints(self, r1, r2, r3, r4):
        hartley = int(r1)+int(r2)+int(r3)+int(r4)    
        self.__Teams[2].UpdateScore(hartley)
    

    # this method will add up the points entered by the user at the end for team Waller
    def WallerPoints(self, r1, r2, r3, r4):
        waller = int(r1)+int(r2)+int(r3)+int(r4)    
        self.__Teams[3].UpdateScore(waller)
    


### TEAMS ###
class Team():
    def __init__(self, N):
        self.__TotalScore = 0 # a variable that stores the teams total score
        self.__HouseName = N # variable to store the house name

    def GetName(self): # gets the name of the team
        return self.__HouseName

    def GetScore(self): # a method to get the score for each house
        return self.__TotalScore

    def UpdateScore(self, points): # updates the score 
        self.__TotalScore += points
        print("Points: ", self.__TotalScore)



### BOGGLE CLASS ###


class Boggle():
    def __init__(self, PlayG):
        self._LettersInGrid = [] # list that stores the letters in the grid
        self._graph = {} # dictionary that stores the adjacency list 
        self._word = [] # stores the user's answer as a list
        self._visited = set() # stores the visited letters (nodes) in a set
        self._points = 0 # stores the points gained by the team
        self._game = PlayG # stores the instance a PlayGame class
        

    def CreateListOfRandomLetters(self, letters): # method that creates a list of random letters
        if len(self._LettersInGrid) >= 1: # checks if there are letters in the list
            self._LettersInGrid.clear() # clears the list
            self._visited.clear() # clears the set
            self._graph.clear() # clears the dictionary
            self._word.clear() # clears the list

            print("in other sub: ", self._LettersInGrid)
            print("Letters In Grid (in boggle class):", self._LettersInGrid)

        else: # shows that there are no letters in the list
            for i in letters: # loops through the random letters created 
                self._LettersInGrid.append(i) # adds the random letters to the list
            print("Letters In Grid (in boggle class):", self._LettersInGrid)
            self._CreateAdjacencyList() # calls the class to make the adjacency list


    def MakeWordToList(self, string, label, correct, incorrect): # method that makes the user's answer into a list
        if len(self._word)>=1: # checks if there are letters in the list
            self._word.clear() # clears the list
            self._visited.clear() # clears the set
            for i in string: # loops through the user's word 
                self._word.append(i) # adds each letter to the list self._word
            print("word to check: ", self._word)
            print("letters in grid: ", self._LettersInGrid)
            self._StartTraversal(label, correct, incorrect) # calls the method that will start to check whether the word can be found in the grid

        else: # shows that there are no letters in the list
            for i in string: # loops through the user's word 
                self._word.append(i)
            print("word to check: ", self._word)
            print("letters in grid: ", self._LettersInGrid)
            self._StartTraversal(label, correct, incorrect) # calls the method that will start to check whether the word can be found in the grid
        

    def _CreateAdjacencyList(self): # a method that creates the adjacency list from the grid
        print("in boggle class", self._LettersInGrid)

        # uses a dictionary to create an adjacency list that can be search through tp check whether words entered by the user are legal within the rules of the game
        self._graph = {
            self._LettersInGrid[0]: [self._LettersInGrid[1], self._LettersInGrid[5], self._LettersInGrid[4]], 
            
            self._LettersInGrid[1]: [self._LettersInGrid[0], self._LettersInGrid[4], self._LettersInGrid[5], self._LettersInGrid[6], self._LettersInGrid[2]],

            self._LettersInGrid[2]: [self._LettersInGrid[1], self._LettersInGrid[5], self._LettersInGrid[6], self._LettersInGrid[7], self._LettersInGrid[3]],

            self._LettersInGrid[3]: [self._LettersInGrid[2], self._LettersInGrid[6], self._LettersInGrid[7]],

            self._LettersInGrid[4]: [self._LettersInGrid[0], self._LettersInGrid[1], self._LettersInGrid[5], self._LettersInGrid[9], self._LettersInGrid[8]],

            self._LettersInGrid[5]: [self._LettersInGrid[0], self._LettersInGrid[1], self._LettersInGrid[2], self._LettersInGrid[6], self._LettersInGrid[10], self._LettersInGrid[9], self._LettersInGrid[8], self._LettersInGrid[4]],

            self._LettersInGrid[6]: [self._LettersInGrid[1], self._LettersInGrid[2], self._LettersInGrid[3], self._LettersInGrid[7], self._LettersInGrid[11], self._LettersInGrid[10], self._LettersInGrid[9], self._LettersInGrid[5]],

            self._LettersInGrid[7]: [self._LettersInGrid[3], self._LettersInGrid[2], self._LettersInGrid[6], self._LettersInGrid[10], self._LettersInGrid[11]],

            self._LettersInGrid[8]: [self._LettersInGrid[4], self._LettersInGrid[5], self._LettersInGrid[9], self._LettersInGrid[13], self._LettersInGrid[12]],

            self._LettersInGrid[9]: [self._LettersInGrid[4], self._LettersInGrid[5], self._LettersInGrid[6], self._LettersInGrid[10], self._LettersInGrid[14], self._LettersInGrid[13], self._LettersInGrid[12], self._LettersInGrid[8]],

            self._LettersInGrid[10]: [self._LettersInGrid[5], self._LettersInGrid[6], self._LettersInGrid[7], self._LettersInGrid[11], self._LettersInGrid[15], self._LettersInGrid[14], self._LettersInGrid[13], self._LettersInGrid[9]],

            self._LettersInGrid[11]: [self._LettersInGrid[7], self._LettersInGrid[6], self._LettersInGrid[10], self._LettersInGrid[14], self._LettersInGrid[15]],

            self._LettersInGrid[12]: [self._LettersInGrid[8], self._LettersInGrid[9], self._LettersInGrid[13]],

            self._LettersInGrid[13]: [self._LettersInGrid[12], self._LettersInGrid[8], self._LettersInGrid[9], self._LettersInGrid[10], self._LettersInGrid[14]],

            self._LettersInGrid[14]: [self._LettersInGrid[13], self._LettersInGrid[9], self._LettersInGrid[10], self._LettersInGrid[11], self._LettersInGrid[15]],

            self._LettersInGrid[15]: [self._LettersInGrid[11], self._LettersInGrid[10], self._LettersInGrid[14]]

        }

    
    def _StartTraversal(self, label, correct, incorrect): # a method that decides whether the traversal should be called
        a = 1 # sets a counter
        for i in range(len(self._word)-1): # loops through the length of the list self._word
            if i+1 == len(self._word): # checks if i+1 is equal the length of the list so that the traversal is not run
                print("stop") # will no run the search
            else: #while i+1 is not equal to the length of the list
                self._DFS(self._word[i], self._word[i+1], a, label, correct, incorrect) # calls the method to start the traversal


    def _DFS(self, node, next, count, label, correct, incorrect): # a method that performes a depth first search to check whether the user's input is legal within the rules of the game
        
        print("graph in new: ", self._graph)
        no = 0 # sets a counter
        nextNodes = [] # creates a list to store the neighbouring nodes
        if count != len(self._word)-1: # if the counter passed through is not equal to the length of the list self._word - 1

            if node not in self._visited: # checks is the node (argument) has been visited
                if node != self._word[len(self._word)-1]: # checks that the node is not equal to the penultimate letter of the word
                    print("node: ", node)
                    self._visited.add(node) # adds the node to the set


                    for neighbour in self._graph[node]: # loops through the nodes neighbours from the adjacency list
                        print("neighbour: ", neighbour)
                        nextNodes.append(neighbour) # adds the neighbours into the list nextNodes
                    print("list of next nodes: ", nextNodes)


                    for i in self._visited: # loops through the set of visited nodes
                        print("node to remove: ", i) 
                        if i in nextNodes: # loops through the list of neighbours
                            nextNodes.remove(i) # removes the visited node from the list of neighbours so that it cannot be visited again
                    print("new list of next nodes: ", nextNodes)


                    for newNode in nextNodes: # loops through the list of neighbouring nodes
                        print("count: ", count)
                        print("\nlist of possible nodes (checks if same): ", next)
                        print("new node (what is being checked): ", newNode)

                        if next == newNode: # if the next node is equal to an item in the neighbouring nodes list 
                            no +=1 # counter increments by 1
                            print("same")
                            print("next: ", next)
                            print("newNode: ", newNode)
                            count +=1 # another counter increments by 1
                            
                            print("count: ", count)
                            print(self._word[count])
                            
                            self._DFS(next, self._word[count], count, label, correct, incorrect) # recursively calls the subroutine again where the next (node) is the new 'start' node
                            break

                        else: # the next node is not equal to a neighbour of the start node 
                            print("not correct")
                            no +=1 # counter increments by 1
                            print("number: ", no)
                        
                    else:
                        print("word not legal")
                        self._CheckIfRealWord(False, label, correct, incorrect) # calls the method to check if it is a real word
                        self._word.clear()
                        
                                
                else: # node is equal to the penultimate letter so the word is legal and must be checked to see if it is a real word
                    print("must be legal")
                    self._CheckIfRealWord(True, label, correct, incorrect) # calls the method to check if it is a real word
                    
        else: # the entire word has been searched 
            self._ShowVisited(label, correct, incorrect) # calls the method to check if the visited nodes correspond to the word being searched
                
        
    def _ShowVisited(self, label, correct, incorrect): # a method to check if the visited nodes correspond to the word being searched
        print("visited:", self._visited)
        if len(self._visited) == len(self._word)-1: # if true shows that the word has been fully searched
            print("final visited: ", self._visited)
            print("word: ", self._word)
            legal = True
            self._CheckIfRealWord(legal, label, correct, incorrect) # checks to see if the word is real
        else: # word has not been fully searched
            print("not finished")


    def _CheckIfRealWord(self, legal, label, correct, incorrect):
        true = 0 # counter to check if the word is real or not
        checkWord = "".join(self._word) # joins the list together to make it back into string
        if legal == True:
            if checkWord == spell.correction(checkWord): # checks if the word matches in the database of words
                true +=1 # counter showing the word is real
                print("True")
                
                self._CalculatePoints(true, label, correct, incorrect) # calls a method to calculate the points based on the length of the word

            else:
                true -=1 # counter showing the word is not real
                print("false")
                
                self._CalculatePoints(true, label, correct, incorrect) # calls a method to calculate the points based on the length of the word
        else:
            true -=1 # counter showing the word is not real
            print("false")
            #IncorrectMessage(incorrect)
            self._CalculatePoints(true, label, correct, incorrect) # calls a method to calculate the points based on the length of the word


    def _CalculatePoints(self, true, label, correct, incorrect):
        # If the word is 3-4 letters long, one point is awarded
        # If the word is 5 letters long, two points will be awarded
        # If the word is 6 letters long, three points will be awarded
        # If the word is 7 letters long, five points will be awarded
        # If the word is 8 or more letters long, eleven points will be awarded
        

        if true >=1: # shows that the word is real so will gain points
            if len(self._word) == 3 or len(self._word) == 4: # check the length of the word is either 3 or 4 letters long
                self._points +=1 # points increase by 1
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen
                

            elif len(self._word) == 5: # check the length of the word is 5 letters long
                self._points +=2 # points increase by 2
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen

            elif len(self._word) == 6: # check the length of the word is 6 letters long
                self._points +=3 # points increase by 3
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen

            elif len(self._word) == 7: # check the length of the word is  letters long
                self._points +=4 # points increase by 4
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen

            elif len(self._word) >= 8: # check the length of the word is 8 or more letters long
                self._points +=11 # points increase by 11
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen
            else:
                self._points = 0 # no points are given
                IncorrectMessage(incorrect)
                self._game.CurrentTeam.UpdateScore(self._points) # updates the score for the current player
                print(self._game.CurrentTeam.GetScore()) # prints the current score
                self._game.DisplayScore(label) # displays the score on the screen
            
            if self._points >= 1:
                CorrectMessage(correct)
            else:
                IncorrectMessage(incorrect)
        
        else:
            print("no points as word is not legal")
            IncorrectMessage(incorrect) # calls a subroutine to show that the answer is wrong
        

### SPELLING BEE CLASS ###
class CreateSpellBeeWords():

    def CreateWords(self, p, year): #method used to create the words and add them into the file specified the arguments
        file = open(p, "w") #opens the file passed in through the parameters in write mode
        file.write("%s\n" % spellingWords) #adds the user input into the file
        file = open(p, "r") #opens the file in read mode
        display = file.read() #stores the data read in the file as a variable called display 
        Words = display.split("\n") #splits the data read from the file so that it appears on one line for each word
        
        #while loop to remove empty string stored in the list
        while '' in Words:
            Words.remove('')  # removes the empty string from the list
        print(Words)
        file.close # closes the file

        # if the user enters the words for the year 10 no matter the subject it will lead back to the screen where you can enter new words
        if file == "Year 10+ Maths Words":
            OpenEnterNewWords(year)
        elif file == "Year 10+ English Words":
            OpenEnterNewWords(year)
        elif file == "Year 10+ Science Words":
            OpenEnterNewWords(year)



class DisplayWords():

    # a method that gets the word from the drop down list selecetd by the user to output the correct words for the user to guess
  
    def WordFromDropDown(self, yearGroup, subject, year): 
        OriginalPath = os.path.join('/Users/adeituraandu/Desktop/spelling bee files', year) # the path needed to access the files

        if yearGroup == "Year 7": # checks if the year group is year 7
            if subject == "Maths": # checks if the subject is maths
                path = os.path.join(OriginalPath, "Year 7 Maths Words") # creates path to open the file for the year 7 maths words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            elif subject == "English": # checks if the subject is english
                path = os.path.join(OriginalPath, "Year 7 English Words") # creates path to open the file for the year 7 english words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            elif subject == "Science": # checks if the subject is science
                path = os.path.join(OriginalPath, "Year 7 Science Words") # creates path to open the file for the year 7 science words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            else:
                print("wrong")

        elif yearGroup== "Year 8": # checks if the year group is year 8
            if subject == "Maths": # checks if the subject is maths
                path = os.path.join(OriginalPath, "Year 8 Maths Words") # creates path to open the file for the year 8 maths words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            elif subject == "English": # checks if the subject is english
                path = os.path.join(OriginalPath, "Year 8 English Words") # creates path to open the file for the year 8 english words
                self._GetWords(path, year) # calls the method to access the words for the specified file path
            elif subject == "Science": # checks if the subject is science

                path = os.path.join(OriginalPath, "Year 8 Science Words") # creates path to open the file for the year 8 science words
                self._GetWords(path, year) # calls the method to access the words for the specified file path
            else:
                print("wrong")

        elif yearGroup == "Year 9": # checks if the year group is year 9
            if subject == "Maths": # checks if the subject is maths
                path = os.path.join(OriginalPath, "Year 9 Maths Words") # creates path to open the file for the year 9 maths words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            elif subject == "English": # checks if the subject is english
                path = os.path.join(OriginalPath, "Year 9 English Words") # creates path to open the file for the year 9 english words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            elif subject == "Science": # checks if the subject is science
                path = os.path.join(OriginalPath, "Year 9 Science Words") # creates path to open the file for the year 9 science words
                self._GetWords(path, year) # calls the method to access the words for the specified file path

            else:
                print("wrong")

        elif yearGroup == "Year 10+": # checks if the year group is year 10+
            if subject == "Maths": # checks if the subject is maths
                path = os.path.join(OriginalPath, "Year 10+ Maths Words") # creates path to open the file for the year 10+ maths words
                self._GetWords(path, year)
            elif subject == "English": # checks if the subject is english
                path = os.path.join(OriginalPath, "Year 10+ English Words") # creates path to open the file for the year 10+ english words
                self._GetWords(path, year)
            elif subject == "Science": # checks if the subject is science
                path = os.path.join(OriginalPath, "Year 10+ Science Words") # creates path to open the file for the year 10+ science words
                self._GetWords(path, year)
            else:
                print("wrong")

        else:
            print("this is not a valid option!")
    

    def _GetWords(self, f, year): # a method used to access the words from the file passed into the parameters and outputs them to the team so that the word can be spelt
        global word_list
        file = open(f, "r") #open file in read mode
        display = file.read() #store items in file in list
        word_list = display.split("\n") #seprates each line with a space

        #while loop to remove empty string stored in the list
        while '' in word_list: 
            word_list.remove('') # removes the empty string from the list
        
        self.getWordsList(word_list, year) # calls the method to get the list of words to check
        

    def getWordsList(self, word_list, year): # a method that gets the word to be read out by the system
        if len(word_list) >=1: # checks that there are words in the list
            print(word_list) 
            print(word_list[-1])

            filetype = 'mp3' # stores the form the files must be saved as 
            mergefile = [word_list[-1], filetype] # stores how to file should be saved as a a list
            
            store = '.'.join(mergefile) # merges the list
            path = '/Users/adeituraandu/Desktop/spelling bee files' # the path file to save the files to 
            new = os.path.join(path, year, store) # creates a new path file with the selected year and the file to be stored
 
            playWord = gTTS(text=word_list[-1], lang='en', slow=False) # sets the voice and text for the system to say
            playWord.save(new) # saves the audio file
            playsound(new) # opens the audio file

        else:

            print("no more words to spell") # shows that there are no more words to spell

    
    def PlayAgain(self, year): # same as getWordsList method an allows the audio to be played again
        filetype = 'mp3'
        mergefile = [word_list[-1], filetype]
        
        store = '.'.join(mergefile)
        path = '/Users/adeituraandu/Desktop/spelling bee files'
        new = os.path.join(path, year, store)

        playWord = gTTS(text=word_list[-1], lang='en', slow=False)
        playWord.save(new)
        playsound(new)


# class that checks the players answer for the spelling bee section
class SpellBeeAnswer():

    def checkAnswer(self, PlayG, answer, entryBox, year, label): # checks if the users answer is correct or not
        d = DisplayWords() # calls the DisplayWords class
        print(answer)
        print(word_list[-1])
        if answer == word_list[-1]: # checks if the users answer is equal to the word presented 
            correct = tk.Label(SpellBeeWindow, text = "CORRECT!!", bg = "light grey", fg = "green", font = ("Lao Sangam MN", 40)) # displays a correct message
            # the position of the label
            correct.place(x=650, y=200)

            # displays the correct spelling of the word
            word = tk.Label(SpellBeeWindow, text = word_list[-1], bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30)) 
            # the position of the label
            word.place(x=670, y=300)

            newList = word_list.pop() # removes the last item in the list

            point = 1 # the points added everytime a word is spelt correctly

            PlayG.CurrentTeam.UpdateScore(point) # updates the score for the player
            
            if len(word_list) == 0: # checks if the list is empty
                PlayG.DisplayTeam() # shows the team
                PlayG.CurrentTeam.GetScore() # gets the score
                PlayG.DisplayScore(label) # displays the score for the label
            
            
            clear(entryBox) # clears the entry box
            d.getWordsList(word_list, year) # calls the method to say the next word

                
        else:
            incorrect = tk.Label(SpellBeeWindow, text = "INCORRECT!!", bg = "light grey", fg = "red", font = ("Lao Sangam MN", 60)) # displays an incorrect message
            # the position of the label
            incorrect.place(x=580, y=200)

            # displays the correct spelling of the word
            word = tk.Label(SpellBeeWindow, text = word_list[-1], bg = "light grey", fg = "black", font = ("Lao Sangam MN", 50)) 
            # the position of the label
            word.place(x=640, y=300)
            PlayG.DisplayTeam() # shows the team
            PlayG.CurrentTeam.GetScore() # gets the score
            PlayG.DisplayScore(label) # displays the score for the label
            

### SPELLING BEE CLASS ###

    
### Anagram Class ###
class CreateAnagrams():
    def __init__(self):
        self.__front = 0 # sets the front counter to 0
        self.__size = 0 # sets the size counter to 0
        self.__queue = [] # creates a queue to store the word
        self.__InitialListOfWords = [] # stores the string created when shuffling the letters in the inital word 
        self.__ListOfWordsToShuffle = [] # stores that string to be shuffled through
        self.__FinalAnagram = [] # stores the final anagrams



    def AddLettersIntoQueue(self, data): # adds the letters of the word to a queue
        for i in data: # loops through the word passed in the arguments
            self.__queue.append(i) # adds the value of i to self.__queue
        self.__size = len(self.__queue) # sets self.__size to the length of the queue
    
        if len(self.__queue) <= 2: # checks if the length of the queue is less than or equal to 2
            print("cant generate an anagram") # cannot be used to find an anagram
        else:
            self._CreateInitialWordsToLoop() # calls the method that will 
    
    # a method that moves the first letter in the queue (self.__queue) to the end of the queue for all of the letters in the queue 
    # (e.g. self.__queue = ['w', 'o', 'r', 'd']
    # ['o', 'r', 'd', 'w'])

    def _CreateInitialWordsToLoop(self): 
        for i in range(len(self.__queue)): # loops through the length of the list queue

            # uses string slicing to get the first letter and add it to the end of the string and stores it in a variable
            FirstSetOfWords = self.__queue[i:]+self.__queue[:i] 

            self.__InitialListOfWords.append(FirstSetOfWords) # adds the newly formed string to the list InitialListOfWords



        for i in range(len(self.__InitialListOfWords)): # loops through the length of the list queue

            # sets the first item in the list InitialListOfWords to a variable called checking (this will be used later on to check if the word has been fully searched)
            checking =  self.__InitialListOfWords[i] 

            self._CreateWordsToShuffle(checking) # calls the method CreateWordsToShuffle and passes in the word to be shuffled
        
     
        self._DisplayWordsToShuffle() # calls the method to show the full list of InitialListOfWords

    # a method that will shuffle the string stored in InitialListOfWords (where each item in the list will be passed through the parameters)
    # each string stored in the list will be shuffled (all the letters but the first will be shuffled and stored in another list)
    def _CreateWordsToShuffle(self, wordToShuffle): 

        for i in range(len(wordToShuffle)-1): # loops through the length of the argument - 1
                
            x = wordToShuffle[1] # stores the first letter in the string as a variable x
            y = wordToShuffle[i+1] # stores letter in index i+1 as a variable y

            x, y = y, x # uses a tuple to swap the letters stored in x and y


            wordToShuffle[1] = x # stores the value in index position 1 of wordToShuffle as the new value of x
            wordToShuffle[i+1] = y # stores the value in index position i+1 of wordToShuffle as the new value of x
            
            
            print("word to shuffle: ", wordToShuffle)
            print("final x: ", x)
            print("final y: ", y)

            print("value of x: ", len(wordToShuffle[1]))
            print("value of y: ", len(wordToShuffle[i+1]))

            FinalWordtoShuffle = list(wordToShuffle) # stores the new string wordToShuffle as a list in the variable FinalWordToShuffle

            self.__ListOfWordsToShuffle.append(FinalWordtoShuffle) # adds FinalWordToShuffle to the list ListOfWordsToShuffle

    # a method that displays the words to be shuffled
    def _DisplayWordsToShuffle(self):
        for i in range(len(self.__ListOfWordsToShuffle)): # loops through the list ListOfWordsToShuffle

            # stores the word that is to be shuffled as the item in the list ListOfWordsToShuffle based on the value of i
            wordToLoop =  self.__ListOfWordsToShuffle[i]

            # stores the word that is to be kept to check against as the item in the list ListOfWordsToShuffle based on the value of i
            wordToKeep = self.__ListOfWordsToShuffle[i]
    
            # calls the method that will remove a certain number of letters to ensure that three letters are remaining in the string
            self._RemoveFirstLetters(wordToLoop, wordToKeep) 


        # a method that will remove a certain number of letters to ensure that three letters are remaining in the string
    def _RemoveFirstLetters(self, word, wordToCheck):
        InitialLetters = [] # a list to store the first few letters that will be removed
        
        for i in range(len(word)-3): # loops through the length of the word to be shuffled - 3
            InitialLetters.append(word[i]) # adds the letter to the list

        self._RemainingLetters(InitialLetters, word, wordToCheck) # calls a method to store the remaining three letters left 


    # a method to store the remaining three letters left 
    def _RemainingLetters(self, InitialLetters, word, wordToCheck):
        ListOfRemainingLetters = [] # a list to store the last three letters
        for i in range(self.__size-len(InitialLetters)): # loops for the size of the word - the length of the list InitialLetters
            value = word[i+len(InitialLetters)] # stores the letter in index i + length of the InitialLetters as a variable value
            ListOfRemainingLetters.append(value) # adds value to the list of remaining letters

        # calls the method that will form the anagrams
        self._swapR(ListOfRemainingLetters, (self.__front), (self.__front+1), wordToCheck, InitialLetters) 

    # a method that will shuffle through the ListOfRemainingLetters and add them to the list of InitialLetters and will do this for every word in the list of 
    # ListOfWordsToShuffle
    def _swapR(self, queue, calcX, calcY, wordToCheck, InitialLetters):
        
        for i in range(len(queue)): # loops through the length of the list queue
            print("i = ", i) # 
            print("old word: ", wordToCheck)
            print("new queue: ", queue)

            if i == len(queue)-1: # checks if i is equal to the length of the list - 1

                if queue == wordToCheck[len(InitialLetters):]: # checks if the list is equal to the last three letters in the wordToCheck variable
                    print("word to check[2:] ", wordToCheck[len(InitialLetters):])
                    print("checking word: ", queue)
                    print("confirming word: ", wordToCheck)
                    print("done")
                    self.__FinalAnagram = list(dict.fromkeys(self.__FinalAnagram)) # removes any repeats from the list of FinalAnagrams
                    print("list of anagrams: ", self.__FinalAnagram)
                    print("length of list: ", len(self.__FinalAnagram))
                    self.__front = 0 # sets the front value to 0
                    self.__size = len(self.__queue) # sets the size to the length of the original word

                else:

                    print("start recursive call")
                    self._swapR(queue, (self.__front), (self.__front+1), wordToCheck, InitialLetters) # recursively calls itself increasing the front pointer by 1 

            else:

                print("calcX: ", calcX)
                print("calcY: ", calcY)
                
                x = queue[calcX] # sets the variable x to value of the list queue index position calcX
                y = queue[calcY] # sets the variable y to value of the list queue index position calcY

                print("first x: ", x)
                print("first y: ", y)
                x, y = y, x # uses a tuple to swap the letters stored in x and y


                queue[calcX] = x # stores the value in index position 1 of wordToShuffle as the new value of x
                queue[calcY] = y # stores the value in index position i+1 of wordToShuffle as the new value of x
                

                print(queue)
                print("final x: ", x)
                print("final y: ", y)

                calcX += 1 # increases the variable value by 1
                calcY += 1 # increases the variable value by 1
                
                firstLetter = "".join(InitialLetters) # a variable to store the list of the first few letters joined together to become string
                restOfLetters = "".join(queue) # a variable to store the list of the last three letters joined together to become string
                print("first letter: ", firstLetter)
                anagram = (firstLetter + restOfLetters) # merges the full word together and stores it as the variable anagram
                
                print(anagram)
        
                print(queue)
                self.__FinalAnagram.append(anagram) # adds the variable anagram to the list of final anagrams
        
        AddToTextBox(self.__FinalAnagram, len(self.__FinalAnagram)) # calls the subroutine that will add the anagram to the text area
        


class CheckAnagram():
    def __init__(self, year):
        self._AnagramWordList = [] # sets a list to store the anagram words
        self.ListOfOriginalWords = [] # sets a list to store the word entered by the user
        self.access = AccessFiles() # calls the AccessFiles class
        self.originalFile = os.path.join(self.access.path, year, "Original Anagram File") # stores a new file path for the words entered by the user
        self.anagramFile = os.path.join(self.access.path, year, "Anagram File") # stores a new file path for the anagram words
        os.chdir('/Users/adeituraandu/Desktop/spelling bee files/'+ year) # changes the file directory


    # method that adds the original words entered by the user to a list
    def AddToList(self):
        print("og file: ", self.originalFile)
        for line in open(self.originalFile).readlines(): # opens the Original Anagram File in read mode using the readlines option
            self.ListOfOriginalWords.append(line.strip()) # adds each line in the file to the list
        print(self.ListOfOriginalWords) # prints the list


    # a method that adds the anagrams to a text box for the student user to guess to choose
    def AddTextToBox(self, textArea_A):
        for line in open(self.anagramFile).readlines(): # opens the Anagram File in read mode using the readlines option
            self._AnagramWordList.append(line.strip()) # adds each line in the file to the list

        textArea_A.insert(tk.END, self._AnagramWordList[0]) # adds the first item on the list to the text box
        textArea_A.insert(tk.END, "\n") # creates a new line in the text area
        print(self._AnagramWordList[0]) # prints the anagram to the console


    # method that checks the users answer for the anagram
    def CheckAnagramAns(self, PlayG, answer, answerBox, year, textArea_A):
        if answer == self.ListOfOriginalWords[0]: # checks if the teams users answer is equal to the original word entered by the teacher user
            point = 2 # stores the amount of points gained if correct
            PlayG.CurrentTeam.UpdateScore(point) # updates the teams score
            PlayG.CurrentTeam.GetScore() # gets the teams current score

            # label shows that the answer is correct
            correctLabel = tk.Label(AnagramWindow, text = "CORRECT", bg = "light grey", fg = "green", font = ("Lao Sangam MN", 50))
            # postion of the label
            correctLabel.place(x=900, y=300)
            with open(self.anagramFile, "r+") as file: # opens the Anagram File in read and write mode
                lines = file.readlines() # reads the file in readlines mode
                file.seek(0) # moves file pointer to the beginning of the file
                file.truncate() # resizes the file to the current file stream position
                for number, line in enumerate(lines): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file.write(line) # rewrites contents of file without line 0

            with open(self.originalFile, "r+") as file2: # opens the Anagram File in read and write mode
                lines2 = file2.readlines() # reads the file in readlines mode
                file2.seek(0) # moves file pointer to the beginning of the file
                file2.truncate() # resizes the file to the current file stream position
                for number, line1 in enumerate(lines2): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file2.write(line1) # rewrites contents of file without line 0
            
            self.ListOfOriginalWords.pop(0) # removes the first item in the list
            print(self.ListOfOriginalWords)
            answerBox.delete(0, tk.END) # clears the entry box
            textArea_A.delete(1.0, tk.END) # clears the text area
            #OpenBoggleWindow(year)

        else:
            PlayG.CurrentTeam.GetScore() # displays the players score

            # label showing the users answer is incorrect
            incorrectLabel = tk.Label(AnagramWindow, text = "INCORRECT", bg = "light grey", fg = "red", font = ("Lao Sangam MN", 50))
            
            # position of label
            incorrectLabel.place(x=900, y=300)
            
            with open(self.anagramFile, "r+") as file: # opens the Anagram File in read and write mode
                lines = file.readlines() # reads the file in readlines mode
                file.seek(0) # moves file pointer to the beginning of the file
                file.truncate() # resizes the file to the current file stream position
                for number, line in enumerate(lines): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file.write(line) # rewrites contents of file without line 0

            with open(self.originalFile, "r+") as file2: # opens the Anagram File in read and write mode
                lines2 = file2.readlines() # reads the file in readlines mode
                file2.seek(0) # moves file pointer to the beginning of the file
                file2.truncate() # resizes the file to the current file stream position
                for number, line1 in enumerate(lines2): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file2.write(line1) # rewrites contents of file without line 0
            
            self.ListOfOriginalWords.pop(0) # removes the first item in the list
            answerBox.delete(0, tk.END) # clears the entry box
            textArea_A.delete(1.0, tk.END) # clears the text area
            self._AnagramWordList.pop(0) # removes the first word in the list 


# a class that inherits from the Boggle, DisplayWords, SpellBeeAnswer and CheckAnagram classes to allow the user to practice the game
class PracticeGames(Boggle, DisplayWords, SpellBeeAnswer, CheckAnagram):
    def __init__(self, PlayG):
        super().__init__(PlayG) # inherits all of the class methods and attributes
        self._AnagramWordList = [] # sets a list to store the anagram words
        self.ListOfOriginalWords = [] # sets a list to store the word entered by the user
        self.access = AccessFiles() # calls the AccessFiles class

        # overrides the originalFile variable and creates a new path file without specifing the year (as this can be plaued at any time)
        self.originalFile = os.path.join(self.access.path, "Practice Original Anagram Words") 
        
        # overrides the anagramFile variable and creates a new path file without specifing the year (as this can be plaued at any time)
        self.anagramFile = os.path.join(self.access.path, "Practice Anagram Words")
    
    # same code as the Boggle class however the label argument has been removed as it is not necessary in this section
    def _MakeWordToList(self, string, correct, incorrect):
        if len(self._word)>=1: # checks if there are letters in the list
            self._word.clear() # clears the list
            self._visited.clear() # clears the set
            for i in string: # loops through the user's word 
                self._word.append(i) # adds each letter to the list self._word
    
            self._StartTraversal(correct, incorrect) # calls the method that will start to check whether the word can be found in the grid

        else: # shows that there are no letters in the list
            for i in string: # loops through the user's word 
                self._word.append(i)
            self._StartTraversal(correct, incorrect) # calls the method that will start to check whether the word can be found in the grid
        
        
    def _StartTraversal(self, correct, incorrect):
        a = 1 # sets a counter
        for i in range(len(self._word)-1): # loops through the length of the list self._word
            if i+1 == len(self._word): # checks if i+1 is equal the length of the list so that the traversal is not run
                print("stop") # will no run the search
            else: #while i+1 is not equal to the length of the list
                self._DFS(self._word[i], self._word[i+1], a, correct, incorrect) # calls the method to start the traversal
        

    def _DFS(self, node, next, count, correct, incorrect):
        no = 0 # sets a counter
        nextNodes = [] # creates a list to store the neighbouring nodes
        if count != len(self._word)-1: # if the counter passed through is not equal to the length of the list self._word - 1

            if node not in self._visited: # checks is the node (argument) has been visited
                if node != self._word[len(self._word)-1]: # checks that the node is not equal to the penultimate letter of the word
                    print("node: ", node)
                    self._visited.add(node) # adds the node to the set


                    for neighbour in self._graph[node]: # loops through the nodes neighbours from the adjacency list
                        print("neighbour: ", neighbour)
                        nextNodes.append(neighbour) # adds the neighbours into the list nextNodes
                    print("list of next nodes: ", nextNodes)


                    for i in self._visited: # loops through the set of visited nodes
                        print("node to remove: ", i) 
                        if i in nextNodes: # loops through the list of neighbours
                            nextNodes.remove(i) # removes the visited node from the list of neighbours so that it cannot be visited again
                    print("new list of next nodes: ", nextNodes)


                    for newNode in nextNodes: # loops through the list of neighbouring nodes
                        print("count: ", count)
                        print("\nlist of possible nodes (checks if same): ", next)
                        print("new node (what is being checked): ", newNode)

                        if next == newNode: # if the next node is equal to an item in the neighbouring nodes list 
                            no +=1 # counter increments by 1
                            print("same")
                            print("next: ", next)
                            print("newNode: ", newNode)
                            count +=1 # another counter increments by 1
                            
                            print("count: ", count)
                            print(self._word[count])
                            
                            self._DFS(next, self._word[count], count, correct, incorrect) # recursively calls the subroutine again where the next (node) is the new 'start' node
                            break

                        else: # the next node is not equal to a neighbour of the start node 
                            print("not correct")
                            no +=1 # counter increments by 1
                            print("number: ", no)
                        
                    else:
                        print("word not legal")
                        self._CheckIfRealWord(False, correct, incorrect) # calls the method to check if it is a real word
                        self._word.clear()
                        
                                
                else: # node is equal to the penultimate letter so the word is legal and must be checked to see if it is a real word
                    print("must be legal")
                    self._CheckIfRealWord(True, correct, incorrect) # calls the method to check if it is a real word
                    
        else: # the entire word has been searched 
            self._ShowVisited(correct, incorrect) # calls the method to check if the visited nodes correspond to the word being searched
                
        
    def _ShowVisited(self, correct, incorrect):
        if len(self._visited) == len(self._word)-1: # if true shows that the word has been fully searched
            legal = True
            self._CheckIfRealWord(legal, correct, incorrect) # checks to see if the word is real
        else: # word has not been fully searched
            print("not finished")
        
        
    def _CheckIfRealWord(self, legal, correct, incorrect):
        true = 0 # counter to check if the word is real or not
        checkWord = "".join(self._word) # joins the list together to make it back into string
        if legal == True:
            if checkWord == spell.correction(checkWord): # checks if the word matches in the database of words
                true +=1 # counter showing the word is real
                print("True")
                CorrectMessage(correct) # calls a subroutine to show that the answer is correct

            else:
                true -=1 # counter showing the word is not real
                print("false")
                
                IncorrectMessage(incorrect) # calls a subroutine to show that the answer is correct
        else:
            true -=1 # counter showing the word is not real
            print("false")
            #IncorrectMessage(incorrect)
            
            IncorrectMessage(incorrect) # calls a subroutine to show that the answer is correct

  
    def WordFromDropDown(self): # a method that gets the file name with the words to be spelt
        
        OriginalPath = '/Users/adeituraandu/Desktop/spelling bee files' # the path needed to access the files
        path = os.path.join(OriginalPath, "Practice Words") # the new path needed to save the file to 
        self._GetWords(path) # calls the _GetWords method
    

    def _GetWords(self, f): # a method used to access the words from the file passed into the parameters and outputs them to the team so that the word can be spelt
        global word_list
        file = open(f, "r") #open file in read mode
        display = file.read() #store items in file in list
        word_list = display.split("\n") #seprates each line with a space

        #while loop to remove empty string stored in the list
        while '' in word_list: 
            word_list.remove('') # removes the empty string from the list
        
        self.getWordsList(word_list) # calls the method to get the list of words to check
        

    def getWordsList(self, word_list): # a method that gets the word to be read out by the system
        if len(word_list) >=1: # checks that there are words in the list
            print(word_list) 
            print(word_list[-1])

            filetype = 'mp3' # stores the form the files must be saved as 
            mergefile = [word_list[-1], filetype] # stores how to file should be saved as a a list
            
            store = '.'.join(mergefile) # merges the list
            path = '/Users/adeituraandu/Desktop/spelling bee files' # the path file to save the files to 
            new = os.path.join(path, store) # creates a new path file with the selected file to be stored
 
            playWord = gTTS(text=word_list[-1], lang='en', slow=False) # sets the voice and text for the system to say
            playWord.save(new) # saves the audio file
            playsound(new) # opens the audio file

        else:

            print("no more words to spell") # shows that there are no more words to spell


    def checkAnswer(self, answer, entryBox, correct, incorrect, win): # pass in list of words
        ClearAnswerSB_AG(correct, incorrect) # calls a subroutine that will clear the correct or incorrect answer label

        # a label showing the correct spelling of the word
        word = tk.Label(win, text = word_list[-1], bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30)) 
        # position of the label
        word.place(x=680, y=250)

        if answer == word_list[-1]: # checks if the users answer is equal to the word to spell
            CorrectMessage(correct) # calls a subroutine that will show that the spelling is correct
            newList = word_list.pop() # removes the word from the list

            clear(entryBox) # clears the entry box
            
            self.getWordsList(word_list) # calls the method that will get the next word

                
        else:

            IncorrectMessage(incorrect) # calls a subroutine that will show that the spelling is correct

            # a label showing the correct spelling of the word
            word = tk.Label(win, text = word_list[-1], bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30))
            # position of the label
            word.place(x=680, y=250)
            clear(entryBox) # clears the entry box
            self.getWordsList(word_list) # calls the method that will get the next word


    def AddToList(self):
        print("og file: ", self.originalFile)
        for line in open(self.originalFile).readlines(): # opens the Original Anagram File in read mode using the readlines option
            self.ListOfOriginalWords.append(line.strip()) # adds each line in the file to the list
        print(self.ListOfOriginalWords) # prints the list


    def AddTextToBox(self, textArea):
        for line in open(self.anagramFile).readlines(): # opens the Anagram File in read mode using the readlines option
            self._AnagramWordList.append(line.strip()) # adds each line in the file to the list

        textArea.insert(tk.END, self._AnagramWordList[0]) # adds the first item on the list to the text box
        textArea.insert(tk.END, "\n") # creates a new line in the text area
        print(self._AnagramWordList[0]) # prints the anagram to the console


    def CheckAnagramAns(self, answer, textArea, answerBox, correct, incorrect):
        if answer == self.ListOfOriginalWords[0]: # checks if the teams users answer is equal to the original word entered by the teacher user
            CorrectMessage(correct)
            with open(self.anagramFile, "r+") as file: # opens the Anagram File in read and write mode
                lines = file.readlines() # reads the file in readlines mode
                file.seek(0) # moves file pointer to the beginning of the file
                file.truncate() # resizes the file to the current file stream position
                for number, line in enumerate(lines): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file.write(line) # rewrites contents of file without line 0

            with open(self.originalFile, "r+") as file2: # opens the Anagram File in read and write mode
                lines2 = file2.readlines() # reads the file in readlines mode
                file2.seek(0) # moves file pointer to the beginning of the file
                file2.truncate() # resizes the file to the current file stream position
                for number, line1 in enumerate(lines2): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file2.write(line1) # rewrites contents of file without line 0
            
            self.ListOfOriginalWords.pop(0) # removes the first item in the list
            print(self.ListOfOriginalWords)
            answerBox.delete(0, tk.END) # clears the entry box
            textArea.delete(1.0, tk.END) # clears the text area
            self._AnagramWordList.pop(0) # removes the first word in the list 



        else:
            IncorrectMessage(incorrect)
            with open(self.anagramFile, "r+") as file: # opens the Anagram File in read and write mode
                lines = file.readlines() # reads the file in readlines mode
                file.seek(0) # moves file pointer to the beginning of the file
                file.truncate() # resizes the file to the current file stream position
                for number, line in enumerate(lines): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file.write(line) # rewrites contents of file without line 0

            with open(self.originalFile, "r+") as file2: # opens the Anagram File in read and write mode
                lines2 = file2.readlines() # reads the file in readlines mode
                file2.seek(0) # moves file pointer to the beginning of the file
                file2.truncate() # resizes the file to the current file stream position
                for number, line1 in enumerate(lines2): # loops through each line
                    if number not in [0, 0]: # deletes the contents of the file on line 0 
                        file2.write(line1) # rewrites contents of file without line 0
            
            self.ListOfOriginalWords.pop(0) # removes the first item in the list
            answerBox.delete(0, tk.END) # clears the entry box
            textArea.delete(1.0, tk.END) # clears the text area
            self._AnagramWordList.pop(0) # removes the first word in the list 

            

            

        




##### STUDENT SECTION #####

def OpenStudentLogin():
    global StudentLogin # makes the student login window global
    global S_userN # makes the username global so that it can be checked again if the user gets the details wrong
    global S_passW # makes the password global so that it can be checked again if the user gets the details wrong
    #global usernameEntry
    #global passwordEntry
    StudentLogin = tk.Toplevel(window1) # creates the child window
    StudentLogin.title("Student Login") # creates the title of the window
    StudentLogin.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    StudentLogin.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    access = AccessFiles()
    studentPath = os.path.join(access.path, "Student Login Details")
    #student = StudentLogins(studentPath) #creates an instance of the login class

    S_userN = tk.StringVar() # makes a variable to store the username entered by the user
    S_passW = tk.StringVar() # makes a variable to store the password entered by the user

    loginLabel = tk.Label(StudentLogin, text = "", bg = "light grey", font = ("Lao Sangam MN", 15))

    #title label
    title = tk.Label(StudentLogin, text = "Student Login", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50)) 
    # username label
    usernameLabel = tk.Label(StudentLogin, text = "Username: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15)) 
    # username entry box
    usernameEntry = tk.Entry(StudentLogin, textvariable = S_userN, width = 25, 
                            fg = "black", insertbackground = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # password label
    passwordLabel = tk.Label(StudentLogin, text = "Password: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # password entry box
    passwordEntry = tk.Entry(StudentLogin, textvariable = S_passW, width = 25, 
                            fg = "black", insertbackground = "black", bg = "light grey", show = "*", 
                            font = ("Lao Sangam MN", 15))
    # login button (calls the Logins class)
    loginButton = tk.Button(StudentLogin, text = "Login", bg = "light grey", fg = "black", 
                            width = 20, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: StudentLogins(studentPath, usernameEntry, passwordEntry, loginLabel))

    # back button (destroys the window)
    backButton = tk.Button(StudentLogin, text= "Back", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=StudentLogin.destroy)

    # positions of the labels, entry boxes and buttons
    loginLabel.place(x=630, y=20)
    title.place(x=560, y=120)
    usernameLabel.place(x=500, y=250)
    usernameEntry.place(x=600, y=250)
    passwordLabel.place(x=500, y=350)
    passwordEntry.place(x=600, y=350)
    loginButton.place(x=450, y=450)
    backButton.place(x=750, y=450)


def OpenStudentArea():
    global StudentArea # makes the window global
    StudentArea = tk.Toplevel(window1) # creates the child window
    StudentArea.title("Student Homepage") # creates the title of the window
    StudentArea.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    StudentArea.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # title label
    title = tk.Label(StudentArea, text = "Select an option", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # how to play button (leads to the how to play subroutine)
    howToPlay_B = tk.Button(StudentArea, text = "How to Play", bg="light grey", fg="black", 
                            width = 40, height = 5, font = ("Lao Sangam MN", 15),
                            command=OpenHowToPlay)
    # practice game button (leads to the practice game window)
    practiceGame_B = tk.Button(StudentArea, text = "Practice Game", bg="light grey", fg="black", 
                                width = 40, height = 5, font = ("Lao Sangam MN", 15), 
                                command=OpenPracticeGame)
    # play game button (leads to the screen where the user will enter a code to enter the official game)
    playGame_B = tk.Button(StudentArea, text = "Play Game", bg = "light grey", fg = "black", 
                            width = 40, height = 5, font = ("Lao Sangam MN", 15), state = tk.NORMAL, 
                            command=OpenCodeWindow)
    # back button (destroys the window)
    back_B = tk.Button(StudentArea, text = "Go Back", bg = "light grey", fg = "black", 
                        width = 20, height = 2, font = ("Lao Sangam MN", 15), 
                        command=StudentArea.destroy)

    # positions of the lables and buttons
    title.place(x=550, y=100)
    howToPlay_B.place(x=100, y=310)
    practiceGame_B.place(x=530, y=310)
    playGame_B.place(x=960, y=310)
    back_B.place(x=620, y=500)


def OpenHowToPlay():
    HowToPlay = tk.Toplevel(window1) # creates the child window
    HowToPlay.title("Student Homepage") # creates the title of the window
    HowToPlay.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    HowToPlay.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # title label
    title = tk.Label(HowToPlay, text = "How To Play", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 70))
    # boggle title label
    boggle_L = tk.Label(HowToPlay, text = "Boggle", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 40))
    # instructions on how to play the boggle section label
    step1 = tk.Label(HowToPlay, 
                    text = "1. The aim of the game is to try and make the longest word using the letters in the grid \n 2. Each letter must be connected either vertically, horizontally or diagonally \n 3. You get points depending on the length of your word", 
                    fg = "black", bg = "light grey", font = ("Lao Sangam MN", 20))
    # spelling bee title label
    spellingbee_L = tk.Label(HowToPlay, text = "Spelling Bee", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 40))
    # instructions on how to play the spelling bee section label
    step2 = tk.Label(HowToPlay, 
                    text = "1. The aim of this section is to correctly spell 10 random words from your chosen subject \n 2. For every word spelt correctly you get 1 point", 
                    fg = "black", bg = "light grey", font = ("Lao Sangam MN", 20))
    # anagram title label
    anagram_L = tk.Label(HowToPlay, text = "Anagram", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 40))
    # instructions on how to play the anagram section label
    step3 = tk.Label(HowToPlay, 
                    text = "1. The aim of this section is to correctly guess the anagram \n 2. You have one chance to guess the anagram, if you get it correct you get you get two bonus points", 
                    fg = "black", bg = "light grey", font = ("Lao Sangam MN", 20))
    # back button (destroys the window)
    back_B = tk.Button(HowToPlay, text = "Back", bg="light grey", fg="black", width = 25, height = 2, font = ("Lao Sangam MN", 15),command=HowToPlay.destroy)

    # positions for the labels and buttons
    title.place(x=550, y=100)
    boggle_L.place(x=100, y=200)
    step1.place(x=100, y=280)
    spellingbee_L.place(x=100, y=390)
    step2.place(x=100, y=460)
    anagram_L.place(x=100, y=540)
    step3.place(x=100, y=600)
    back_B.place(x=1000, y=400)


def OpenPracticeGame():
    PracticeGame = tk.Toplevel(window1) # creates the child window
    PracticeGame.title("Practice Game") # creates the title of the window
    PracticeGame.configure(bg="light grey") # makes the background colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    PracticeGame.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    SB_PracticeAns = tk.StringVar() # variable to store the user input for the spelling bee
    AG_PracticeAns = tk.StringVar() # variable to store the user input for the anagram
    word = [] # a list to store the word from the boggle
    # creates an instance of the PlayGame class
    play = PlayGame(0)
    # creates an instance of the PracticeGames class
    practice = PracticeGames(play)
    
    # title label
    label = tk.Label(PracticeGame, text = "Practice Round", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))

    # instructions for Boggle label
    BO_lable = tk.Label(PracticeGame, text = "Click the buttons with the letters to guess a word", 
                        bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    # label to store the answer chosen by the user
    PracticeAns = tk.Label(PracticeGame, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # creates an instance of the practice class
    
    # label to check the answer for the Boggle
    BOcheck_B = tk.Button(PracticeGame, text = "CHECK", bg = "light grey", fg = "black", 
                            width = 10, height = 1, font = ("Lao Sangam MN", 15), 
                            command = lambda: practice.MakeWordToList(PracticeAns.cget('text'), correctanswerlabel, incorrectanswerlabel))
    
    correctanswerlabel = tk.Label(PracticeGame, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    incorrectanswerlabel = tk.Label(PracticeGame, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    # clears the label (the user's answer for the Boggle)
    clear_B = tk.Button(PracticeGame, text = "CLEAR", bg = "light grey", fg = "black", width = 10, height = 1, font = ("Lao Sangam MN", 15), command = lambda: ClearBoggleAnswer(word, PracticeAns, correctanswerlabel, incorrectanswerlabel))

    
    # positions for the boggle labels and buttons
    label.place(x=580, y=50)
    BO_lable.place(x=80, y=500)
    PracticeAns.place(x=100, y=530)
    BOcheck_B.place(x=100, y=600)
    clear_B.place(x=230, y=600)
    correctanswerlabel.place(x=50, y=640)
    incorrectanswerlabel.place(x=100, y=640)
    
    # spelling bee title label
    SB_lable = tk.Label(PracticeGame, text = "Spell the word read out by the computer", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # text area for the words to spell to appear
    #wordsToSpell = tk.Text(PracticeGame, height = 5, width = 20, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # button to get the words for the spelling bee
    #access.EditPracticeFiles()
    getWord_B = tk.Button(PracticeGame, text = "Get Words", bg = "light grey", fg = "black", 
                            width = 15, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: practice.WordFromDropDown())
    # enty box for the users answer
    SB_PracticeAnswer = tk.Entry(PracticeGame, textvariable = SB_PracticeAns, width = 25, fg = "black", insertbackground = "black", bg = "light grey")
    # button to check spelling answer
    SBcheck_B = tk.Button(PracticeGame, text = "CHECK", bg = "light grey", fg = "black", width = 10, height = 1, font = ("Lao Sangam MN", 15), command=lambda: practice.checkAnswer(SB_PracticeAns.get(), SB_PracticeAnswer, correctanswerlabel, incorrectanswerlabel, PracticeGame))

    # positions of the labels, entry box, text area and buttons for the spelling bee section
    SB_lable.place(x=605, y=180)
    #wordsToSpell.place(x=650, y=230)
    getWord_B.place(x=660, y=380)
    SB_PracticeAnswer.place(x=625, y=460)
    SBcheck_B.place(x=682, y=510)

    # anagram title label
    AG_lable = tk.Label(PracticeGame, text = "Guess the anagram!", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # text area for the anagram words to appear
    anagramArea = tk.Text(PracticeGame, height = 5, width = 20, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # button to get the words for the anagram
    getAnagram_B = tk.Button(PracticeGame, text = "Get Words", bg = "light grey", fg = "black", 
                                width = 15, height = 2, font = ("Lao Sangam MN", 15), 
                                command = lambda: [practice.AddTextToBox(anagramArea), practice.AddToList()])
    # entry box to enter answer for anagram
    AG_PracticeAnswer = tk.Entry(PracticeGame, textvariable = AG_PracticeAns, width = 25, fg = "black", insertbackground = "black", bg = "light grey")
    # button to check the user's answer
    AGcheck_B = tk.Button(PracticeGame, text = "CHECK", bg = "light grey", fg = "black", width = 10, height = 1, font = ("Lao Sangam MN", 15), command=lambda: practice.CheckAnagramAns(AG_PracticeAns.get(), anagramArea, AG_PracticeAnswer, correctanswerlabel, incorrectanswerlabel))

    # position of the anagram label, entry box, text area and buttons
    AG_lable.place(x=1080, y=180)
    anagramArea.place(x=1050, y=230)
    getAnagram_B.place(x=1060, y=380)
    AG_PracticeAnswer.place(x=1025, y=460)
    AGcheck_B.place(x=1082, y=510)

    # back button (destroys the window)
    back_B = tk.Button(PracticeGame, text = "BACK", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=PracticeGame.destroy)
    # positin of back button
    back_B.place(x=600, y=700)
    # calls the subroutine to make the grid in the window
    makeGrid(PracticeGame, word, practice, PracticeAns) 


def OpenCodeWindow():
    global CodeWindow # makes the window a global variable
    CodeWindow = tk.Toplevel(window1) # creates the child window
    CodeWindow.title("Code Window") # creates the title of the window
    CodeWindow.configure(bg="light grey") # makes the background colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    CodeWindow.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    userCode = tk.StringVar() # a variable to store the code entered by the student

    # title label 
    title = tk.Label(CodeWindow, text = "Enter the code to get into the game", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 50))
    # entry box allowing the user to enter the code
    codeEntryBox = tk.Entry(CodeWindow, textvariable = userCode, width = 25, fg = "black", insertbackground = "black", bg = "light grey")
    # button to check if the code is correct
    confirm = tk.Button(CodeWindow, text = "Confirm", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=lambda: checkCode(userCode.get()))


    # positions of the label, entry box and button
    title.place(x=390, y=100)
    codeEntryBox.place(x=600, y=350)
    confirm.place(x=630, y=500)


def checkCode(code): # a subroutine that checks if the users code is correct
    try: # try except block to deal with the code not being generated 
        print(generateCode)
        newCode = "".join(generateCode) # makes the list of the code into string
        if code == newCode: # if the users code is equal to the correct code
            OpenPlayGame() # open the play game window to start the game
        else:
            CodeWindow.destroy() # will send the user back to the student area 
            # label telling the user that code was incorrect
            label = tk.Label(StudentArea, text = "You have entered an incorrect code, so you cannot enter the competition", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
            # posiiton of label
            label.place(x=550, y=700)
    except:
        print("no code has been generated so the competition cannot start") # prints to the terminal
        # label telling the user that the code has not been generated so the competition cannot start
        label = tk.Label(StudentArea, text = "no code has been generated so the competition cannot start", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
        # position of label
        label.place(x=550, y=700)
        CodeWindow.destroy()# will send the user back to the student area 
    


def OpenPlayGame():
    Game = tk.Toplevel(window1) # creates the child window
    Game.title("Inter-house Spelling Bee Game") # creates the title of the window
    Game.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    Game.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen
   
    # a variable to store the year selected by the student
    YearSelectedInStudent = tk.StringVar()

    # calls the accessFiles class
    access = AccessFiles()

    while '.DS_Store' in access.entries: # while loop that is used to search through the list self.entries to find the specified string
        access.entries.remove('.DS_Store') # removes 'DS_Store' which is stored in the self.entries so that it is not visible to user when selecting a year
    values = access.entries # stores the list of years in the variable values

    # title label
    title = tk.Label(Game, text = "Welcome to the Inter-House \n Spelling Bee Competition!", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 80))

    # instruction label
    label = tk.Label(Game, text = "Before you start enter the year of this competition:", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 25))

    # a dropdown box that allows the user to select the correct year
    getYear = ttk.Combobox(Game, width=15, textvariable=YearSelectedInStudent)

    # gets the values of the items in the contents box to be the folders in the spelling bee file directory 
    getYear['values'] = values

    # instruction label
    pressButton = tk.Label(Game, text = "Press the button to start!", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 25))
    # start button (starts the game)
    start_B = tk.Button(Game, text = "START", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=lambda: OpenBoggleWindow(YearSelectedInStudent.get(), 0))
    
    # positions of the labels, dropdown box and button
    title.place(x=250, y=130)
    label.place(x=450, y=390)
    getYear.place(x=625, y=440)
    pressButton.place(x=570, y=500)
    start_B.place(x=625, y=550)

##### STUDENT SECTION #####


##### STUDENTS - Boggle/Spelling Bee/Anagram #####

    

def clear(answer):
    answer.delete(0, tk.END) # clears the answer box for the spelling bee
 

def OpenBoggleWindow(Year, i):
    global BoggleWindow # makes the Boggle window global
    BoggleWindow = tk.Toplevel(window1) # creates the child window
    BoggleWindow.title("Boggle") # creates the title of the window
    BoggleWindow.configure(bg="light grey") # makes the background colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    BoggleWindow.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # checks if i=4 if so the current player will go back to the first team stored in the list
    if i == 4:
        i=0
    PlayG = PlayGame(i) # calls the playgame class
   
    # a list to store the users guess
    word = []
    
    # title label
    playBoggle = tk.Label(BoggleWindow, text = "Boggle", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 50))
    # instruction label (telling the user what to do next)
    nextOption = tk.Label(BoggleWindow, text = "Click the button to go to the spelling bee section or anagram section", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # button leading to the spelling bee section
    spellB_B = tk.Button(BoggleWindow, text = "Spelling Bee", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=lambda: OpenSpellingBeeWindow(Year, PlayG, i))
    # button leading to the anagram section
    anagram_B = tk.Button(BoggleWindow, text = "Anagram", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=lambda: OpenAnagramWindow(Year, PlayG, i))

    # label indicating the team
    teamLabel = tk.Label(BoggleWindow, text = "Team: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 25))
    # label that displays the team
    teamName = tk.Label(BoggleWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # label showing the teams points
    PointsLabel = tk.Label(BoggleWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # calling the display team method in the PlayGame class to present the team in the label
    PlayG.DisplayTeam(teamName)

    # instructions for the user
    entry_L = tk.Label(BoggleWindow, text = "Click the buttons with the letters to guess a word", 
                        bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    # label that contains the users answer once they click the buttons
    BoggleAnswerL = tk.Label(BoggleWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # a label to show that the answer is correct
    correctBoggleAns = tk.Label(BoggleWindow, text = " ", fg = "green", bg = "light grey", font = ("Lao Sangam MN", 25))
    # a label to show that the answer is incorrect
    IncorrectBoggleAns = tk.Label(BoggleWindow, text = " ", fg = "green", bg = "light grey", font = ("Lao Sangam MN", 25))
    
    
    # a button used to check if the answer is correct
    check_B = tk.Button(BoggleWindow, text = "CHECK", bg = "light grey", fg = "black", width = 10, height = 1, 
                        font = ("Lao Sangam MN", 15), 
                        command=lambda: b.MakeWordToList(BoggleAnswerL.cget('text'), PointsLabel, correctBoggleAns, IncorrectBoggleAns))
    # a button to the users answer if the made a mistake
    edit_B = tk.Button(BoggleWindow, text = "CLEAR", bg = "light grey", fg = "black", width = 10, height = 1, 
                        font = ("Lao Sangam MN", 15), command=lambda: ClearBoggleAnswer(word, BoggleAnswerL, correctBoggleAns, IncorrectBoggleAns))
    # a label showing the user to enter the users 
    pointsLabel = tk.Label(BoggleWindow, text = "Click the button to confirm your teams points at the end", 
                            bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # a button leading to the area where the user enters their points from each round
    confirmPoints_B = tk.Button(BoggleWindow, text = "Get Results", bg = "light grey", fg = "black", 
                                width = 10, height = 1, font = ("Lao Sangam MN", 15), command=lambda: ConfirmPoints(PlayG))
  
    # calls the boggle class
    b = Boggle(PlayG)
    # calls the subroutone that creates the grid of buttons
    makeGrid(BoggleWindow, word, b, BoggleAnswerL)
    
    # positions of the labels and buttons
    teamLabel.place(x=510, y=90)
    teamName.place(x=510, y=150)
    PointsLabel.place(x=510, y=200)
    BoggleAnswerL.place(x=100, y=550)
    check_B.place(x=250, y=610)
    edit_B.place(x=100, y=610)
    entry_L.place(x=90, y=510)
    playBoggle.place(x=950, y=50)
    nextOption.place(x=750, y=280)
    spellB_B.place(x=800, y=350)
    anagram_B.place(x=1050, y=350)
    correctBoggleAns.place(x=780, y=160)
    IncorrectBoggleAns.place(x=780, y=160)
    pointsLabel.place(x=800, y=500)
    confirmPoints_B.place(x=900, y=550)


def makeGrid(win, word, b, B_label):
    letterList = list("abcdefghijklmnopqrstuvwxyz") # a list of the letters in the alphabet
    lettersInGrid = [] # a list to store the letters in the grid
    print(letterList)
    
    randomLetter = random.sample(letterList, 16) # produces a random letter from the list (no repeated letter will be chosen)
    

    ## creates the first column of buttons ##
    b00 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[0], 
                    command = lambda: MakeGuess(B_label, word, b00.cget('text')))
    b00.place(x=0, y=0)
    b01 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[4], 
                    command = lambda: MakeGuess(B_label, word, b01.cget('text')))
    b01.place(x=0, y=120)
    b02 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[8], 
                    command = lambda: MakeGuess(B_label, word, b02.cget('text')))
    b02.place(x=0, y=240)
    b03 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[12],
                     command = lambda: MakeGuess(B_label, word, b03.cget('text')))
    b03.place(x=0, y=360)

    ## creates the second column of buttons ##
    b10 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[1], 
                    command = lambda: MakeGuess(B_label, word, b10.cget('text')))
    b10.place(x=110, y=0)
    b12 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[5], 
                    command = lambda: MakeGuess(B_label, word, b12.cget('text')))
    b12.place(x=110, y=120)
    b13 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[9], 
                    command = lambda: MakeGuess(B_label, word, b13.cget('text')))
    b13.place(x=110, y=240)
    b14 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[13],
                     command = lambda: MakeGuess(B_label, word, b14.cget('text')))
    b14.place(x=110, y=360)

    ## creates the third column of buttons ##
    b20 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[2], 
                    command = lambda: MakeGuess(B_label, word, b20.cget('text')))
    b20.place(x=220, y=0)
    b21 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[6], 
                    command = lambda: MakeGuess(B_label, word, b21.cget('text')))
    b21.place(x=220, y=120)
    b22 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[10],
                     command = lambda: MakeGuess(B_label, word, b22.cget('text')))
    b22.place(x=220, y=240)
    b23 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[14],
                     command = lambda: MakeGuess(B_label, word, b23.cget('text')))
    b23.place(x=220, y=360)

    ## creates the fourth column of buttons ##
    b30 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[3], 
                    command = lambda: MakeGuess(B_label, word, b30.cget('text')))
    b30.place(x=330, y=0)
    b31 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[7], 
                    command = lambda: MakeGuess(B_label, word, b31.cget('text')))
    b31.place(x=330, y=120)
    b32 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[11],
                     command = lambda: MakeGuess(B_label, word, b32.cget('text')))
    b32.place(x=330, y=240)
    b33 = tk.Button(win, height = 3, width = 6, font = ("Lao Sangam MN", 25), text = randomLetter[15],
                     command = lambda: MakeGuess(B_label, word, b33.cget('text')))
    b33.place(x=330, y=360)

    for i in randomLetter: # loops through the list of random letters created
        lettersInGrid.append(i) # adds each letter to the list of letters in the grid
    b.CreateListOfRandomLetters(lettersInGrid) # calls the boggle class and passes in the letters in the grid
    
    
def MakeGuess(label, word, letter):
    word.append(letter) # adds the value of the button to the list word
    print(word)
    guess = "".join(word) # joins the list word to become string
    print(guess)
    label.config(text = guess) # sets the label to be equal to the users answer so they can see what buttons they have selected
    

def ClearBoggleAnswer(word, ansLabel, correctLabel, incorrectLabel):

    ansLabel.config(text = "") # clears the boggle answer
    word.clear() # clears the list of the word selected in Boggle
    correctLabel.config(text="") # clears the correct answer label
    incorrectLabel.config(text="") # clears the incorrect answer label


def ClearAnswerSB_AG(correctLabel, incorrectLabel):
    correctLabel.config(text="") # clears the correct answer label
    incorrectLabel.config(text="") # clears the incorrect answer label


def CorrectMessage(label): # a subroutine the displays a message


    # a label that displays that the users answer is correct
    label.config(text = "CORRECT ANSWER! \n Choose the section you would like to move onto: ", fg = "green", bg = "light grey", font = ("Lao Sangam MN", 25))
    

def IncorrectMessage(label): # a subroutine the displays a message

    # a label that displays that the users answer is incorrect
    label.config(text = "INCORRECT ANSWER!", fg = "red", bg = "light grey", font = ("Lao Sangam MN", 40))
 

def OpenSpellingBeeWindow(Year, PlayG, i): # a subroutine that creates the spelling bee window used for the competition
    global SpellBeeWindow # makes the window global 
    SpellBeeWindow = tk.Toplevel(window1) # makes child window
    SpellBeeWindow.title("Spelling Bee") # creates the title of the window
    SpellBeeWindow.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    SpellBeeWindow.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # stores the users answer as a variable
    spellAns = tk.StringVar()
    # stores the year group selected in the drop down list as a variable
    yG = tk.StringVar()
    # stores the subject selected in the drop down list as a variable
    s = tk.StringVar()

    # makes an instance of the SpellBeeAnswer class
    w = SpellBeeAnswer()
    # makes an instance of the DisplayWords class
    d = DisplayWords()

    # label showing the points 
    PointsLabel = tk.Label(SpellBeeWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    # title label
    spellingBee_L = tk.Label(SpellBeeWindow, text = "Spelling Bee", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 70))

    # instruction label
    enterAns_L = tk.Label(SpellBeeWindow, text = "Type your answer here: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))

    # entry box for user to enter their answer
    spellingAnswer = tk.Entry(SpellBeeWindow, textvariable = spellAns, width = 25, fg = "black", insertbackground = "black", bg = "light grey")

    # Button to check the users answer (it calls the check answer method in SpellBeeAnswer class)
    checkAnswer = tk.Button(SpellBeeWindow, text = "CHECK", bg = "light grey", fg = "black", width = 20, height = 2, 
                            font = ("Lao Sangam MN", 20), command = lambda: w.checkAnswer(PlayG, spellAns.get(), spellingAnswer, Year, PointsLabel))

    # button that replays the audio of the word to be spelt (calls the PlayAgain method in DisplayWords)
    playAgain_B = tk.Button(SpellBeeWindow, text = "Play again", bg = "light grey", fg = "black", 
                            width = 20, height = 3, font = ("Lao Sangam MN", 20), command = lambda: d.PlayAgain(Year))

    # a button that send the user back to the boggle screen (calls the subroutine OpenBoggleWindow)
    next_B = tk.Button(SpellBeeWindow, text = "Back to Boggle", bg = "light grey", fg = "black", 
                        width = 20, height = 2, font = ("Lao Sangam MN", 20), command=lambda: OpenBoggleWindow(Year, i+1))

    # instruction label that asks the user for the year group they are in
    yearGroup_L = tk.Label(SpellBeeWindow, text = "What year group are you in? \n Select your year group from the drop down list: ", 
                            bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # a dropdown box that will show the year groups
    yearGroup = ttk.Combobox(SpellBeeWindow, width = 15, textvariable=yG)
    # the different year groups selectable
    yearGroup['values'] = ("Year 7", "Year 8", "Year 9", "Year 10+")

    # instruction label that asks the user for the subject they would like
    subject_L = tk.Label(SpellBeeWindow, text = "What subject would you like? \n Select the subject from the drop down list: ", 
                        bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # a dropdown box that will show the subject options
    subject = ttk.Combobox(SpellBeeWindow, width = 15, textvariable=s)
    # the different subjects selectable
    subject['values'] = ("Maths", "English", "Science")

    # a button that will get the words (calls the WordFromDropDown method from the DisplayWords class)
    getWord_B = tk.Button(SpellBeeWindow, text = "Get Words", bg = "light grey", fg = "black", width = 20, height = 3, font = ("Lao Sangam MN", 20), 
                            command = lambda: d.WordFromDropDown(yG.get(), s.get(), Year))

    # label indicating the team
    house_L = tk.Label(SpellBeeWindow, text = "Team: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30))
    # label that displays the team
    teamName = tk.Label(SpellBeeWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    
    # calls the PlayGame class to display the current team
    PlayG.DisplayTeam(teamName)
    
    # instruction label showing what the user should do next
    correct = tk.Label(SpellBeeWindow, text = "Click the button to go back to the boggle \n once all of the words are finished or you have spelt a word wrong", 
                        bg = "light grey", fg = "black", font = ("Lao Sangam MN", 25))
            


    
    # positions of the buttons, labels, entry box, and dropdown boxes
    spellingBee_L.place(x=500, y=50)

    enterAns_L.place(x=610, y=450)
    spellingAnswer.place(x=590, y=490)

    checkAnswer.place(x=580, y=540)
    playAgain_B.place(x=940, y=500)
    next_B.place(x=580, y=620)

    house_L.place(x=190, y=120)
    teamName.place(x=185, y=165)
    PointsLabel.place(x=700, y=350)

    yearGroup_L.place(x=80, y=270)
    yearGroup.place(x=190, y=350)

    subject_L.place(x=95, y=380)
    subject.place(x=190, y=460)
    getWord_B.place(x=135, y=530)
    
    correct.place(x=510, y=730)


def OpenAnagramWindow(Year, PlayG, i):
    global AnagramWindow # makes the anagram window global
    AnagramWindow = tk.Toplevel(window1) # creates the child window
    AnagramWindow.title("Anagram") # creates the title of the window
    AnagramWindow.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    AnagramWindow.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # stores the users answer for the anagram as a variable
    anagramAns = tk.StringVar()

    # title label
    title = tk.Label(AnagramWindow, text = "Solve the anagram", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 50))
    # text area to display the anagrams
    AnswertextArea = tk.Text(AnagramWindow, height = 20, width = 30, bg = "light grey", fg = "black")
    # instruction label (telling the user to type their answer in the entry box)
    enterAns_L = tk.Label(AnagramWindow, text = "Type your answer here: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # the entry box where the player will enter their answer
    anagramAnswer = tk.Entry(AnagramWindow, textvariable = anagramAns, width = 25, fg = "black", insertbackground = "black", bg = "light grey")
    # a label that displays the points collected
    PointsLabel = tk.Label(AnagramWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    
    # creates an instance of the CheckAnagram Class
    a = CheckAnagram(Year)
    # calls the method AddToList in the CheckAnagram Class
    a.AddToList()
    # calls the method AddTextToBox in the CheckAnagram Class
    a.AddTextToBox(AnswertextArea)

    # button used to check the player's answer
    checkAnswer = tk.Button(AnagramWindow, text = "CHECK", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: a.CheckAnagramAns(PlayG, anagramAns.get(), anagramAnswer, Year, AnswertextArea))
    # button leading the player back to the Boggle window (calls the OpenBoggleWindow subroutine)
    next_B = tk.Button(AnagramWindow, text = "Back to Boggle", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=lambda:OpenBoggleWindow(Year, i+1))
    # label indicating the team
    team_L = tk.Label(AnagramWindow, text = "Team: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # label that displays the team
    teamName = tk.Label(AnagramWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # calls the DisplayTeam method in the PlayGame class 
    PlayG.DisplayTeam(teamName)

    # positions of the labels, buttons, text area and entry box
    title.place(x=540, y=50)
    AnswertextArea.place(x=620, y=150)
    enterAns_L.place(x=660, y=450)
    anagramAnswer.place(x=620, y=500)
    checkAnswer.place(x=650, y=540)
    next_B.place(x=650, y=600)

    team_L.place(x=80, y=120)
    teamName.place(x=140, y=200)
    PointsLabel.place(x=140, y=250)


def ConfirmPoints(PlayG):
    PointsWindow = tk.Toplevel(window1) # creates the child window
    PointsWindow.title("End Window") # creates the title of the window
    PointsWindow.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    PointsWindow.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # instruction title (telling the user to enter their points for their team)
    endWinLabel = tk.Label(PointsWindow, text = "Enter the number of points your team has in the label box: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30))
    # north title text
    north = tk.Label(PointsWindow, text = "NORTH")
    # text area for north team
    NorthBox = tk.Text(PointsWindow, width=10, height=10, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # south title text
    south = tk.Label(PointsWindow, text = "SOUTH")
    # text area for south team
    SouthBox = tk.Text(PointsWindow, width=10, height=10, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # hartley title text
    hartley = tk.Label(PointsWindow, text = "HARTLEY")
    # text area for hartley team
    HartleyBox = tk.Text(PointsWindow, width=10, height=10, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # waller title text
    waller = tk.Label(PointsWindow, text = "WALLER")
    # text area for waller team
    WallerBox = tk.Text(PointsWindow, width=10, height=10, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    # label that shows the team who has the most points
    pointsLabel = tk.Label(PointsWindow, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30))
    # label indicating the winning team
    winner = tk.Label(PointsWindow, text = "The Winner is: ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 30))
    # button that will add up the points for north 
    displayTeams = tk.Button(PointsWindow, text = "Confirm North", bg = "light grey", fg = "black", width = 10, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: 
                            PlayG.NorthPoints(NorthBox.get(1.0, 2.0), NorthBox.get(2.0, 3.0), NorthBox.get(3.0, 4.0), NorthBox.get(4.0, 5.0)))
    # team button position
    displayTeams.place(x=30, y=500)

    displayTeams = tk.Button(PointsWindow, text = "Confirm South", bg = "light grey", fg = "black", width = 10, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: 
                            PlayG.SouthPoints(SouthBox.get(1.0, 2.0), SouthBox.get(2.0, 3.0), SouthBox.get(3.0, 4.0), SouthBox.get(4.0, 5.0)))
    # team button
    displayTeams.place(x=150, y=500)


    displayTeams = tk.Button(PointsWindow, text = "Confirm Hartley", bg = "light grey", fg = "black", width = 10, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: 
                            PlayG.HartleyPoints(HartleyBox.get(1.0, 2.0), HartleyBox.get(2.0, 3.0), HartleyBox.get(3.0, 4.0), HartleyBox.get(4.0, 5.0)))
    
    # team button
    displayTeams.place(x=270, y=500)

    displayTeams = tk.Button(PointsWindow, text = "Confirm Waller", bg = "light grey", fg = "black", width = 10, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: 
                            PlayG.WallerPoints(WallerBox.get(1.0, 2.0), WallerBox.get(2.0, 3.0), WallerBox.get(3.0, 4.0), WallerBox.get(4.0, 5.0)))
    
    
    finalPoints = tk.Button(PointsWindow, text = "Final Points", bg = "light grey", fg = "black", width = 10, height = 2, font = ("Lao Sangam MN", 15), 
                            command = lambda: PlayG.DisplayPoints(pointsLabel))
    

    # positions of the labels and text areas
    displayTeams.place(x=390, y=500)
    
    north.place(x=50, y=150)
    NorthBox.place(x=50, y=200)

    south.place(x=150, y=150)
    SouthBox.place(x=150, y=200)

    hartley.place(x=250, y=150)
    HartleyBox.place(x=250, y=200)

    waller.place(x=350, y=150)
    WallerBox.place(x=350, y=200)

    endWinLabel.place(x=350, y=50)
    winner.place(x=690, y=200)
    pointsLabel.place(x=700, y=250)
    

    finalPoints.place(x=700, y=350)



##### STUDENTS - Boggle/Spelling Bee/Anagram #####



##### TEACHER SECTION #####

def OpenTeacherLogin():
    global TeacherLogin # makes the TeacherLogin window global
    global T_userN # makes the username global so that it can be checked again if the user gets the details wrong
    global T_passW # makes the password global so that it can be checked again if the user gets the details wrong
    TeacherLogin = tk.Toplevel(window1) # creates the child window
    TeacherLogin.title("Teacher Login") # creates the title of the window
    TeacherLogin.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    TeacherLogin.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    access = AccessFiles() # creates an object of the AccessFiles class
    teacherPath = os.path.join(access.path, "Teacher Login Details") # creates a path to access the teacher login files
    #teacher = TeacherLogins(teacherPath) # creates an object of the Teacher Login class

    T_userN = tk.StringVar() # a variable to store the username entered by the user
    T_passW = tk.StringVar() # a variable to store the password entered by the user

    loginLabel = tk.Label(TeacherLogin, text = "", bg = "light grey", font = ("Lao Sangam MN", 15))

    # title label
    title = tk.Label(TeacherLogin, text = "Teacher Login", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # label indicating where the user should enter the username
    usernameLabel = tk.Label(TeacherLogin, text = "Username: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # entry box where the user will enter their username
    usernameEntry = tk.Entry(TeacherLogin, textvariable = T_userN, width = 25, fg = "black", insertbackground = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # label indicating where the user should enter the password
    passwordLabel = tk.Label(TeacherLogin, text = "Password: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # entry box where the user will enter their password
    passwordEntry = tk.Entry(TeacherLogin, textvariable = T_passW, width = 25, fg = "black", insertbackground = "black", bg = "light grey", show = "*", font = ("Lao Sangam MN", 15))
    # login button (checks if the username and password is correct and sends them to the homepage for the teachers done in the TeacherLogins class)
    loginButton = tk.Button(TeacherLogin, text = "Login", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command = lambda:  TeacherLogins(teacherPath, usernameEntry, passwordEntry, loginLabel))
    # back button (destroys the window)
    backButton = tk.Button(TeacherLogin, text= "Back", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=TeacherLogin.destroy)

    # positions for the labels, buttons and entry boxes
    loginLabel.place(x=630, y=20)
    title.place(x=560, y=120)
    usernameLabel.place(x=500, y=250)
    usernameEntry.place(x=600, y=250)
    passwordLabel.place(x=500, y=350)
    passwordEntry.place(x=600, y=350)
    loginButton.place(x=450, y=450)
    backButton.place(x=750, y=450)


def OpenTeacherArea():
    TeacherArea = tk.Toplevel(window1) # creates the child window
    TeacherArea.title("Teacher Homepage") # creates the title of the window
    TeacherArea.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    TeacherArea.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # title label
    title = tk.Label(TeacherArea, text = "Select an option", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # button allowing the user to open an existing game
    openExisting = tk.Button(TeacherArea, text = "Open Existing Game", bg="light grey", fg="black", width = 20, height = 5, font = ("Lao Sangam MN", 15),command=OpenSelectYear)
    # button allowing the user to create a new game
    createNew = tk.Button(TeacherArea, text = "Create New Game", bg="light grey", fg="black", width = 20, height = 5, font = ("Lao Sangam MN", 15),command=OpenCreateNew)
    # button allowing the user to start the game
    startGame_B = tk.Button(TeacherArea, text = "Start Game", bg="light grey", fg="black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenUnlockGame)
    # back button (destroys the window)
    back_B = tk.Button(TeacherArea, text = "Back", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=TeacherArea.destroy)

    # positions of the buttons
    title.place(x=550, y=100)
    openExisting.place(x=50, y=310)
    createNew.place(x=280, y=310)
    startGame_B.place(x=530, y=310)
    back_B.place(x=960, y=310)


def OpenSelectYear():
    SelectYear = tk.Toplevel(window1) # creates the child window
    SelectYear.title("Edit Game") # creates the title of the window
    SelectYear.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    SelectYear.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # a variable to store the year entered by the user
    Year = tk.StringVar()
    # creates an object of the AccessFiles class
    access = AccessFiles()
    
    # instruction label for the user
    selectyearLabel = tk.Label(SelectYear, text = "Push the button to select a year to edit: ", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # shows where the list of past years will be
    text = tk.Label(SelectYear, text = "List of past years: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 25))
    # label that will display the list of past years
    listOfYears = tk.Label(SelectYear, text = " ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # entry box allowing the user to select a year
    yearWanted = tk.Entry(SelectYear, textvariable = Year, width = 20, fg = "black", insertbackground = "black", bg = "light grey")

    messageLabel = tk.Label(SelectYear, text = " ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))

    # button that will present the previous years
    getYears = tk.Button(SelectYear, text= "Get Years", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=lambda: access.OpenExistingFolder(listOfYears))
    # button that will confirm the users selected year
    confirm_B = tk.Button(SelectYear, text= "Confirm", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command= lambda: access.GetYear(Year.get(), messageLabel, yearWanted))
    # button that leads them to edit the game with the year they selected
    next_B = tk.Button(SelectYear, text= "Go to Edit Game", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command=lambda: OpenEditGame(Year.get()))
    # back button (destroys the window)
    back_B = tk.Button(SelectYear, text= "Back", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command=SelectYear.destroy)

    
    # positions of the labels, buttons and entry box
    selectyearLabel.place(x=350, y=50)
    text.place(x=530, y=200)
    listOfYears.place(x=550, y=250)
    yearWanted.place(x=530, y=400)
    messageLabel.place(x=250, y=300)

    getYears.place(x=750, y=300)
    confirm_B.place(x=480, y=500)
    next_B.place(x=800, y=600)
    back_B.place(x=770, y=500)


def OpenCreateNew():
    CreateNew = tk.Toplevel(window1) # creates the child window
    CreateNew.title("Teacher Homepage") # creates the title of the window
    CreateNew.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    CreateNew.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # a variable to store the users selected year 
    NewYear = tk.StringVar()
    # creates an instance of the AccessFiles class
    access = AccessFiles()
    
    # a folder indicating the existing folders
    ExistingFolders = tk.Label(CreateNew, text = "Existing folders: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 25))
    # a lable that displays the existing folders
    ExistingYears = tk.Label(CreateNew, text = " ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # calls the OpenExistingFolder method from the Accessfile class
    access.OpenExistingFolder(ExistingYears)

    # label that shows if the new year the uer has created exists or not
    messageLabel = tk.Label(CreateNew, text = " ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))

    successmessageLabel = tk.Label(CreateNew, text = " ", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))

    # label indicating where the user should enter their answer
    enteryearLabel = tk.Label(CreateNew, text = "Enter the new year you would like to create: ", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # entry box for user to enter the new year
    yearWanted = tk.Entry(CreateNew, textvariable = NewYear, width = 20, fg = "black", insertbackground = "black", bg = "light grey")
    # button to confirm the new year created
    confirm_B = tk.Button(CreateNew, text= "Confirm", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command= lambda: access.CreateNewFolder(NewYear.get(), messageLabel, successmessageLabel))
    # button that leads the user to the edit game section where they can edit the game they just created
    next_B = tk.Button(CreateNew, text= "Go to Edit Game", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command=lambda: OpenEditGame(NewYear.get()))
    # back button (destoys the current window)
    back_B = tk.Button(CreateNew, text= "Back", bg = "light grey", fg = "black", width = 25, height = 2, font = ("Lao Sangam MN", 15), command=CreateNew.destroy)

    # position of the lables, buttons and entry box
    enteryearLabel.place(x=300, y=50)
    yearWanted.place(x=530, y=400)

    ExistingFolders.place(x=50, y=200)
    ExistingYears.place(x=250, y=200)
    messageLabel.place(x=250, y=300)
    successmessageLabel.place(x=250, y=300)

    confirm_B.place(x=480, y=500)
    next_B.place(x=750, y=600)
    back_B.place(x=770, y=500)


def OpenEditGame(Year):
    EditGame = tk.Toplevel(window1) # creates the child window
    EditGame.title("Edit Game") # creates the title of the window
    EditGame.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    EditGame.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # instruction label telling the user to press a button
    enterNewLabel = tk.Label(EditGame, text = "Select an option", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # edit spelling bee button (allows the user to enter the words for the spelling bee section)
    enterNewSpell_B = tk.Button(EditGame, text= "Edit spelling bee", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=lambda: OpenEnterNewWords(Year))
    # edit anagram button (allows the user to enter the anagrams to use for the anagram section)
    enterNewAnagram_B = tk.Button(EditGame, text= "Edit anagram", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=lambda: OpenEditAnagram(Year))
    # locks the game so that the student players cannot access the game until the game officially starts
    lockGame_B = tk.Button(EditGame, text= "Lock Game", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenLockedGame)
    # back button (destroys the window)
    back_B = tk.Button(EditGame, text= "Back", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=EditGame.destroy)

    # positions of the buttons and label
    enterNewLabel.place(x=550, y=100)
    enterNewSpell_B.place(x=100, y=310)
    enterNewAnagram_B.place(x=530, y=310)
    lockGame_B.place(x=960, y=310)
    back_B.place(x=620, y=500)


def lockGame(lock, label):
    global generateCode # makes the random code a global variable
    if lock: # if true
        print("lock")
        generateCode = random.sample(string.ascii_letters, 5) # a random code will be generated
        # a label showing the user what to do next
        label.config(text = "code has been generated \n if you would like to have access to the code please unlock the game")
        print(generateCode)
    else:
        print("unlock")
        # a label indicating where the code will be presented
        code = tk.Label(UnlockGame, text= "Code: ", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 25))
        # position of the label
        code.place(x=500, y=640)
        # another label that displays the code 
        label.config(text = generateCode)
        print(generateCode)


def OpenLockedGame():
    LockGame = tk.Toplevel(window1) # creates the child window
    LockGame.title("Lock Game") # creates the title of the window
    LockGame.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    LockGame.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen
    lock = True # a boolean value to check if the game should be locked or not

    # label that is adjusted if the game is locked (tells the user what to do next)
    label = tk.Label(LockGame, text= "", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # title label
    lock_L = tk.Label(LockGame, text="Click the button to lock the game", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # button that allows the user to lock the game by creating a code that can only be know if the game has been unlocked
    lockButton = tk.Button(LockGame, text= "Lock", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command= lambda: lockGame(lock, label))
    # back button leads the user back to the teacher area
    back_B = tk.Button(LockGame, text= "Back", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenTeacherArea)
    
    # positions of the labels and buttons
    label.place(x=500, y=650)
    lock_L.place(x=390, y=100)
    lockButton.place(x=330, y=310)
    back_B.place(x=760, y=310)
    
    
def OpenUnlockGame():
    global UnlockGame # makes the window global
    UnlockGame = tk.Toplevel(window1) # creates the child window
    UnlockGame.title("Unlock Game") # creates the title of the window
    UnlockGame.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    UnlockGame.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen
    lock = False # a boolean value to check if the game should be locked or not

    # label that is adjusted if the game is unlocked it will show the code that the teacher can share with the students to access the game
    label = tk.Label(UnlockGame, text= "", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    # title label
    unlock_L = tk.Label(UnlockGame, text="Click the button to unlock the game", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    # button that will present the code to unlock the game
    unlockButton = tk.Button(UnlockGame, text= "Unlock", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=lambda: lockGame(lock, label))
    # back button leading the user back to the teacher area
    back_B = tk.Button(UnlockGame, text= "Back", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenTeacherArea)

    # positions of the labels and buttons
    label.place(x=500, y=700)
    unlock_L.place(x=390, y=100)
    unlockButton.place(x=330, y=310)
    back_B.place(x=760, y=310)

##### TEACHER SECTION #####



##### CREATE SPELLING BEE #####

def OpenEnterNewWords(Year):
    EnterNewWords = tk.Toplevel(window1) # creates the child window
    EnterNewWords.title("Creating New Game") # creates the title of the window
    EnterNewWords.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    EnterNewWords.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # instruction for user to press the button to enter the maths words
    mathsWordsLabel = tk.Label(EnterNewWords, text = "Press the button to enter maths words", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # button leading to screen where user can enter the maths words
    mathsWordsButton = tk.Button(EnterNewWords, text = "Maths Words", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command = lambda: CreateMathsWords(Year))
    # instruction for user to press the button to enter the english words
    englishWordsLabel = tk.Label(EnterNewWords, text = "Press the button to enter english words", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # button leading to screen where user can enter the english words
    englishWordsButton = tk.Button(EnterNewWords, text = "English Words", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command = lambda: CreateEnglishWords(Year))
    # instruction for user to press the button to enter the science words
    scienceWordsLabel = tk.Label(EnterNewWords, text = "Press the button to enter science words", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 20))
    # button leading to screen where user can enter the science words
    scienceWordsButton = tk.Button(EnterNewWords, text = "Science Words", bg = "light grey", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command = lambda: CreateScienceWords(Year))
    # back button allows the user to go back to the previous screen (destroys window)
    back_B = tk.Button(EnterNewWords, text = "Back", bg = "light grey", fg = "black", width = 20, height = 2, font = ("Lao Sangam MN", 15), command=EnterNewWords.destroy)

    # positions of the labels and buttons
    mathsWordsLabel.place(x=100, y=210)
    mathsWordsButton.place(x=100, y=310)
    englishWordsLabel.place(x=530, y=210)
    englishWordsButton.place(x=530, y=310)
    scienceWordsLabel.place(x=960, y=210)
    scienceWordsButton.place(x=960, y=310)
    back_B.place(x=620, y=500)


def GetText(words, f, win, year, label): # subroutine that checks that the words entered by the user are correct and adds it into the specified file
    global spellingWords # makes the words entered by the user a global variable

    label.config(text = words.get(1.0, tk.END)) # edits the text variable for the label in each screen to show the words the user entered
    spellingWords = words.get(1.0, tk.END) # gets the words the user entered into the text area
    access = AccessFiles() # makes an instance of the AccessFiles class

    # gets the user to check if their spelling is correct
    check = tk.Label(win, text = "Is each word spelt correctly?", bg = "light grey", fg = "black")
    # position of label
    check.place(x=1250, y=600)
    # button for user to click if their spelling is correct
    yes = tk.Button(win, text = "Yes", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15), command = lambda: access.editFile(f, year))
    # position of button
    yes.place(x=1300, y=650)
    # button for user to click if their spelling is incorrect
    no = tk.Button(win, text = "No", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15), command = lambda: words.delete(1.0, tk.END))
    # position of button
    no.place(x=1300, y=690)


def CreateMathsWords(Year): # a subroutine that allows the user to create the spelling bee words for the competitions - for the subject Maths
    MathsWords = tk.Toplevel(window1) # creates the child window
    MathsWords.title("Creating New Game") # creates the title of the window
    MathsWords.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    MathsWords.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # label that shows the words entered by the user to confirm if they are correct or not
    label = tk.Label(MathsWords, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # instruction for user
    yr7WordsLabel = tk.Label(MathsWords, text = "Enter the words for year 7 maths", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr7Words = tk.Text(MathsWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr7Button = tk.Button(MathsWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr7Words, "Year 7 Maths Words", MathsWords, Year, label))
    
    

    # instruction for user
    yr8WordsLabel = tk.Label(MathsWords, text = "Enter the words for year 8 maths", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr8Words = tk.Text(MathsWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr8Button = tk.Button(MathsWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr8Words, "Year 8 Maths Words", MathsWords, Year, label))
    
    
    # instruction for user
    yr9WordsLabel = tk.Label(MathsWords, text = "Enter the words for year 9 maths", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr9Words = tk.Text(MathsWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr9Button = tk.Button(MathsWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr9Words, "Year 9 Maths Words", MathsWords, Year, label))
    
    
    # instruction for user
    yr10PlusWordsLabel = tk.Label(MathsWords, text = "Enter the words for year 10+ maths", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr10PlusWords = tk.Text(MathsWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr10PlusButton = tk.Button(MathsWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr10PlusWords, "Year 10+ Maths Words", MathsWords, Year, label))

    
    # back button (destroys current window)
    back_B = tk.Button(MathsWords, text = "Back", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=MathsWords.destroy)
    
    # positions of the labels, text areas and buttons
    yr7WordsLabel.place(x=95, y=90)
    Yr7Words.place(x=80, y=150)
    Yr7Button.place(x=120, y=600)
    yr8WordsLabel.place(x=395, y=90)
    Yr8Words.place(x=380, y=150)
    Yr8Button.place(x=420, y=600)
    yr9WordsLabel.place(x=695, y=90)
    Yr9Words.place(x=680, y=150)
    Yr9Button.place(x=720, y=600)
    yr10PlusWordsLabel.place(x=995, y=90)
    Yr10PlusWords.place(x=980, y=150)
    Yr10PlusButton.place(x=1020, y=600)
    label.place(x=1320, y=300)
    back_B.place(x=1250, y=200)


def CreateEnglishWords(Year): # a subroutine that allows the user to create the spelling bee words for the competitions - for the subject English
    EnglishWords = tk.Toplevel(window1) # creates the child window
    EnglishWords.title("Creating New Game") # creates the title of the window
    EnglishWords.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    EnglishWords.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen


    # label that shows the words entered by the user to confirm if they are correct or not
    label = tk.Label(EnglishWords, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # instruction for user
    yr7WordsLabel = tk.Label(EnglishWords, text = "Enter the words for year 7 english", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr7Words = tk.Text(EnglishWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr7Button = tk.Button(EnglishWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr7Words, "Year 7 English Words", EnglishWords, Year, label))
    
    # instruction for user
    yr8WordsLabel = tk.Label(EnglishWords, text = "Enter the words for year 8 english", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr8Words = tk.Text(EnglishWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr8Button = tk.Button(EnglishWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr8Words, "Year 8 English Words", EnglishWords, Year, label))
    
    # instruction for user
    yr9WordsLabel = tk.Label(EnglishWords, text = "Enter the words for year 9 english", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr9Words = tk.Text(EnglishWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr9Button = tk.Button(EnglishWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr9Words, "Year 9 English Words", EnglishWords, Year, label))
    
    # instruction for user
    yr10PlusWordsLabel = tk.Label(EnglishWords, text = "Enter the words for year 10+ english", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr10PlusWords = tk.Text(EnglishWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr10PlusButton = tk.Button(EnglishWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr10PlusWords, "Year 10+ English Words", EnglishWords, Year, label))
    
    # back button (destroys the current window)
    back_B = tk.Button(EnglishWords, text = "Back", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=EnglishWords.destroy)
    
    # positions for the labels, text areas and buttons
    yr7WordsLabel.place(x=95, y=90)
    Yr7Words.place(x=80, y=150)
    Yr7Button.place(x=120, y=600)
    yr8WordsLabel.place(x=395, y=90)
    Yr8Words.place(x=380, y=150)
    Yr8Button.place(x=420, y=600)
    yr9WordsLabel.place(x=695, y=90)
    Yr9Words.place(x=680, y=150)
    Yr9Button.place(x=720, y=600)
    yr10PlusWordsLabel.place(x=995, y=90)
    Yr10PlusWords.place(x=980, y=150)
    Yr10PlusButton.place(x=1020, y=600)
    label.place(x=1320, y=300)
    back_B.place(x=1250, y=200)


def CreateScienceWords(Year): # a subroutine that allows the user to create the spelling bee words for the competitions - for the subject of Science
    ScienceWords = tk.Toplevel(window1) # creates the child window
    ScienceWords.title("Creating New Game") # creates the title of the window
    ScienceWords.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    ScienceWords.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen
    
    # label that shows the words entered by the user to confirm if they are correct or not
    label = tk.Label(ScienceWords, text = "", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))

    # instruction for user
    yr7WordsLabel = tk.Label(ScienceWords, text = "Enter the words for year 7 science", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr7Words = tk.Text(ScienceWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr7Button = tk.Button(ScienceWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr7Words, "Year 7 Science Words", ScienceWords, Year, label))
    
    # instruction for user
    yr8WordsLabel = tk.Label(ScienceWords, text = "Enter the words for year 8 science", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr8Words = tk.Text(ScienceWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr8Button = tk.Button(ScienceWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr8Words, "Year 8 Science Words", ScienceWords, Year, label))
    
    # instruction for user
    yr9WordsLabel = tk.Label(ScienceWords, text = "Enter the words for year 9 science", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr9Words = tk.Text(ScienceWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr9Button = tk.Button(ScienceWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr9Words, "Year 9 Science Words", ScienceWords, Year, label))
    
    # instruction for user
    yr10PlusWordsLabel = tk.Label(ScienceWords, text = "Enter the words for year 10+ science", bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # text area for user to enter the words for the subject and year group
    Yr10PlusWords = tk.Text(ScienceWords, height = 15, width = 25, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the words entered by the user
    Yr10PlusButton = tk.Button(ScienceWords, text = "Finished", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: GetText(Yr10PlusWords, "Year 10+ Science Words", ScienceWords, Year, label))
    
    # back button (destroys the current window)
    back_B = tk.Button(ScienceWords, text = "Back", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=ScienceWords.destroy)

    # positions for labels, text areas and buttons
    yr7WordsLabel.place(x=95, y=90)
    Yr7Words.place(x=80, y=150)
    Yr7Button.place(x=120, y=600)
    yr8WordsLabel.place(x=395, y=90)
    Yr8Words.place(x=380, y=150)
    Yr8Button.place(x=420, y=600)
    yr9WordsLabel.place(x=695, y=90)
    Yr9Words.place(x=680, y=150)
    Yr9Button.place(x=720, y=600)
    yr10PlusWordsLabel.place(x=995, y=90)
    Yr10PlusWords.place(x=980, y=150)
    Yr10PlusButton.place(x=1020, y=600)
    label.place(x=1320, y=300)
    back_B.place(x=1250, y=200)

##### CREATE SPELLING BEE #####


##### CREATE ANAGRAM #####

# a subroutine that allows the user to edit the anagram section of the game 
# by allowing them to generate anagrams from the words that they have entered

def OpenEditAnagram(Year): 
    global AnagramtextArea # makes the text area global 
    global enterWord # makes the entry box global
    global selectedAnagrams # makes the text area global

    EditAnagram = tk.Toplevel(window1) # creates the child window
    EditAnagram.title("Lock Game") # creates the title of the window
    EditAnagram.configure(bg="light grey") # makes the back ground colour of the window light grey
    width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
    height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
    EditAnagram.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen

    # calls an instance of the AccessFiles class to store the anagram file in he correct path
    access = AccessFiles()

    # stores the word entered by the user as a variable
    newAnagram = tk.StringVar()

    # title label of window
    anagramLabel = tk.Label(EditAnagram, text = "Edit Anagram", fg = "black", bg = "grey", font = ("Lao Sangam MN", 50))
    
    # label informing the user of what to do next
    title_L = tk.Label(EditAnagram, text = "Enter a word to generate an anagram of it", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 20))
    
    # label informing the user of what to do next
    entry_L = tk.Label(EditAnagram, text = "Enter your word here:", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    
    # the word entered by the user to generate an anagram of
    enterWord = tk.Entry(EditAnagram, textvariable = newAnagram, width = 25, fg = "black", insertbackground = "black", bg = "light grey")
    
    # button that generates anagrams
    confirmWord = tk.Button(EditAnagram, text = "Create Anagram", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda: CreateList(newAnagram.get()))

    # label informing the user of what to do next
    selectedLabel = tk.Label(EditAnagram, text = "Copy the selected anagrams here:", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 15))
    
    # text area to store anagrams selected by the user
    selectedAnagrams = tk.Text(EditAnagram, height = 5, width = 30, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # button to confirm the anagrams selected by the user
    confirmAnagrams = tk.Button(EditAnagram, text = "Confirm", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command = lambda:[access.editAnagramFile("Anagram File", Year, selectedAnagrams.get(1.0, tk.END)), access.editAnagramFile("Original Anagram File", Year, selectedAnagrams.get(1.0, tk.END))])
    
    # text area to store generated anagrams
    AnagramtextArea = tk.Text(EditAnagram, height = 20, width = 40, bg = "light grey", fg = "black", font = ("Lao Sangam MN", 15))
    
    # back button (destroys window)
    back_B = tk.Button(EditAnagram, text = "Back", bg = "light grey", fg = "black", width = 15, height = 2, font = ("Lao Sangam MN", 15), command=EditAnagram.destroy)

    # positions of the labels, entry boxex, text area and buttons
    anagramLabel.place(x=570, y=50)
    title_L.place(x=200, y=200)
    entry_L.place(x=200, y=250)
    enterWord.place(x=200, y=300)
    confirmWord.place(x=200, y=350)
    AnagramtextArea.place(x=600, y=200)
    selectedLabel.place(x=1000, y=160)
    selectedAnagrams.place(x=1000, y=200)
    confirmAnagrams.place(x=1000, y=400)
    back_B.place(x=200, y=420)


def CreateList(string): # a subroutine that creates a list using the value of the user input 
    word = [] # list variable that will store the letters of the word entered by the user
    for i in string: # loops through l
        word.append(i) # adds each letter into the list 'word'
    a = CreateAnagrams() # calls an instance of the class CreateAnagrams
    a.AddLettersIntoQueue(word) # calls a method in CreateAnagrams that will make the letters of the word entered by the user into a queue


def AddToTextBox(NewAnagramList, length): # a subroutine that adds the anagram words to the text area
    for i in range(length): # loops through the variable passed in called length 
        popped = NewAnagramList.pop() # pops the next anagram in line to be presented 
        newLine = "\n" # stores a new line 
        AnagramtextArea.insert(tk.END, popped) # inserts the anagram into the text area 
        AnagramtextArea.insert(tk.END, newLine) # adds the new line to seperate each generated anagram 
    remove_duplicate(AnagramtextArea) # calls the subroutine that will remove any duplicates in the text area


def remove_duplicate(text):
    values = text.get(1.0, tk.END).split('\n') # Initial values
    print(values)
    print("number of anagrams created: ", len(values)) # prints the number of permutations made (only used to show how many permutations are made not necessary for the program just for the testing)
    #values = text.get(1.0, 101.0).split('\n') # gets the values from line 1 to line 100
    duplicates = [] # an empty list to append all non duplicates
    text.delete(1.0, tk.END) # it eemoves currently written words
    
    for i in values: # loops through the list
        if i not in duplicates: # if it is not a duplicate
            duplicates.append(i) # it appends it to list
            duplicates.append('\n') # creates a new line in the text area 

    text.insert(1.0, ''.join(duplicates)) # adds the new data onto the text area
    text.delete('end-1c', 'end') # To remove the extra line.


def CopyToTextBox(p, selected): # a subroutine that writes the user input into the file passed in through the parameters 
    AnagramFile = open(p, "a") # opens the file in append mode so that not data is overwritten
    AnagramFile.write(selected) # writes the user input into the file


def AddUserInputIntoList(p, year): # a subroutine that stores the original anagram word entered by the user into a file
    OriginalWordFile = open(p, "a") # opens the file in append mode so that not data is overwritten
    wordToBeEntered = enterWord.get() # gets the value of the user input from the text box
    OriginalWordFile.write(wordToBeEntered) # writes the user input value into the file
    OriginalWordFile.write("\n") # adds a new line to the file


    s = CheckAnagram(year) # creates an instance of the CheckAngram class
    s.AddToList() # calls the method AddToList


    clearAnagram() # calls the subroutine to clear the entry boxes and text area


def clearAnagram(): # a subroutine that clears the entry box and text areas
    enterWord.delete(0, tk.END) # deletes the contents of the entry box
    AnagramtextArea.delete(1.0, tk.END) # deletes the contents of the text area
    selectedAnagrams.delete(1.0, tk.END) # deletes the contents of the text area











### main window ###
window1 = tk.Tk() # creates the root window
width = window1.winfo_screenwidth() # gets the full width of the screen of the computer/monitor screen
height = window1.winfo_screenheight() # gets the full height of the screen of the computer/monitor screen
window1.geometry("%dx%d" % (width, height)) # multiplies the width and height to make the window appear in full screen
window1.title("Start Page") # creates the title of the window
window1.configure(bg="light grey") # makes the back ground colour of the window light grey
title1 = tk.Label(window1, text = "Interhouse Spelling Bee Game", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 80)) # title label
title2 = tk.Label(window1, text = "Login:", fg = "black", bg = "light grey", font = ("Lao Sangam MN", 50)) # login label
# button that leads to the student login section
studentButton = tk.Button(window1, text = "Students", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenStudentLogin) 
# button that leads to the teacher login section
teacherButton = tk.Button(window1, text = "Teachers", fg = "black", width = 40, height = 5, font = ("Lao Sangam MN", 15), command=OpenTeacherLogin) 

### positions of the lables and buttons ###
title1.place(x=200, y=200)
title2.place(x=660, y=320)
teacherButton.place(x=250, y=450)
studentButton.place(x=800, y=450)





access = AccessFiles()
access.EditLoginFiles()
window1.mainloop() # calls the main root window
