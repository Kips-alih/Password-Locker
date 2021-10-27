class User:
  '''
  Class that generates new instances of Users
  '''
  user_list=[]

  def __init__(self,username,password):
    self.username=username
    self.password=password

  def save_user(self):
    '''
    save_user method saves user objects to the user_list
    '''
    User.user_list.append(self)

  @classmethod
  def user_verificate(cls,username,password):
    '''
    Return a boolean on given inputs
    '''
    for user in cls.user_list:
      if user.username==username and user.password==password:
        return True
      return False