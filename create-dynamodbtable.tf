provider "aws" {
  region = "sa-east-1"
}

resource "aws_dynamodb_table" "exemple" {
  table_name   = "meu-dynamodb-lab-ia"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = { 
    Name        = "MyDynamoDBTerraform"
    Environment = "Dev"
  }
}

output "aws_dynamodb_table_name" {
  value = aws_dynamodb_table.exemple.name
}

# Usando o template do Terraform:
# 1. Abrindo um provider para a AWS na região sa-east-1 (São Paulo).
# 2. Criando um recurso do DynamoDB (tabela).
# 3. Definindo o nome da tabela, o tipo de pagamento como "PAY_PER_REQUEST" e a chave de partição.
# 4. Definindo o atributo da chave de partição como "S" (String).
# 5. Criando tags para o recurso, incluindo "Name" e "Environment".
# 6. Criando um output para exibir o nome da tabela quando rodarmos o código para criar a infraestrutura.