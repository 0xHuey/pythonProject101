#Way to hold information in "Key Value" pairs

monthConversions = {
#Always create the Dictionary in the brackets
#Examplple Jan = Key and January = Value

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("luv", "Not a valid key"))