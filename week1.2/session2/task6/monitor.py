# Week 1.2, Session 2: Task 6

temperature = input(int("Please enter a temperature "))
pressure = input(int("Please enter the pressure"))
status = input(int("Please enter the status"))

if temperature >80:
    print("Error: Temperature is too high")

elif temperature >=50 and temperature <=80:
    print("Temperature is within the safe limits")

else:
    print("The temperature is low")


    if pressure >100:
        print("Error high pressure is detected")

    elif pressure >= 70 and temperature <= 100:
        print("The pressure is stable")

    else:
        print("The pressure is low")


        if status == 1:
            print("The machine is currently operating")
        else:
            print("Thw machine has stoppe opperating")
            if status > 1:
                print("Please enter a value in between 1 and 0")

                

        








