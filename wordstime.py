
NUM=[
    "zero",
    "one", "two", "three", "four", "five", "six", "seven", "eight","nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "thirty",
    "thirty one",
    "thirty two",
    "thirty three",
    "thirty four",
    "thirty five",
    "thirty six",
    "thirty seven",
    "thirty eight",
    "thirty nine",
    "forty",
    "forty one",
    "forty two",
    "forty three",
    "forty four",
    "forty five",
    "forty six",
    "forty seven",
    "forty eight",
    "forty nine",
    "fifty",
    "fifty one",
    "fifty two",
    "fifty three",
    "fifty four",
    "fifty five",
    "fifty six",
    "fifty seven",
    "fifty eight",
    "fifty nine",
    "zero"
]
HOUR = [
    "midnight",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "noon",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "midnight"
]


def wordstime(dd):
    try:
        h = dd.hour
        m = dd.minute
        s = dd.second

        if (h >= 12):
            end = "in the afternoon"
            if h >= 18:
                end = "in the evening"
            if h >= 21:
                end = "at night"
        else:
            end = "in the morning"

        ss = NUM[s]
        mm = NUM[m]
        hh = HOUR[h]
        place = "past"
        if m > 30:
            mm = NUM[60 - m]
            ss = NUM[60 - s]
            hh = HOUR[h + 1]
            place = "to"
        if m == 30 and s > 0:
            mm = NUM[60 - m - 1]
            ss = NUM[60 - s]
            hh = HOUR[h + 1]
            place = "to"

        ret = ""
        if mm != "zero":
            if mm == "one":
                mm = mm + " minute "
            elif (m == 15 or m == 45) and s == 0:
                mm = "quarter "
            elif m == 30 and place == "past" and s == 0:
                mm = "half "
            else:
                mm = mm + " minutes "

            if m == 59 and s > 0:
                ret = ""
            else:
                ret = mm
            if ss != "zero":
                if ret:
                    ret = ret + "and "
        if ss != "zero":
            if ss == "one":
                ret = ret + ss + " second "
            else:
                ret = ret + ss + " seconds "

        if mm != "zero" or ss != "zero":
            ret = ret + place + " "
        ret = ret + hh
        if not (hh == "noon" or hh == "midnight"):
            ret = ret + " o'clock " + end
        return ret #, mm,ss,place,hh,end

    except Exception as e:
        raise Exception('error from {}'.format(dd)) from e
