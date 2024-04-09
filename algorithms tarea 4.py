
def greet(hour):

    if hour < 18:
      return "good morning"
    else:
      return "good afternoon"

hour = int(input("Enter the hour (0-23): "))
print(greet(hour))
