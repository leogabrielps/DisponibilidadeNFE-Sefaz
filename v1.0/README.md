# DisponibilidadeNFE-Sefaz
>*Créditos ao Leogregianin por fazer o [Disponibilidade-NFE](https://github.com/leogregianin/disponibilidade-nfe)*

Projeto tem foco de criar uma função onde a pessoa consegue saber como está a disponibilidade da SEFAZ e também poder escolher um servidor específico.

*Exemplos de chamando a função sem especificar servidor:*

```python
from TratamentoDisponibilidadeNFE import ConsultaDisponibilidadeNFE

Consulta = ConsultaDisponibilidadeNFE()
Pesquisa = Consulta.Pesquisa()
print(Pesquisa)
```

*Resultado:*
```console
[
  {
    "autorizador": "AM",
    "autorizacao": "verde",
    "retorno_autorizacao": "verde",
    "inutilizacao": "verde",
    "consulta_protocolo": "verde",
    "status_servico": "verde",
    "consulta_cadastro": "",
    "recepcao_evento": "verde"
  },
  {
    "autorizador": "BA",
    "autorizacao": "verde",
    "retorno_autorizacao": "verde",
    "inutilizacao": "verde",
    "consulta_protocolo": "verde",
    "status_servico": "verde",
    "consulta_cadastro": "verde",
    "recepcao_evento": "verde"
  },
  {
  ...
  }
]
```

*Exemplos especificando alguns servidores*
```python
Pesquisa = Consulta.Pesquisa(['MT','AM'])
print(Pesquisa)
```
*Resultado:*
```console
[
  {
    "autorizador": "MT",
    "autorizacao": "verde",
    "retorno_autorizacao": "verde",
    "inutilizacao": "verde",
    "consulta_protocolo": "verde",
    "status_servico": "verde",
    "consulta_cadastro": "verde",
    "recepcao_evento": "verde"
  },
  {
    "autorizador": "AM",
    "autorizacao": "verde",
    "retorno_autorizacao": "verde",
    "inutilizacao": "verde",
    "consulta_protocolo": "verde",
    "status_servico": "verde",
    "consulta_cadastro": "",
    "recepcao_evento": "verde"
  }
]
```
