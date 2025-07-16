def status(status):
   match status:
      case(400):
         return ('hello')
      case(500):
         return ('hello world')
      case(600):
         return ('hello bibek')
      
print(status(500))