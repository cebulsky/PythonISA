# napisz program ktory przyjmuje zdanie od uzytkownika (input)
#
# jezeli napis zaczyna sie na litere 'a' - powiedz uzytkownikowi ze zaczyna sie od pierwszej litery alfabetu
# jezeli na litere 'z' - powiedz uzytkownikowi ze zaczyna sie od ostatniej litery alfabetu
# w przeciwnym razie powiedz ze zaczyna sie od innej litery niz 'a' i 'z'

temperature = int(input("Podaj temperature: "))
HOT_TEMPERATURE = 30
WARM_TEMPERATURE = 25
NOT_COLD_NOT_WARM_TEMPERATURE = 20

if (temperature >= HOT_TEMPERATURE):
    print("It's hot")
elif (temperature >= WARM_TEMPERATURE):
    print("It's warm")
elif (temperature >= NOT_COLD_NOT_WARM_TEMPERATURE):
    print("It's not warm or cold")
else:
    print("It's cold")



