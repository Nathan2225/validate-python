import re

class Validate:

  @staticmethod
  def zip(input):
    if re.match("^[0-9]{5}$", input):
      return True
    return False
  
  @staticmethod
  def minor(age):
    if age > 17:
      return False
    return True
  
  @staticmethod 
  def email(input):
    if "@" in input and "." in input:
      return True
    return False
  
  @staticmethod
  def is_lat(number):
    return number >= -90 and number <= 90
  
  @staticmethod
  def is_lng(number):
    return number >= -180 and number <= 180
  
  @staticmethod
  def is_domain(input):
    if re.match("^[a-zA-Z0-9-]{2,253}\\.[a-zA-Z]{1}[a-zA-Z0-9]{1,}$", input):
      return True
    return False
  
  @staticmethod
  def is_url(input):
    if re.match("^http(s)?:\\/\\/(.*?)\\.[a-z]{2,52}\\/.*$", input):
      return True
    return False
  
  @staticmethod
  def grade(value):
    if value < 60:
      return 'F'
    elif value < 70:
      return 'D'
    elif value < 80:
      return 'C'
    elif value < 90:
      return 'B'
    
    return 'A'
  
  '''
  Typing added to enhance validation
  '''
  @staticmethod
  def sanitize(sql : str) -> str:
    sql = sql.upper().replace("ADMIN", "")
    sql = sql.upper().replace("OR", "")
    sql = sql.upper().replace("COLLATE", "")
    sql = sql.upper().replace("DROP", "")
    sql = sql.upper().replace("AND", "")
    sql = sql.upper().replace("UNION", "")
    sql = sql.replace("/*", "")
    sql = sql.replace("*/", "")
    sql = sql.replace("//", "")
    sql = sql.replace(";", "")
    sql = sql.replace("||", "")
    sql = sql.replace("&&", "")
    sql = sql.replace("--", "")
    sql = sql.replace("#", "")
    sql = sql.replace("=", "")
    sql = sql.replace("!=", "")
    sql = sql.replace("<>", "")

    return sql

  @staticmethod
  def strip_null(input : str) -> str:
    input = input.replace("None", "")

    return input

  '''
  TODO: Implement IP validation. Consider white-list, regex.
  '''
  @staticmethod
  def ip(input: str) -> bool:
    if re.match("\\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b", input):
      return True
    return False
  
  '''
  TODO: Implement MAC address validation. Consider white-list, regex.

  allow : - and whitespaces
  '''
  @staticmethod
  def mac(input: str) -> bool:
    if re.match("^([0-9A-Fa-f]{2}[:-]?){5}([0-9A-Fa-f]{2})$", input):
      return True
    return False
  
  '''
  TODO: Implement md5 validation. Consider white-list, regex.
  '''
  @staticmethod
  def md5(input: str) -> bool:
    if re.match("^[a-fA-F0-9]{32}$", input):
      return True
    return False
