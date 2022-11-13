from DisponibilidadeNFE import DisponibilidadeNFe
import pandas as pd

class ConsultaDisponibilidadeNFE:
    def __init__(self):
        self.statusNFE = DisponibilidadeNFe().get_status()
        self.dfStatus = pd.DataFrame.from_dict(self.statusNFE)
    
    def Pesquisa(self,estados = None):
        lista = []
        seen = set(lista)
        # 1. Verifica se a variável estados está vázia, se tiver manda todos os estados
        if estados is None:
            return self.dfStatus.to_json(orient='records')
        else:
            # 2. Se ela não tiver vazia, verifica se ela é uma lista, se ela não for alertar de um erro
            if isinstance(estados, list):
                for estado in estados:
                    dfWhere = self.dfStatus.where(self.dfStatus['autorizador']==estado.upper()).dropna()
                    # 3. Verifica se o servidor solicitado tem na lista, se não tiver retornar um erro
                    if(dfWhere.empty == False):
                        dfPrincipal = pd.DataFrame(dfWhere)
                        # 4. Coloca os estados no Seen para não houver duplicidade.
                        if estado not in seen:
                            seen.add(estado)
                            lista.append(dfPrincipal)
                    else:
                        return 400 # 'Verificar se as siglas está correta'
                # 5. Após verificar todos os estado da lista enviada, ele faz um concat e retorna para a função
                if lista is not None:
                    dfConcat = pd.concat(lista)
                    return dfConcat.to_json(orient='records')
            else:
                return 'Apenas é permitido enviar em forma de lista.'