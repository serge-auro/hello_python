def division(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return None


def multiplication(a, b):
  try:
    return a * b
  except Exception:
    return None


def addition(a, b):
  try:
    return a + b
  except Exception:
    return None


def subtraction(a, b):
  try:
    return a - b
  except Exception:
    return None
