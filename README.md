
**Projeto de Pesquisa de Dados Empresariais e Geração de Relatório com Docker**

Este projeto Python visa simplificar e automatizar a pesquisa de dados empresariais por meio de filtros, como razão social, porte, CNAE (Classificação Nacional de Atividades Econômicas), natureza jurídica e muito mais. Ao fornecer esses filtros, o projeto recolherá informações relevantes sobre as empresas e, em seguida, gerará um relatório em formato Excel que contém os dados coletados.

**Recursos e Funcionalidades:**

- Pesquisa de Dados Empresariais: O projeto permite aos usuários inserir diversos filtros, como razão social, porte, CNAE e natureza jurídica, para recuperar informações detalhadas sobre empresas que atendam aos critérios definidos.

- Geração de Relatório em Excel: Com base nos filtros fornecidos, o projeto gera automaticamente um relatório em formato Excel contendo os dados das empresas pesquisadas. Isso oferece uma forma conveniente de visualizar e analisar os resultados da pesquisa.

- Download Automático: O relatório gerado é disponibilizado para download automático no navegador do usuário. Isso garante uma experiência fluida e direta para acessar os resultados da pesquisa.

- Dockerização: O projeto é dockerizado, facilitando a implantação e a execução em diversos ambientes. Com o Dockerfile fornecido, é possível criar um contêiner Docker que contenha todas as dependências necessárias para a execução do projeto.

**Instruções de Uso:**

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Docker instalado em seu sistema.
3. No terminal, navegue até o diretório do projeto.
4. Execute o seguinte comando para construir a imagem Docker:
   ```
   docker build -t pesquisa-empresarial .
   ```
5. Após a construção da imagem, execute o projeto no Docker com o seguinte comando:
   ```
   docker run -p 8080:8080 pesquisa-empresarial
   ```
6. Abra o navegador e acesse http://localhost:8080 para acessar a interface do projeto.
7. Insira os filtros desejados e inicie a pesquisa.
8. O relatório Excel será gerado automaticamente e estará disponível para download no navegador.

Este projeto demonstra a capacidade de utilizar o Docker para encapsular e executar aplicativos Python de forma independente do ambiente, facilitando a implantação e o compartilhamento. Além disso, fornece uma solução eficiente para a pesquisa de dados empresariais e geração de relatórios personalizados.
