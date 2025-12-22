class Tweet:
    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError("max_length must be at least 1")

        self.__max_length=max_length
        
        if len(message)>self.__max_length:
            self.__message=message[:self.__max_length]
        else:
            self.__message=message
    def get_message(self,):
        print(self.__message)
        return self.__message
    
    def set_message(self,new_msg):
        if len(new_msg)>self.__max_length:
            self.__message=new_msg[:self.__max_length]
        else:
            self.__message=new_msg
  
    def get_max_length(self):
        print(self.__max_length)
        return self.__max_length
    
    def set_max_length(self,length):
        if length < 1:
            raise ValueError("max_length must be at least 1")
        if length < len(self.__message):
            self.__message=self.__message[:length]
        self.__max_length=length
    
tweet=Tweet("123456",5)
tweet.get_message()