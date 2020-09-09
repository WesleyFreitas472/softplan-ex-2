# Exercício 1 - SoftPlan - Algoritmos
Você deverá criar uma API's com um endpoint (em sua linguagem preferida):

Path relativo "/valueWithTaxes" 
Verbo POST
Exemplo de payload: {
	tax: 2.2
	amount: 10000
}

O retorno deverá ser o valor “amount” acrescido dos juros “tax” correspondentes.

{valueWithTaxes: 10220.00 }

### Instruções
*   pip install -r requirements.txt -> Instalar dependencias
*   python test.py -v -> Executar os testes
*   python main.py -> Executa a API localmente

### Projeto
Projeto desenvolvido utilizando python 3.6 e feito o deploy no Heroku.

Usei o flask para desenvolver a API por conta da sua simplicidade, assim não utilizei recursos que não seriam necessários.

Como visto no exemplo do enunciado, assumi que o amount será do tipo int e o tax do tipo float, o retorna, se correta a requisição, é um float.

### Organização
*   main.py -> inicia o sistema
*   API -> Pasta com o projeto da api
    *   app -> Aplicação que calcula o valor acrescido de taxas
        *   models -> Contém os modelos de dados, se fosse para persistir dados num banco ou arquivo, essa seria classe responsável por herdar do framework que iria se comunicar com o banco ou gravar no arquivo.
        *   views -> Funções responsáveis por tratar os endpoints
        *   payloads -> Aqui eu crio os modelos payloads esperados para cada endpoint
        *   validatorPayload -> Contém a função que é responsável por verificar se o payload passado corresponde com o payload esperado
   
*   tests.py -> executa os testes do sistema

#### Testes (unittest)

*   Testo se o validador de payload realmente funciona (testIfPayloadValidatorWorks);
*   Testo se o model está calculando certo o valor acrescido de tax (testIfModelCalculateRight);
*   Testo se realmente é da erro caso seja passado uma string no método getValueWithTaxes (testIfTaxIsStringShowRaiseTypeError);
*   Testo se os tipos dos parametros do payload fazem a API disparar um Bad Request (testIfClientPassParameterWithWrongType);
*   Testo se o cliente não passar payload é retornado um Bad Request (testIfClientDontPassPayload)


Endpoint do projeto deployado -> https://values-softplan.herokuapp.com/valueWithTaxes

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"amount":100,"tax":2.2}' \
  https://values-softplan.herokuapp.com/valueWithTaxes
