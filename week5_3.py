def my_logger(orig_func):
   import logging
   logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

   def wrapper(*args, **kwargs):
       logging.info(
           'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
       return orig_func(*args, **kwargs)

   return wrapper


@my_logger
def display_info(name, age):
   print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Johnny', 20)


def display_info2(name, age):
   import logging
   logging.basicConfig(filename='{}.log'.format(display_info2.__name__), level=logging.INFO)
   logging.info(
           'Ran with args: {}, and kwargs: {}'.format((name,age), {}))
   print('display_info ran with arguments ({}, {})'.format(name, age))


display_info2('Johnny', 20)
