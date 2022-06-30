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

def tempconvert(farenheit):
  celcius = (farenheit- 32) * 5 / 9
  return celcius

def alert_in_celcius(farenheit, network_alert_func): #improved by using function pointer
    celcius = tempconvert(farenheit)
    returnCode = network_alert_func(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1

#test for input provided initially
alert_in_celcius(303.6, network_alert)
assert(alert_failure_count==0)
alert_in_celcius(303.6, network_alert_stub)
assert(alert_failure_count==0)

#Test for temparature < threshold
alert_in_celcius(391.5, network_alert)
assert(alert_failure_count==0)
assert(tempconvert(391.5)<200)
alert_in_celcius(391.5, network_alert_stub)
assert(alert_failure_count==0)
#Test for temparature == threshold
alert_in_celcius(392 , network_alert)
assert(tempconvert(392)==200)
assert(alert_failure_count==0)
alert_in_celcius(392 , network_alert_stub)
assert(alert_failure_count==0)

#Test for temparature > threshold in real network
alert_in_celcius(392.5 , network_alert)
assert(tempconvert(392.5)>200)
assert(alert_failure_count==1) #first failure in system
alert_in_celcius(400.5 , network_alert)
assert(alert_failure_count==2)  #second failure in system

#Test for temparature > threshold with stub 
alert_in_celcius(392.5 , network_alert_stub)
assert(alert_failure_count==3)  #third failure in system
alert_in_celcius(400.5 , network_alert_stub)
assert(alert_failure_count==4)  #fourth failure in system
print(f'{alert_failure_count} alerts failed.')
print('All is well')