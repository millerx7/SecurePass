# 🔐 SecurePass - Gerador de Senhas Seguras

Este projeto é um **gerador de senhas aleatórias e seguras** desenvolvido em Python. Ele utiliza o módulo `secrets`, que é mais seguro que `random`, sendo ideal para gerar senhas fortes para usos pessoais, profissionais ou acadêmicos.

---

## 🛠 Funcionalidades

- 🔒 Geração de senhas com letras maiúsculas, minúsculas, números e símbolos
- 📏 Personalização do tamanho da senha pelo usuário
- ✅ Segurança criptográfica com `secrets`
- 🖥 Interface em linha de comando (terminal)

---

## 📂 Estrutura do Projeto

```
SecurePass/
├── gerador_senha.py   # Script principal para geração de senhas
└── README.md          # Documentação do projeto
```

---

## ▶️ Como usar

1. Certifique-se de ter o **Python 3.6 ou superior** instalado.

2. Clone o repositório:

```bash
git clone https://github.com/millerx7/SecurePass.git
```

3. Acesse a pasta do projeto:

```bash
cd SecurePass
```

4. Execute o script:

```bash
python gerador_senha.py
```

5. Quando solicitado, informe o tamanho da senha desejada.

**Exemplo de uso:**

```
Digite a quantidade de caracteres que você quer na senha: 16
A senha forte gerada foi: L@9z#fP1wT8&rMq2
```

---

## 🔒 Segurança

Este projeto utiliza o módulo `secrets`, que é recomendado para geração de dados sensíveis como senhas, chaves de acesso e tokens. Ele oferece segurança **criptograficamente forte**, diferente do `random`.

---

## ⚠️ Observações

- As senhas geradas são seguras, mas é responsabilidade do usuário armazená-las adequadamente.
- Este projeto é para fins educacionais e práticos. Use com responsabilidade.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para estudar, modificar e utilizar em seus próprios projetos!

---

## 👨‍💻 Autor

**Guilherme Miller Nunes Costa**  
Aluno de Telemática - IFPB  
Contato: guilhermemiller.dev@gmail.com
