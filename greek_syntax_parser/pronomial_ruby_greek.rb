puts "Ruby!"

# comments in Ruby are like in python, parsed by "#"

def personal_pronomials()
	puts "JAG"
	puts "ego, NV"
	puts "emou, G (mou enklitisk form)"
	puts "emoi, D (moi enklitisk form)"
	puts "eme, A (me enklitisk form)"
	puts "DU (accenterade former, enklitiska har ej diakritiska tecken {syns ej här dock})"
	puts "sy, NV"
	puts "sou, G"
	puts "soi, D"
	puts "se, A"
	puts "VI"
	puts "emeis, NV"
	puts "emon, G"
	puts "emin, D"
	puts "emas, A"
	puts "NI"
	puts "ymeis, NV"
	puts "ymon, G"
	puts "ymin, D"
	puts "ymas, A"
end

personal_pronomials()

def demonstrative_pronomials()
	printf("%-10s %-30s", "", "Demonstrative pronomials\n")
	printf("%-5s %-10s %-10s %-10s %-10s %-10s %-10s\n", "", "SM", "SF", "SN", "PM", "PF", "PN")
	# first argument is "formatting string"
	printf("%-10s %-10s %-10s %-10s %-10s %-10s %-10s\n", "N", "ode", "ede", "tode", "oide", "aide", "tade")
	printf("%-10s %-10s %-10s %-10s %-10s %-10s %-10s\n", "G", "toude", "tesde", "toude", "tonde", "tonde", "tonde")
	printf("%-10s %-10s %-10s %-10s %-10s %-10s %-10s\n", "D", "tode", "tede", "tode", "toisde", "taisde", "toisde")
	printf("%-10s %-10s %-10s %-10s %-10s %-10s %-10s\n", "A", "tonde", "tende", "tode", "tousde", "tasde", "tade")
end

demonstrative_pronomials()

def interogative_pronomials()
	printf("%-10s %-30s\n", "", "Interogative pronomials")
	printf("%-10s %-10s %-10s %-10s %-10s\n", "", "S(M/F)", "SN", "P(M/F)", "PN")
	# first argument is "formatting string"
	printf("%-10s %-10s %-10s %-10s %-10s\n", "N", "tis", "ti", "tines", "tina")
	printf("%-10s %-10s %-10s %-10s %-10s\n", "G", "tinos/tou", "tinos/tou", "tinon", "tinon")
	printf("%-10s %-10s %-10s %-10s %-10s\n", "D", "tini/to", "tini/to", "tisi(n)", "tisi(n)")
	printf("%-10s %-10s %-10s %-10s %-10s\n", "A", "tina", "ti", "tinas", "tina")
end

interogative_pronomials()
