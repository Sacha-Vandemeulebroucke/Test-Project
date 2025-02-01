

def day_of_week(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return "Invalid day"

print(day_of_week("Saturday"))

print(dir())