import torch, numpy as np

modelo = Net()

modelo.load_state_dict(torch.load('./modelo/iris.dat'))
modelo.eval()

def predict(larg_sepala, comp_sepala, larg_petala, comp_petala, modelo):
    dados = [larg_sepala, comp_sepala, larg_petala, comp_petala]
    entrada = torch.FloatTensor(dados)

    y_pred = modelo(entrada)

    return y_pred