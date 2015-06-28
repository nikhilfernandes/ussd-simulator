import re
class StringUtils:

  @classmethod
  def camelize(cls, str):        
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).capitalize(), str.title())

  @classmethod
  def is_number(cls, s):
      try:
          float(s)
          return True
      except ValueError:
          pass
 
      try:
          import unicodedata
          unicodedata.numeric(s)
          return True
      except (TypeError, ValueError):
          pass
 
      return False
