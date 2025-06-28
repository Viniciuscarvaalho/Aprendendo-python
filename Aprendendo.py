print('Olá, mundo')

Nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer', Nome)

idade = input('Qual é a sua idade? ')
print('Ótimo!')

peso = input('Qual é o seu peso? ')
print('Confira os seus dados abaixo:')
print(Nome, idade, peso)

print('Deu tudo certo, agora vamos para a Fase 2')
print('Fase 2')

pretende = input('Qual a data que vai começar a aprender Inglês ')
print('Isso aí, o primeiro passo é o maior de todos!')

sonhos = input('Por que está tentando aprender isso? ')
print('Continue!')

onde = input('Onde você quer chegar? ')
print('Acreditamos em você!!')

print('Fase 3')
print('Treine seu inglês')
print('Vamos aprender as seguintes palavras em Inglês!!')

resposta1 = input('gato: ')
if resposta1.lower() == 'cat':
    print('Certo!')
else:
    print('Errado! A resposta correta é "cat".')

resposta2 = input('Cachorro: ')
if resposta2.lower() == 'dog':
    print('Certo!')
else:
    print('Errado! A resposta correta é "dog".')

resposta3 = input('leão: ')
if resposta3.lower() == 'lion':
    print('Certo!')
else:
    print('Errado! A resposta correta é "lion".')

resposta4 = input('girafa: ')
if resposta4.lower() == 'giraffe':
    print('Certo!')
else:
    print('Errado! A resposta correta é "giraffe".')

resposta5 = input('Lagartixa: ')
if resposta5.lower() == 'lizard':
    print('Certo!')
else:
    print('Errado! A resposta correta é "lizard".')

resposta6=input('camaleão')
if resposta6.lower() == 'chameleon':
    print('certo')
else:
    print('Errado a resposta correta é" chameleon".')




print('Fase 4')
print('Forme as seguintes frases:')

questions = [
    {"sentence": "I usually _____ coffee in the morning to wake up.", "answer": "drink"},
    {"sentence": "She was very tired, _____ she went to bed early.", "answer": "so"},
    {"sentence": "We have been friends _____ childhood.", "answer": "since"},
    {"sentence": "He _____ his homework before watching TV yesterday.", "answer": "did"},
    {"sentence": "They _____ to the gym every weekend.", "answer": "go"}
]

for q in questions:
    print(q["sentence"])
    resposta = input("Complete com a palavra correta: ").strip().lower()
    if resposta == q["answer"]:
        print("Correto!\n")
    else:
        print(f"Errado! A resposta certa é '{q['answer']}'.\n")

print('Parabéns por completar a sua primeira prova!')
