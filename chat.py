import g4f

g4f.debug.logging = False # enable logging
g4f.check_version = False # Disable automatic version checking
#print(g4f.version) # check version
#print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')
    
while(1):    
# normal response
    answ = input("Введите запрос: ")
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": answ}],
    )  # alternative model setting

    print(response)