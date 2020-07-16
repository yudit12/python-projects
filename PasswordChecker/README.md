## Password checker  </br>
read passwords from given password file you want to check  if they  ever been hacked </br>
return how many time each password was hacked  (using API) </br>

The password strength based on k-anonymity k-anonymity concept  </br>
k-anonymity mean we allows somebody receive information about us with out knowing who we are  </br>
how it's done?  </br>
when we requests  password pwend API the requests.get url includes the password, converted to hash. furthermore, for more security it add only the first 5 characters of the  result hash password
the response is the all hash password that their beginning  fits to your given password hash beginning
so we get a lot of  fit hash password


