relwords = [
    'klokken', 'morgen', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag',
    'lørdag', 'søndag', 'velkommen', 'kl', 'bursdag', 'bursdagsfeiring',
    'hjemme', 'hos', 'moro', 'kake', 'kaker', 'brus', 'is', 'veien', 'beskjed',
    'fotball', 'blir', 'håper', 'passer', 'meg', 'kontakt'
]
klokkeslett = []
for i in range(0, 24):
    klokkeslett.append(i)
    for o in range(60):
        if len(str(o)) == 1:
            o = (f"0{o}").strip()
        klokkeslett.append((f"{i}:{o}").strip())
        klokkeslett.append((f"{i}.{o}").strip())
        klokkeslett.append((f"{i}{o}").strip())

relevanse = relwords + klokkeslett


#Main code, used to verify message
def verifier(message):
    kvalifikasjoner = []
    points = 0
    wordslist = message.split(' ')
    if (len(wordslist) > 7 and len(wordslist) < 100):
        print(f'1st level checked, message length is {len(wordslist)} ')
        for word in wordslist:
            word = word.strip(",.?!=")
            if word in relevanse or word.lower() in relevanse or word.title(
            ) in relevanse:
                points += 1
                kvalifikasjoner.append(word)
        if (points >= 3):
            return (
                f"The following message is most likely a genuine and relevant message:'{message}', because it is {len(wordslist)} words long and contains these promising words: {kvalifikasjoner} "
            )

        else:
            print('Check 2 did not pass')

    else:
        print('Message did not qualify, and is therefore discarded')


#Test your code
while True:
    print(verifier(input('Write your message here: ')))