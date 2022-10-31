import torch, numpy as np

class Net(torch.nn.Module):
  def __init__(self, input_size, hidden_size):
    super(Net, self).__init__()
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size) #full connected
    self.relu = torch.nn.ReLU() #(0, infinito)
    self.fc2 = torch.nn.Linear(self.hidden_size, 1)
    self.sigmoid = torch.nn.Sigmoid() #(0, 1)
  def forward(self, x):
    hidden = self.fc1(x)
    relu = self.relu(hidden)
    output = self.fc2(relu)
    output = self.sigmoid(output)
    return output



def predict(larg_sepala, comp_sepala, larg_petala, comp_petala, modelo):

    input_size = entrada.size()

    modelo = Net(input_size,hidden_size=10)
    modelo.load_state_dict(torch.load('./modelo/iris.dat'))
    modelo.eval()

    dados = [larg_sepala, comp_sepala, larg_petala, comp_petala]
    entrada = torch.FloatTensor(dados)

    y_pred = modelo(entrada)

    return y_pred