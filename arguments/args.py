#A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string
def concatenates_args(**strings):
  for str in strings:
    arguments+=str
    return arguments
    #A function named concatenate_kwargs that takes any number of string arguments in keyword 
    # arguments  format and concatenates them into a single string
  def concatenate_kwargs(*str1):
       stringed= ""
       for key,value in str1.items():
         str1+=(f"{key}{value}")
       return stringed
