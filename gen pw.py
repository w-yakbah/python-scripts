import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def gen_random_password():
	length = int(input("Entrez la longueur du mot de passe (plus de 10 pour la securite): "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))
gen_random_password()