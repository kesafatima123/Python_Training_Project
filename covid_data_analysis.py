# importing the requests library
import requests
class covid:
    name='abc'
    user=0

    def getName(self):
        print("Welcome in my world")
        self.name = input("Enter your name: ")
        print("Hello",self.name )        
        self.getInput()
        
    def getInput(self):
        self.user = input("What do you want to see?\nClick 1 for Country Current Status or Click 2 for Province Wise Result: ")
        self.begin()

    def begin(self):
        if self.user == '1':
            self.countrycurentstatus()
        elif self.user == '2':
            self.provincewiseresult()
        else: 
            print('Invalid Input')
            self.startOver()
    
    def end(self):
        print("You are out from my world")


    def countrycurentstatus(self):    
        URL = "https://api.covid19api.com/dayone/country/india"
        r = requests.get(url = URL)
        
        # extracting data in json format
        data = r.json()
        length = len(data)
        new_data = data[length-1]
        val = ''
        val +="Country =>"+new_data['Country']+"\n"
        val +="Confirmed =>"+str(new_data['Confirmed'])+"\n"
        val +="Deaths =>"+str(new_data['Deaths'])+"\n"
        val +="Recovered =>"+str(new_data['Recovered'])+"\n"
        val +="Active =>"+str(new_data['Active'])+"\n"
        print(val)
        self.startOver()
           
    def provincewiseresult(self):
        URL = "https://api.covid19api.com/live/country/india/status/confirmed"
        r = requests.get(url = URL)
        
        # extracting data in json format
        data = r.json()
        for i in range(len(data)):
            val =""
          
            new_data = data[i]
            
            val +="Province =>"+new_data['Province']+"\n"
            val +="Confirmed =>"+str(new_data['Confirmed'])+"\n"
            val +="Deaths =>"+str(new_data['Deaths'])+"\n"
            val +="Recovered =>"+str(new_data['Recovered'])+"\n"
            val +="Active =>"+str(new_data['Active'])+"\n"
            print(val)
        self.startOver()
        
    
    def startOver(self):
        inp = input("Press 0 to start Over or Press 1 to continue: ")
        if inp == '0':
            self.getName()
        elif inp == '1':
            self.getInput()
        else:
            print("Invalid Input")
            self.end()
            
obj = covid()
obj.getName()