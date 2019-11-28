def errors():
     try:
         a=int(input())
     except Exception as e:
       print(type(e).__name__,e)
     except KeyboadInterrupt as e:
        print(type(e).__name__,e)
errors()
