import json
grafo_inicial= {}
bob = {}
davi = {}
carlos = {}
ernesto = {}
fernanda = {}
gustavo = "you find gustavo"
grafo_inicial["alice"] = [bob,davi,carlos]
bob["bob"]= [ernesto]
davi["davi"] = [gustavo]
carlos["carlos"] = [fernanda]
ernesto["ernesto"] = [gustavo]
fernanda["fernanda"] = [gustavo]

print(json.dumps(
    grafo_inicial,
    sort_keys=True,
    indent=3,
    separators=(',', ': ')
))

