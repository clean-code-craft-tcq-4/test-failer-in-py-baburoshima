from alerterstub import network_alert_stub 
alert_failure_count = 0
THRESHOLD_TEMP_inCelsius = 200

def network_alert(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius<=THRESHOLD_TEMP_inCelsius):    
      returnCode = 200     # Return 200 for ok
    elif(celcius>THRESHOLD_TEMP_inCelsius):
      returnCode = 500     # Return 500 for not-ok
    return returnCode

def alert_in_celcius(farenheit, network_alert_func): #improved by using function pointer
    celcius = (farenheit- 32) * 5 / 9
    returnCode = network_alert_func(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(303.6, network_alert)
assert(alert_failure_count==0)
alert_in_celcius(303.6, network_alert_stub)
assert(alert_failure_count==0)
alert_in_celcius(400.5 , network_alert)
assert(alert_failure_count!=0)
alert_in_celcius(400.5 , network_alert_stub)
assert(alert_failure_count!=0)
print(f'{alert_failure_count} alerts failed.')
print('All is well')