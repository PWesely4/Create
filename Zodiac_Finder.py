Zodiac_List = ["Capricorn","Aquarius","Pisces","Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius"]
Month_List = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Birth_Month = input("What is your Birth Month? ")
Birth_Day = int(input("What is your Birth Day "))
x = 0
Zodiac = "Shouldn't be this"
def Zodiac_finder():
  global Zodiac_List, Birth_Month, x, Month_List, Zodiac
  for month in Month_List:
    if Birth_Month == Month_List[x]:
      print(x)
      print(type(x))
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
      print(Zodiac)
    x += 1
Zodiac_finder()