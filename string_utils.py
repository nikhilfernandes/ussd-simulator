import re
class StringUtils:

  @classmethod
  def camelize(cls, str):        
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).capitalize(), str.title())

  
