from wordstime import wordstime
import datetime as dt



def test_wordstime():
    assert wordstime(dt.time(0,0,0)) == "midnight"
    assert wordstime(dt.time(1,0,0)) == "one o'clock in the morning"
    assert wordstime(dt.time(12,0,0)) == "noon"
    assert wordstime(dt.time(13,0,0)) == "one o'clock in the afternoon"
    assert wordstime(dt.time(18,0,0)) == "six o'clock in the evening"
    assert wordstime(dt.time(21,0,0)) == "nine o'clock at night"

    assert wordstime(dt.time(23,29,59)) == "twenty nine minutes and fifty nine seconds past eleven o'clock at night"
    assert wordstime(dt.time(23,30,0)) == "half past eleven o'clock at night"
    assert wordstime(dt.time(23,30,1)) == "twenty nine minutes and fifty nine seconds to midnight"
    assert wordstime(dt.time(23,59,58)) == "two seconds to midnight"
    assert wordstime(dt.time(23,59,59)) == "one second to midnight"

    assert wordstime(dt.time(0,0,1)) == "one second past midnight"
    assert wordstime(dt.time(0,0,59)) == "fifty nine seconds past midnight"
    assert wordstime(dt.time(0,29,59)) == "twenty nine minutes and fifty nine seconds past midnight"
    assert wordstime(dt.time(0,30,0)) == "half past midnight"
    assert wordstime(dt.time(0,30,1)) == "twenty nine minutes and fifty nine seconds to one o'clock in the morning"
    assert wordstime(dt.time(0,30,59)) == "twenty nine minutes and one second to one o'clock in the morning"
    assert wordstime(dt.time(0,31,0)) == "twenty nine minutes to one o'clock in the morning"

    assert wordstime(dt.time(11,29,59)) == "twenty nine minutes and fifty nine seconds past eleven o'clock in the morning"
    assert wordstime(dt.time(11,30,0)) == "half past eleven o'clock in the morning"
    assert wordstime(dt.time(11,30,1)) == "twenty nine minutes and fifty nine seconds to noon"
    assert wordstime(dt.time(11,59,58)) == "two seconds to noon"
    assert wordstime(dt.time(11,59,59)) == "one second to noon"

    assert wordstime(dt.time(12,0,1)) == "one second past noon"
    assert wordstime(dt.time(12,0,59)) == "fifty nine seconds past noon"
    assert wordstime(dt.time(12,29,59)) == "twenty nine minutes and fifty nine seconds past noon"
    assert wordstime(dt.time(12,30,0)) == "half past noon"
    assert wordstime(dt.time(12,30,1)) == "twenty nine minutes and fifty nine seconds to one o'clock in the afternoon"
    assert wordstime(dt.time(12,30,59)) == "twenty nine minutes and one second to one o'clock in the afternoon"
    assert wordstime(dt.time(12,31,0)) == "twenty nine minutes to one o'clock in the afternoon"


