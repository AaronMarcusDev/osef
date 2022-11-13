from sys import argv
from os.path import exists
from os import system

args = argv[1:]

keychars = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e',
  'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
  '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
  '{', '|', '}', '~', ' ', '\t', '\n', '\r'
]


def error(msg: str):
  print("ERROR: %s" % msg)
  exit(1)


def decrypt(key: str, source: str) -> list:
  result = []
  chars = key.split("#")
  dec_chars = {}

  for i in range(len(keychars) - 1):
    dec_chars[chars[i]] = keychars[i]

  for char in source.split("#"):
    result.append(dec_chars[char])

  return result

def write(file, chars: list):
  with open(file, "w") as f:
    f.write("".join(chars))

if __name__ == "__main__":
  if len(args) != 1:
    if len(args) != 1:
      error("Invalid amount of arguments.\nUsage: %s <file>" % argv[0])

  if exists(args[0]):
    key = input("Enter encryption key: ")
    system("cls||clear")
    with open(args[0], "r") as f:
      write("out.txt", decrypt(key, f.read()))
  else:
    error("File `%s` does not exist in current working directory." % args[0])
