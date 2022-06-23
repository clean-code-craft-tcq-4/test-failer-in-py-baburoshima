from alerterstub import network_alert_stub 
alert_failure_count = 0
THRESHOLD_TEMP = 200

def network_alert(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius<=THRESHOLD_TEMP):    
      returnCode = 200     # Return 200 for ok
    elif(celcius>THRESHOLD_TEMP):
      returnCode = 500     # Return 500 for not-ok
    return returnCode


def alert_in_celcius(farenheit, testenv):
    celcius = (farenheit - 32) * 5 / 9
    if testenv=='stub':
        returnCode = network_alert_stub(celcius)
    else:
        returnCode = network_alert(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(303.6, 'stub')
assert(alert_failure_count==0)
alert_in_celcius(303.6, 'prod')
assert(alert_failure_count==0)
alert_in_celcius(400.5 ,'stub')
assert(alert_failure_count==1)
alert_in_celcius(400.5 , 'prod')
assert(alert_failure_count==1)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
