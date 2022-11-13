# OSEF : Open Source Encryption Format
import sys
from os.path import exists
from random import randint as ran

keychars = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e',
  'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
  '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
  '{', '|', '}', '~', ' ', '\t', '\n', '\r'
]

enc_keychars = {}
for kc in keychars:
  curr_ran = ran(0, 10000000)
  while curr_ran in enc_keychars:
    curr_ran = ran(0, 1000000)
  enc_keychars[kc] = curr_ran


def error(msg: str):
  print("ERROR: %s" % msg)
  exit(1)


def encrypt(source: str) -> list:
  tokens = []
  for char in source:
    tokens.append(str(enc_keychars[char]))
  return tokens


def write(file: str, tokens: list):
  with open(file, "w") as out:
    out.write("#".join(tokens))

  key_values = []
  for item in enc_keychars:
    key_values.append(str(enc_keychars[item]))

  with open("out.key", "w") as out:
    out.write("#".join(key_values))


if __name__ == "__main__":
  args = sys.argv[1:]
  if len(args) != 1:
    error("Invalid amount of arguments.\nUsage: %s <file>" % sys.argv[0])

  if exists(args[0]):
    with open(args[0], "r") as f:
      write("out.osef", encrypt(f.read()))
  else:
    error("File `%s` does not exist in current working directory." % args[0])
