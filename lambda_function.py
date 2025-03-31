import boto3

def lambda_handler(event, context): 
    ec2 = boto3.client('ec2', region_name='sa-east-1')

    # Definição dos filtros
    filters = [
        {'Name': 'tag:ambiente', 'Values': ['dev']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]

    # Listar instâncias que atendem aos filtros
    instances = ec2.describe_instances(Filters=filters)

    # Pegando as IDs das instâncias em execução
    instances_to_stop = [
        instance['InstanceId']
        for reservation in instances['Reservations']
        for instance in reservation['Instances']
    ]

    # Se houver instâncias para parar, executa a ação
    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print(f"Desligando as instâncias: {instances_to_stop}")
    else: 
        print("Nenhuma instância encontrada com o ambiente de dev")