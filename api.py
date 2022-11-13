from fastapi import FastAPI, Response, Query,HTTPException 
from TratamentoDisponibilidadeNFE import ConsultaDisponibilidadeNFE
from typing import List, Optional
Consulta = ConsultaDisponibilidadeNFE()
Pesquisa = Consulta.Pesquisa()

app = FastAPI()
@app.get("/CDS/", name="Consulta-Disponibilidade-Sefaz", description='Rota onde você consegue ver o Status de NFe na Sefaz')
def Search(estados: List[str] = Query(None))-> Optional[List]:
    if(estados == None):
        return Response(content=Pesquisa, media_type="application/json")
    else:
        SeparaEstados = [s.split(',') for s in estados]
        Search = Consulta.Pesquisa(SeparaEstados[0])
        if(Search != 400):
            return Response(content=Search, media_type="application/json")
        else:
            raise HTTPException(status_code=400, detail='Verificar se as siglas está correta')