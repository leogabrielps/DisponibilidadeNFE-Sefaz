# Simple API usando o Tratamento Disponibilidade NFE

Para ligar a API é apenas necessário dar um:
```console
uvicorn api:app --reload
```

A rota padrão para a consulta de Disponibilidade é */CDS/?estados={ID}
Exemplos de requisições:
``console
curl 127.0.0.1:8000/CDS/?estados=MT
Resposta:
[{"autorizador":"MT","autorizacao":"verde","retorno_autorizacao":"verde","inutilizacao":"verde","consulta_protocolo":"verde","status_servico":"verde","consulta_cadastro":"verde","recepcao_evento":"verde"}]
---
curl 127.0.0.1:8000/CDS/?estados=MT,SP
Resposta:
[{"autorizador":"MT","autorizacao":"verde","retorno_autorizacao":"verde","inutilizacao":"verde","consulta_protocolo":"verde","status_servico":"verde","consulta_cadastro":"verde","recepcao_evento":"verde"},{"autorizador":"SP","autorizacao":"verde","retorno_autorizacao":"verde","inutilizacao":"verde","consulta_protocolo":"verde","status_servico":"verde","consulta_cadastro":"verde","recepcao_evento":"verde"}]
```