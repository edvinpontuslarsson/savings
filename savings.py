savings = 0
years = 0

monthly_saving = int(input("How many dollars can you save per month? "))

while(years < 40):
    savings += monthly_saving * 12
    savings *= 1.12  # increases with average of 12 % every year

    years += 1

    if (years < 10 or years % 5 == 0):
        print("$", '{:,}'.format(round(savings)), "after", years, "years")
