class User:
  '''
  Class that generates new instances of Users
  '''
  user_list=[]

  def __init__(self,username,password):
    self.username=username
    self.password=password