Zodiac_List = ["Capricorn","Aquarius","Pisces","Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius"]
Month_List = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Month = input("What is your Birth Month? ")
x = 0
Zodiac = " "
def Zodiac_finder(Birth_Day):
  global Zodiac_List, Month, x, Month_List, Zodiac
  for month in Month_List:
    if Month == Month_List[x]:
      #print(x)
      #print(type(x))
      if x == 0:
        if Birth_Day < 20:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 1:
        if Birth_Day < 19:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 2:
        if Birth_Day < 21:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 3:
        if Birth_Day < 20:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 4:
        if Birth_Day < 21:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 5:
        if Birth_Day < 21:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 6:
        if Birth_Day < 23:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 7:
        if Birth_Day < 23:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 8:
        if Birth_Day < 23:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 9:
        if Birth_Day < 23:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 10:
        if Birth_Day < 22:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      elif x == 11:
        if Birth_Day < 22:
          Zodiac = Zodiac_List[x]
        else: Zodiac = Zodiac_List[x+1]
      print("You are a " + Zodiac)
    x += 1
Day = int(input("What is your Birth Day "))
Zodiac_finder(Day)