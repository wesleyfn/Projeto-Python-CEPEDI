# Sistema de Gerenciamento de Prontuários Odontológicos Digitais

O sistema cadastra e pesquisa 3 entidadas: 
- Especialista (profissional odontológico)
- Paciente
- Prontuário

## Especialista
O especialista é uma classe que herda informações da classe abstrata pessoa. Nas instâncias dessa classe será guardada as informações dos profissionais de odontologia. Após o cadastro, a instância será gravada em um arquivo .json. Antes de atender algum paciente, o especialista deve se cadastrar no sistema para que suas informações sejam guardadas para posteriormente serem carregadas no prontuário.

## Paciente
O paciente é uma classe que herda informações da classe abstrata pessoa. Nas instâncias dessa classe será guardada as informações dos pacientes cadastrados no sistema. Após o cadastro, a instância será gravada em um arquivo .json. Antes de ser atendido, o paciente deve se cadastrar no sistema para que suas informações sejam guardadas para posteriormente serem carregadas no prontuário.

## Prontuário
O prontuário é uma classe que em usas instacias recebe informações - e por isso depende - do paciente e do especialista para ser construído. Após o cadastro, a instância será gravada em um arquivo .json.

- Sem especialistas ou pacientes não é possível construir um prontuário.
- É recomendado cadastrar pacientes e especialistas no sistema antes de preencher um prontuário.
- Há a opção de atualização de informações das entidades quando é encontrada na busca (não é recomendada).


