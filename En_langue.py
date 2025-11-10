Nom = None

# Correction : Retirez la f-string et insérez le placeholder `{name}`
Fr = {
    "main.69.m": "Bienvenue, {name} !\nTu veux faire quoi ?",
}

En = {
    "main.69.m": "Welcome, {name}!\nWhat would you like to do?",
} 

#.format(name = nom if nom else 'Invité')